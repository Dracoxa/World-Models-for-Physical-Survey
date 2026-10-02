#!/usr/bin/env python3
"""Compare paper lists in external survey READMEs with the local catalog."""

from __future__ import annotations

import argparse
import csv
import re
import tempfile
import unicodedata
from collections import defaultdict
from difflib import get_close_matches
from pathlib import Path


ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})", re.I)
MARKDOWN_LINK_RE = re.compile(r"\[([^]]+)\]\(([^)]+)\)")
PRIORITY_TERMS = {
    "benchmark",
    "evaluation",
    "safety",
    "uncertainty",
    "calibration",
    "contact",
    "tactile",
    "force",
    "3d",
    "4d",
    "geometry",
    "cross embodiment",
    "navigation",
    "planning",
    "closed loop",
}


def normalize_title(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).lower()
    value = re.sub(r"<[^>]+>|\[[^]]*\]|[*_`$]", " ", value)
    value = value.replace("&", " and ")
    return " ".join(re.findall(r"[a-z0-9]+", value))


def clean_title(block: str, arxiv_id: str) -> str:
    first = block.splitlines()[0].strip()
    patterns = (
        r'^-\s+\*\*[^*]+\*\*:\s+"([^"]+)"',
        r"—\s+\*([^*]+)\*",
        r"^-\s+(?::[^:]+:\s+)?\*\*[^*]+\*\*:\s+(.+?)(?:\s{2,}|$)",
        r"^-\s+(?::[^:]+:\s+)?\*\*([^*]+)\*\*\.",
    )
    for pattern in patterns:
        match = re.search(pattern, first)
        if match:
            return match.group(1).strip().rstrip(".")
    return f"Untitled external record {arxiv_id}"


def title_from_line(line: str, arxiv_id: str) -> str:
    generic_labels = {"arxiv", "paper", "pdf", "paper link", "project"}
    for label, url in MARKDOWN_LINK_RE.findall(line):
        if arxiv_id in url and normalize_title(label) not in generic_labels:
            return re.sub(r"^[^A-Za-z0-9]+", "", label).strip()

    if "|" in line:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        for index, cell in enumerate(cells):
            if arxiv_id not in cell:
                continue
            for candidate in reversed(cells[:index]):
                candidate = MARKDOWN_LINK_RE.sub(r"\1", candidate)
                candidate = re.sub(r"[*_]", "", candidate).replace(chr(96), "").strip()
                if candidate and not re.fullmatch(r"\d{4}(?:-\d{1,2})?", candidate):
                    return candidate
    return ""


def extract_records(path: Path, source: str) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    records = []
    seen = set()
    for line in text.splitlines():
        for match in ARXIV_RE.finditer(line):
            arxiv_id = match.group(1)
            if arxiv_id in seen:
                continue
            title = title_from_line(line, arxiv_id)
            if not title:
                continue
            seen.add(arxiv_id)
            records.append(
                {
                    "source": source,
                    "arxiv_id": arxiv_id,
                    "title": title,
                    "normalized_title": normalize_title(title),
                    "year": str(2000 + int(arxiv_id[:2])),
                    "url": f"https://arxiv.org/abs/{arxiv_id}",
                }
            )

    blocks = re.split(r"(?m)(?=^-\s+)", text)
    for block in blocks:
        match = ARXIV_RE.search(block)
        if not match:
            continue
        arxiv_id = match.group(1)
        if arxiv_id in seen:
            continue
        seen.add(arxiv_id)
        title = clean_title(block, arxiv_id)
        year = str(2000 + int(arxiv_id[:2]))
        records.append(
            {
                "source": source,
                "arxiv_id": arxiv_id,
                "title": title,
                "normalized_title": normalize_title(title),
                "year": year,
                "url": f"https://arxiv.org/abs/{arxiv_id}",
            }
        )
    return records


def load_catalog(path: Path) -> tuple[dict[str, list[dict]], dict[str, list[dict]]]:
    by_arxiv: dict[str, list[dict]] = defaultdict(list)
    by_title: dict[str, list[dict]] = defaultdict(list)
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            match = ARXIV_RE.search(row.get("url", ""))
            if match:
                by_arxiv[match.group(1)].append(row)
            by_title[normalize_title(row["title"])].append(row)
    return by_arxiv, by_title


