"""Focused checks for safe and reproducible candidate-index publication."""

import csv
from pathlib import Path
import tempfile
import unittest

from export_current_catalog import CATEGORIES, FIELDS, candidate_url, export_snapshot, project_rows, render_category


class CurrentCatalogTests(unittest.TestCase):
    def source(self, **changes):
        row = dict(family_id="SUP-2601.12345", title="Paper [A] <tag>", year="2026",
                   categories=" | ".join(name for name, _ in CATEGORIES[:2]),
                   publication_url="https://arxiv.org/abs/2601.12345v3",
                   review_state="candidate_pending_review", evidence="/Users/private/secret", authors="Private note")
        row.update(changes)
        return row

    def test_whitelist_and_conflict_quarantine(self):
        row = project_rows([self.source()])[0]
        self.assertEqual(set(row), set(FIELDS))
        self.assertNotIn("private", str(row).lower())
        self.assertEqual(row["url"], self.source()["publication_url"])
        row = project_rows([self.source(review_state="identity_conflict")])[0]
        self.assertEqual(row["url"], "")
        self.assertEqual(row["link_status"], "held_identity_conflict")

    def test_url_safety_and_exact_version(self):
        url = "https://arxiv.org/abs/2601.12345v3"
        self.assertEqual(candidate_url(url), url)
        for bad in ("https://link.wtturl.cn/?target=https://pdf.sciencedirectassets.com/x",
                    "https://example.org/Paper‑Conference.pdf", "http://127.0.0.1/a",
                    "http://[::1]/a", "http://host.local/a", "https://alice:secret@example.org/a",
                    "https://example.org/?api_key=secret", "https://example.org/?%74oken=secret",
                    "file:///Users/private/a", "https://example.org/a extra"):
            with self.subTest(url=bad):
                self.assertEqual(candidate_url(bad), "")

    def test_invalid_metadata_rejected(self):
        for change in (dict(title="/Users/private/a"), dict(review_state="verified"),
                       dict(categories="Unknown"), dict(family_id="<script>")):
            with self.subTest(change=change), self.assertRaises(ValueError):
                project_rows([self.source(**change)])
        with self.assertRaises(ValueError):
            project_rows([self.source(), self.source()])

    def test_export_is_repeatable_and_source_is_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "master_table.csv"
            items = [self.source(title="=UnsafeFormula [A] <tag>"),
                     self.source(family_id="PF-MISSING", publication_url=""),
                     self.source(family_id="PF-BAD", publication_url="https://example.org/non‑ascii")]
            with source.open("w", encoding="utf-8", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=items[0].keys())
                writer.writeheader()
                writer.writerows(items)
            before = source.read_bytes()
            output = root / "current"
            rows = export_snapshot(source, output, "2026-10-10")
            files = {p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()}
            export_snapshot(source, output, "2026-10-10")
            self.assertEqual(files, {p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()})
            self.assertEqual(before, source.read_bytes())
            self.assertNotIn(b"\r\n", (output / "catalog.csv").read_bytes())
            with (output / "catalog.csv").open(encoding="utf-8-sig", newline="") as file:
                public = list(csv.DictReader(file))
            self.assertEqual(len(public), 3)
            self.assertTrue(public[0]["title"].startswith("'=UnsafeFormula"))
            page = (output / "categories" / f"{CATEGORIES[0][1]}.md").read_text(encoding="utf-8")
            self.assertNotIn("<tag>", page)
            self.assertIn("&#91;A&#93;", page)
            self.assertIn(rows[0]["url"], page)
            self.assertNotIn("[Paper](<>)", page)
            readme = (output / "README.md").read_text(encoding="utf-8")
            self.assertIn("**1 条提供公开检索链接**", readme)
            self.assertNotIn("/Users/", readme)

    def test_checked_in_views_match_public_csv(self):
        root = Path(__file__).resolve().parent / "current"
        with (root / "catalog.csv").open(encoding="utf-8-sig", newline="") as file:
            rows = list(csv.DictReader(file))
        self.assertEqual(len(rows), len({r["family_id"] for r in rows}))
        readme = (root / "README.md").read_text(encoding="utf-8")
        snapshot_date = readme.split("候选发现索引快照：**", 1)[1].split("**", 1)[0]
        for name, slug in CATEGORIES:
            selected = [r for r in rows if name in r["categories"].split(" | ")]
            self.assertEqual((root / "categories" / f"{slug}.md").read_text(encoding="utf-8"),
                             render_category(name, selected, snapshot_date))
        for row in rows:
            if row["url"]:
                self.assertEqual(candidate_url(row["url"]), row["url"])
                self.assertNotEqual(row["review_state"], "identity_conflict")


if __name__ == "__main__":
    unittest.main()
