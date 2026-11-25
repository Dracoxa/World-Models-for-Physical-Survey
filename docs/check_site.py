"""Validate static site pages, anchors, local assets, 7 figures, and JSON counts."""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.urls: list[str] = []
        self.data_figs: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        if "id" in attr_map and attr_map["id"]:
            self.ids.add(attr_map["id"])
        for key in ("src", "href", "data-fig-src", "data-fig-webp", "data-fig-pdf"):
            if key in attr_map and attr_map[key]:
                val = attr_map[key]
                self.urls.append(val)
                if key.startswith("data-fig-"):
                    self.data_figs.add(val)
        if tag == "source" and "srcset" in attr_map and attr_map["srcset"]:
            self.urls.extend(item.strip().split()[0] for item in attr_map["srcset"].split(","))


def check_html(root: Path, page_name: str, all_pages: dict[str, SiteParser]) -> None:
    parser = all_pages[page_name]
    for url in parser.urls:
        if url.startswith("#"):
            assert url[1:] in parser.ids, f"{page_name}: missing anchor target {url}"
        elif url.startswith("assets/"):
            target = root / url.split("#")[0]
            assert target.is_file(), f"{page_name}: missing local asset {target}"
        elif url.startswith(("index.html", "explorer.html")):
            target_page, _, rest = url.partition("#")
            target_page = target_page.split("?")[0]
            assert (root / target_page).is_file(), f"{page_name}: missing target page {target_page}"
            if rest:
                assert rest in all_pages[target_page].ids, f"{page_name}: missing cross-page anchor {url}"


def main() -> None:
    root = Path(__file__).resolve().parent
    pages = {}
    for page_name in ("index.html", "explorer.html"):
        p = SiteParser()
        p.feed((root / page_name).read_text(encoding="utf-8"))
        pages[page_name] = p

    for page_name in pages:
        check_html(root, page_name, pages)

    index_figs = pages["index.html"].data_figs
    for i in range(1, 8):
        for ext in ("pdf", "png", "webp"):
            rel = f"assets/figure-0{i}.{ext}"
            assert rel in index_figs, f"index.html: missing figure switcher reference {rel}"
            assert (root / rel).is_file(), f"Missing figure asset on disk: {rel}"

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
        "Passed: index.html + explorer.html anchors/links, 7 figures (PDF/PNG/WebP), "
        "75/93 evidence JSON, and 33/66 benchmark JSON verified."
    )


if __name__ == "__main__":
    main()