def load_known(paths: list[Path]) -> tuple[set[str], set[str]]:
    known_ids = set()
    known_titles = set()
    for path in paths:
        text = path.read_text(encoding="utf-8")
        known_ids.update(ARXIV_RE.findall(text))
        known_ids.update(re.findall(r"\b([0-9]{4}\.[0-9]{4,5})\b", text))
        if path.suffix == ".csv":
            known_titles.update(
                normalize_title(row["title"])
                for row in csv.DictReader(text.splitlines())
                if row.get("title")
            )
        elif path.suffix == ".bib":
            known_titles.update(
                normalize_title(match.group(1))
                for match in re.finditer(r'(?mi)^\s*title\s*=\s*[{\"](.+)[}\"]\s*,?\s*$', text)
            )
        else:
            known_titles.update(
                normalize_title(label)
                for label, _ in MARKDOWN_LINK_RE.findall(text)
                if len(normalize_title(label).split()) >= 2
            )
    return known_ids, known_titles


def nearest_title(title: str, catalog_titles: list[str]) -> tuple[str, float]:
    if not title or title.startswith("untitled external record"):
        return "", 0.0
    matches = get_close_matches(title, catalog_titles, n=1, cutoff=0.94)
    return (matches[0], 0.94) if matches else ("", 0.0)


def priority(record: dict) -> tuple[str, str]:
    title = record["normalized_title"]
    padded = f" {title} "
    hits = sorted(term for term in PRIORITY_TERMS if f" {term} " in padded)
    recent = record["year"] == "2026"
    repeated = record["source_count"] >= 2
    if repeated and hits:
        signals = []
        signals.append("多源交叉")
        if recent:
            signals.append("2026 新作")
        return "最高", "、".join(signals) + "且命中薄弱方向：" + "、".join(hits)
    if repeated or (recent and hits):
        if repeated:
            return "高", "被多个近邻仓库收录"
        return "高", "2026 新作且命中薄弱方向：" + "、".join(hits)
    if recent or hits:
        return "中", "2026 新作" if recent else "命中薄弱方向：" + "、".join(hits)
    return "低", "单一来源，需先判断与综述范围的关系"


def compare(catalog: Path, known_paths: list[Path], sources: list[tuple[str, Path]]) -> tuple[list[dict], dict]:
    by_arxiv, by_title = load_catalog(catalog)
    known_ids, known_titles = load_known(known_paths)
    catalog_titles = list(by_title)
    merged: dict[str, dict] = {}
    source_stats = {}

    for source, path in sources:
        records = extract_records(path, source)
        source_stats[source] = {
            "extracted": len(records),
            "catalog": 0,
            "known": 0,
            "unresolved": 0,
            "candidates": 0,
        }
        for record in records:
            key = record["arxiv_id"]
            if key not in merged:
                merged[key] = {**record, "sources": set()}
            elif len(record["normalized_title"]) > len(merged[key]["normalized_title"]):
                merged[key].update({field: record[field] for field in ("title", "normalized_title", "year", "url")})
            merged[key]["sources"].add(source)

    candidates = []
    for record in merged.values():
        matches = by_arxiv.get(record["arxiv_id"], [])
        match_type = "arxiv_id" if matches else ""
        if not matches:
            matches = by_title.get(record["normalized_title"], [])
            match_type = "title" if matches else ""
        if not matches:
            nearest, ratio = nearest_title(record["normalized_title"], catalog_titles)
            if ratio >= 0.94:
                matches = by_title[nearest]
                match_type = f"near_title:{ratio:.3f}"

        known = record["arxiv_id"] in known_ids or record["normalized_title"] in known_titles
        unresolved = record["title"].startswith("Untitled external record")
        status = "catalog" if matches else "known" if known else "unresolved" if unresolved else "candidates"
        for source in record["sources"]:
            source_stats[source][status] += 1
        if matches:
            continue
        if known or unresolved:
            continue

        record["sources"] = sorted(record["sources"])
        record["source_count"] = len(record["sources"])
        record["priority"], record["priority_reason"] = priority(record)
        record["match_status"] = match_type or "not_found"
        candidates.append(record)

    order = {"最高": 0, "高": 1, "中": 2, "低": 3}
    candidates.sort(key=lambda row: (order[row["priority"]], -int(row["year"] or 0), row["title"]))
    stats = {
        "catalog_records": sum(len(rows) for rows in by_title.values()),
        "catalog_unique_titles": len(by_title),
        "external_unique_arxiv": len(merged),
        "candidate_count": len(candidates),
        "source_stats": source_stats,
    }
    return candidates, stats


def write_csv(path: Path, candidates: list[dict]) -> None:
    fields = ["priority", "year", "title", "arxiv_id", "url", "sources", "source_count", "priority_reason"]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in candidates:
            public_row = {field: row[field] for field in fields}
            public_row["sources"] = "; ".join(row["sources"])
            writer.writerow(public_row)


