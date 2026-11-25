"""Validate static site links, asset integrity, figure counts, and JSON evidence consistency."""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.urls: list[str] = []
        self.images: int = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        if "id" in attr_map and attr_map["id"]:
            self.ids.add(attr_map["id"])
        if "src" in attr_map and attr_map["src"]:
            self.urls.append(attr_map["src"])
        if tag == "source" and "srcset" in attr_map and attr_map["srcset"]:
            self.urls.extend(item.strip().split()[0] for item in attr_map["srcset"].split(","))
        if tag in ("a", "link") and "href" in attr_map and attr_map["href"]:
            self.urls.append(attr_map["href"])
        if tag == "img":
            self.images += 1


def main() -> None:
    root = Path(__file__).resolve().parent
    parser = SiteParser()
    parser.feed((root / "index.html").read_text(encoding="utf-8"))

    for url in parser.urls:
        if url.startswith("#"):
            assert url[1:] in parser.ids, f"Missing anchor target: {url}"
        elif url.startswith("assets/"):
            target = root / url.split("#")[0]
            assert target.is_file(), f"Missing local asset: {target}"

    assert parser.images >= 7, f"Expected >= 7 <img> elements, got {parser.images}"
    for i in range(1, 8):
        for ext in ("pdf", "png", "webp"):
            fpath = root / "assets" / f"figure-0{i}.{ext}"
            assert fpath.is_file(), f"Missing figure asset: {fpath}"

    for doc in ("survey.pdf", "survey-review.pdf", "Evidence-companion.zip"):
        assert (root / "assets" / doc).is_file(), f"Missing deliverable asset: {doc}"

    evidence = json.loads((root / "assets" / "data" / "evidence.json").read_text(encoding="utf-8"))
    benchmarks = json.loads((root / "assets" / "data" / "benchmarks.json").read_text(encoding="utf-8"))

    assert evidence["meta"]["core_papers"] == 75
    assert evidence["meta"]["comparisons"] == 93
    assert len(evidence["comparisons"]) == 93
    assert len({c["key"] for c in evidence["comparisons"]}) == 75
    assert benchmarks["robotwin"]["total_configs"] == 33
    assert len(benchmarks["robotwin"]["profiles"]) == 33
    assert benchmarks["robodojo"]["total_configs"] == 66
    assert len(benchmarks["robodojo"]["profiles"]) == 66
    assert benchmarks["robodojo"]["zero_sr_pos_score_cells"] == 858
    assert not (root / ".openai").exists()

    print(
        "Passed: 7 figures (PDF/PNG/WebP), local assets, anchors, "
        "75/93 evidence JSON, and 33/66 benchmark JSON verified."
    )


if __name__ == "__main__":
    main()
