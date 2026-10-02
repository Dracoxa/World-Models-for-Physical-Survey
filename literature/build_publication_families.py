#!/usr/bin/env python3
"""Build a provisional publication-family layer from the frozen catalog."""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit

from compare_external_surveys import ARXIV_RE, normalize_title


FIELDS = [
    "family_id",
    "canonical_title",
    "year",
    "venue",
    "publication_status",
    "canonical_url",
    "arxiv_ids",
    "doi",
    "record_ids",
    "categories",
    "member_count",
    "resolution_basis",
    "review_status",
]
DOI_RE = re.compile(r"(?:doi\.org/|doi:\s*)(10\.\d{4,9}/[^\s?#]+)", re.I)


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        left, right = self.find(left), self.find(right)
        if left != right:
            self.parent[right] = left


def choose_url(records: list[dict[str, str]]) -> str:
    def score(url: str) -> tuple[int, int]:
        host = (urlsplit(url).hostname or "").lower()
        if "doi.org" in host:
            rank = 5
        elif any(name in host for name in ("acm.org", "aaai.org", "ecva.net", "openaccess.thecvf.com", "openreview.net", "proceedings.mlr.press", "nature.com")):
            rank = 4
        elif "arxiv.org" in host:
            rank = 3
        elif url:
            rank = 2
        else:
            rank = 0
        return rank, -len(url)

    return max((record["url"] for record in records), key=score, default="")


def render_csv(families: list[dict[str, str]]) -> str:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(families)
    return stream.getvalue()


def render_report(
    source_records: list[dict[str, str]],
    records: list[dict[str, str]],
    excluded_records: list[dict[str, str]],
    families: list[dict[str, str]],
    decisions: dict,
) -> str:
    duplicate_families = sum(int(family["member_count"]) > 1 for family in families)
    manual_families = sum("manual_merge" in family["resolution_basis"] for family in families)
    corrected_records = len(decisions["overrides"])
    category_counts = Counter(record["category"] for record in source_records)
    lines = [
        "# Provisional Publication-Family Corpus",
        "",
        f"Snapshot: {decisions['snapshot_date']}. This layer audits all {len(source_records)} source rows, excludes {len(excluded_records)} logged non-publication placeholders, and resolves {len(records)} publication candidates into **{len(families)} provisional publication families**.",
        "",
        "The count is reproducible but not final: exact normalized titles, verified arXiv identifiers, and logged manual decisions are merged; fuzzy similarity alone never merges records. Formal-version resolution and records without canonical identifiers still require review.",
        "",
        "## Accounting",
        "",
        "| Item | Count |",
        "|---|---:|",
        f"| Frozen category records | {len(source_records)} |",
        f"| Excluded non-publication placeholders | {len(excluded_records)} |",
        f"| Publication candidate rows | {len(records)} |",
        f"| Exact normalized candidate titles before family resolution | {len({normalize_title(record['title']) for record in records})} |",
        f"| Provisional publication families | {len(families)} |",
        f"| Families containing multiple source rows | {duplicate_families} |",
        f"| Families touched by a manual merge decision | {manual_families} |",
        f"| Identity or metadata corrections applied in this layer | {corrected_records} |",
        "",
        "## Source Categories",
        "",
        "| Category | Source rows |",
        "|---|---:|",
    ]
    lines.extend(f"| {category} | {count} |" for category, count in sorted(category_counts.items()))
    lines.extend(["", "## Excluded Non-Publication Placeholders", ""])
    for record in excluded_records:
        lines.append(f"- `{record['record_id']}`: {record['title']}")
    lines.extend(["", "## Logged Corrections", ""])
    for record_id, decision in decisions["overrides"].items():
        sources = ", ".join(f"[{url}]({url})" for url in decision["source_urls"])
        lines.append(f"- `{record_id}`: {decision['reason']} Sources: {sources}")
    lines.extend(["", "## Manual Merge Decisions", ""])
    for decision in decisions["merges"]:
        records_text = ", ".join(f"`{record_id}`" for record_id in decision["records"])
        lines.append(f"- {records_text}: {decision['reason']}")
    lines.extend(["", "## Explicit Non-Merges", ""])
    for decision in decisions["non_merges"]:
        records_text = ", ".join(f"`{record_id}`" for record_id in decision["records"])
        lines.append(f"- {records_text}: {decision['reason']}")
    lines.extend(
        [
            "",
            "## Assurance Boundary",
            "",
            "This artifact supports record-level navigation and bounded manuscript claims. It does not establish comprehensive recall, independent dual screening, or a final PRISMA count. Singleton families without canonical identifiers remain candidates rather than verified unique publications.",
            "",
            "Rebuild with `python literature/build_publication_families.py`; verify freshness with `python literature/build_publication_families.py --check`.",
        ]
    )
    return "\n".join(lines) + "\n"