def write_markdown(path: Path, candidates: list[dict], stats: dict, source_meta: list[str]) -> None:
    lines = [
        "# 外部调研库去重后新增候选",
        "",
        "生成日期：2026-10-02。该文件由 `compare_external_surveys.py` 生成，是待核验候选，不代表已纳入正文。",
        "",
        "## 快照与口径",
        "",
        *[f"- {item}" for item in source_meta],
        f"- 本地基线：929 条分类记录，{stats['catalog_unique_titles']} 个规范化题名；跨类别重复保留。",
        "- 去重顺序：arXiv ID、规范化题名、相似度不低于 0.94 的近似题名。",
        "- GitHub 仓库条目只用于发现；候选数量不代表纳入数量、证据数量或已核验论文数量。",
        "",
        "## 去重结果",
        "",
        "| 来源 | 提取 arXiv 条目 | 已在目录 | 已在补充材料追踪 | 题名待解析 | 新增候选 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for source, row in stats["source_stats"].items():
        lines.append(
            f"| {source} | {row['extracted']} | {row['catalog']} | {row['known']} | "
            f"{row['unresolved']} | {row['candidates']} |"
        )
    lines.extend(
        [
            "",
            f"{len(stats['source_stats'])} 个来源合并后得到 {stats['external_unique_arxiv']} 个唯一 arXiv ID，其中 {stats['candidate_count']} 个未在本地目录或已跟踪材料中找到。完整清单见配套 CSV。",
            "",
            "## 优先核验候选",
            "",
            "展示“最高”优先级，以及被至少两个近邻仓库共同收录的“高”优先级条目。优先级是检索排序，不是质量评价或纳入决定。",
            "",
            "| 优先级 | 年份 | 论文 | 来源 | 排序原因 |",
            "|---|---:|---|---|---|",
        ]
    )
    shown = [
        row
        for row in candidates
        if row["priority"] == "最高" or (row["priority"] == "高" and row["source_count"] >= 2)
    ]
    for row in shown:
        title = row["title"].replace("|", "\\|")
        reason = row["priority_reason"].replace("|", "\\|")
        lines.append(
            f"| {row['priority']} | {row['year']} | [{title}]({row['url']}) | {', '.join(row['sources'])} | {reason} |"
        )
    lines.extend(
        [
            "",
            "## 人工验收要求",
            "",
            "每篇候选进入七类目录前，至少核对题名、作者、版本、发表状态、任务环境、动作是否进入预测、是否闭环使用，以及能够支撑正文的具体图表或章节。自动匹配不能替代全文核验。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def self_check() -> None:
    assert normalize_title("World-Action Models: A Survey") == "world action models a survey"
    sample = '- **Demo**: "A 3D World Model", arXiv 2026.\n  [[Paper](https://arxiv.org/pdf/2601.12345)]'
    assert clean_title(sample, "2601.12345") == "A 3D World Model"
    direct = "| 2026-01 | [A Robot World Model](https://arxiv.org/abs/2601.12345) | Video |"
    assert title_from_line(direct, "2601.12345") == "A Robot World Model"
    labeled = "| 2026-01 | A Robot World Model | [arXiv](https://arxiv.org/abs/2601.12345) |"
    assert title_from_line(labeled, "2601.12345") == "A Robot World Model"
    with tempfile.TemporaryDirectory() as directory:
        bib = Path(directory, "known.bib")
        bib.write_text("@article{x,\n  title={Cosmos Policy: Robot Control},\n}\n", encoding="utf-8")
        _, titles = load_known([bib])
        assert normalize_title("Cosmos Policy: Robot Control") in titles
    screening = {"normalized_title": "robot planning", "year": "2026", "source_count": 1}
    assert priority(screening)[0] == "高"
    screening["source_count"] = 2
    assert priority(screening)[0] == "最高"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--source", action="append", required=True, help="NAME=README_PATH")
    parser.add_argument("--known", action="append", type=Path, default=[])
    parser.add_argument("--source-meta", action="append", default=[])
    parser.add_argument("--output-csv", type=Path, required=True)
    parser.add_argument("--output-md", type=Path, required=True)
    args = parser.parse_args()
    sources = []
    for value in args.source:
        name, path = value.split("=", 1)
        sources.append((name, Path(path)))
    self_check()
    candidates, stats = compare(args.catalog, args.known, sources)
    write_csv(args.output_csv, candidates)
    write_markdown(args.output_md, candidates, stats, args.source_meta)
    print(f"Wrote {len(candidates)} candidates from {stats['external_unique_arxiv']} unique external arXiv IDs")


if __name__ == "__main__":
    main()