def build(root: Path) -> tuple[str, str]:
    with (root / "catalog.csv").open(encoding="utf-8-sig", newline="") as handle:
        source_records = list(csv.DictReader(handle))
    decisions = json.loads((root / "publication_family_decisions.json").read_text(encoding="utf-8"))
    by_record_id = {record["record_id"]: record for record in source_records}
    assert len(by_record_id) == len(source_records)

    for record_id, decision in decisions["overrides"].items():
        if record_id not in by_record_id:
            raise ValueError(f"Unknown override record: {record_id}")
        for field, value in decision["fields"].items():
            if field not in by_record_id[record_id]:
                raise ValueError(f"Unknown field {field!r} for {record_id}")
            by_record_id[record_id][field] = value or ""

    excluded_records = [record for record in source_records if "待补文献" in record["publication_status"]]
    records = [record for record in source_records if record not in excluded_records]
    reviewed_titles = decisions["canonical_arxiv_titles"]

    titles_by_arxiv: dict[str, set[str]] = defaultdict(set)
    arxiv_ids_by_title: dict[str, set[str]] = defaultdict(set)
    for record in records:
        title = normalize_title(record["title"])
        if match := ARXIV_RE.search(record["url"]):
            arxiv_id = match.group(1)
            titles_by_arxiv[arxiv_id].add(title)
            arxiv_ids_by_title[title].add(arxiv_id)
    unreviewed_conflicts = sorted(arxiv_id for arxiv_id, titles in titles_by_arxiv.items() if len(titles) > 1 and arxiv_id not in reviewed_titles)
    if unreviewed_conflicts:
        raise ValueError("Unreviewed arXiv title conflicts: " + ", ".join(unreviewed_conflicts))
    conflicting_ids = {title: ids for title, ids in arxiv_ids_by_title.items() if len(ids) > 1}
    if conflicting_ids:
        raise ValueError(f"Exact titles mapped to multiple arXiv IDs: {conflicting_ids}")

    union_find = UnionFind(len(records))
    index_by_record_id = {record["record_id"]: index for index, record in enumerate(records)}
    evidence_by_pair: dict[frozenset[int], str] = {}

    def merge_on(key_name: str, key_function) -> None:
        seen: dict[str, int] = {}
        for index, record in enumerate(records):
            key = key_function(record)
            if not key:
                continue
            if key in seen:
                evidence_by_pair[frozenset((index, seen[key]))] = key_name
                union_find.union(index, seen[key])
            else:
                seen[key] = index

    merge_on("normalized_title", lambda record: normalize_title(record["title"]))
    merge_on("arxiv_id", lambda record: (match.group(1) if (match := ARXIV_RE.search(record["url"])) else ""))

    for decision in decisions["merges"]:
        indexes = [index_by_record_id[record_id] for record_id in decision["records"]]
        for left, right in zip(indexes, indexes[1:]):
            pair = frozenset((left, right))
            evidence_by_pair[pair] = "manual_merge"
            union_find.union(left, right)

    groups: dict[int, list[dict[str, str]]] = defaultdict(list)
    for index, record in enumerate(records):
        groups[union_find.find(index)].append(record)

    override_ids = set(decisions["overrides"])
    families = []
    for members in groups.values():
        members.sort(key=lambda record: record["record_id"])
        record_ids = {member["record_id"] for member in members}
        arxiv_ids = sorted({match.group(1) for member in members if (match := ARXIV_RE.search(member["url"]))})
        reviewed = [reviewed_titles[arxiv_id] for arxiv_id in arxiv_ids if arxiv_id in reviewed_titles]
        canonical_title = reviewed[0] if len(set(reviewed)) == 1 else max((member["title"] for member in members), key=len)
        canonical_url = choose_url(members)
        canonical_record = next((member for member in members if member["url"] == canonical_url), members[0])
        doi_match = DOI_RE.search(canonical_url)
        bases = set()
        if len(members) == 1:
            bases.add("singleton")
        else:
            member_indexes = {index_by_record_id[record_id] for record_id in record_ids}
            for pair, basis in evidence_by_pair.items():
                if pair <= member_indexes:
                    bases.add(basis)
        statuses = []
        if record_ids & override_ids:
            statuses.append("metadata_corrected")
        if "manual_merge" in bases or reviewed:
            statuses.append("manual_identity_review")
        elif len(members) > 1:
            statuses.append("deterministic_identity")
        else:
            statuses.append("candidate_singleton")
        families.append(
            {
                "family_id": "PF-" + members[0]["record_id"],
                "canonical_title": canonical_title,
                "year": canonical_record["year"],
                "venue": canonical_record["venue"],
                "publication_status": canonical_record["publication_status"],
                "canonical_url": canonical_url,
                "arxiv_ids": " | ".join(arxiv_ids),
                "doi": doi_match.group(1).rstrip(".,") if doi_match else "",
                "record_ids": " | ".join(member["record_id"] for member in members),
                "categories": " | ".join(sorted({member["category"] for member in members})),
                "member_count": str(len(members)),
                "resolution_basis": " + ".join(sorted(bases)),
                "review_status": " + ".join(statuses),
            }
        )
    families.sort(key=lambda family: normalize_title(family["canonical_title"]))

    assert sum(int(family["member_count"]) for family in families) == len(records)
    assert len({record_id for family in families for record_id in family["record_ids"].split(" | ")}) == len(records)
    return render_csv(families), render_report(source_records, records, excluded_records, families, decisions)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    csv_text, report_text = build(root)
    outputs = {
        root / "publication_families.csv": csv_text,
        root / "PUBLICATION_FAMILIES.md": report_text,
    }
    if args.check:
        stale = [path.name for path, content in outputs.items() if not path.exists() or path.read_text(encoding="utf-8") != content]
        if stale:
            raise SystemExit("Stale publication-family outputs: " + ", ".join(stale))
        print("Publication-family outputs are current.")
        return
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")
    print(f"Wrote {len(csv_text.splitlines()) - 1} provisional publication families.")


if __name__ == "__main__":
    main()
