#!/usr/bin/env python3
"""Synchronize r6 manuscript artifacts, figures, and deterministic JSON data for docs/."""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import subprocess
import zipfile
from collections import Counter
from pathlib import Path
from PIL import Image

USE_LABELS = {
    "representation": "Predictive representation",
    "train": "Policy training",
    "plan": "Planning & selection",
    "generate": "Action generation",
    "assess": "Assessment",
    "execute": "Execution & intervention",
}

USE_ORDER = [
    "train",
    "generate",
    "plan",
    "representation",
    "assess",
    "execute",
]

SYSTEM_ALIASES = {
    "assran2025vjepa2": "V-JEPA 2",
    "bai2026laravla": "LaRA-VLA",
    "bar2025nwm": "NWM",
    "chua2018pets": "PETS",
    "du2023unipi": "UniPi",
    "ebert2018visualforesight": "Visual Foresight",
    "guan2026jopat": "JOPAT",
    "hafner2019planet": "PlaNet",
    "hafner2020dreamer": "Dreamer",
    "hafner2025dreamerv3": "DreamerV3",
    "huang2026fomofd": "FoMo-FD",
    "huang2026scvc": "SCVC",
    "janner2019mbpo": "MBPO",
    "kipf2020cswm": "C-SWM",
    "li2026dream2fix": "Dream2Fix",
    "lingbot": "LingBot-VA",
    "liu2026physicallygroundedjepa": "Physically Grounded JEPA",
    "lu2026dawn": "DAWN",
    "patel2026pgrd": "PGRD",
    "pfaff2021meshgraphnets": "MeshGraphNets",
    "sanchez2020gns": "GNS",
    "thomas2021imagining": "SMBPO",
    "vpp2": "VPP2",
    "wang2024drivewm": "Drive-WM",
    "wang2026interactive": "IWS",
    "wang2026simtorealwam": "Sim-to-Real WAM",
    "xwam": "X-WAM",
    "yang2024unisim": "UniSim",
    "yang2025driveoccworld": "Drive-OccWorld",
    "ye2026dreamzero": "DreamZero",
    "yuan2026visualqualitystudytesttime": "Beyond Visual Quality",
    "zhao2026geometricverification": "GeoBoN",
    "zhen2025tesseract": "TesserAct",
}

# Exact r6 paper figure numbering -> docs/assets/figure-01..07
FIGURE_MAP = [
    ("figure-01", "fig01_survey_organization.pdf"),
    ("figure-02", "fig02_predictive_uses_timeline.pdf"),
    ("figure-03", "fig03_data_models_overview.pdf"),
    ("figure-04", "fig04_prediction_action_generation.pdf"),
    ("figure-05", "fig06_evaluator_training_preferences.pdf"),
    ("figure-06", "fig07_editable_action_windows.pdf"),
    ("figure-07", "fig05_design_evidence_contrasts.pdf"),
]

# Published capability breakdown for RoboDojo (r6 Table 8, snapshot Nov 3 / Nov 10 2026)
ROBODOJO_CAPABILITY_ROWS = [
    {
        "method": "WALL-OSS-1.0-lite",
        "overall_score": 42.59,
        "avg_sr": 34.97,
        "memory_sr": 56.00,
        "precision_sr": 29.08,
        "long_sr": 32.25,
        "gen_sr": 37.94,
        "open_sr": 19.58,
    },
    {
        "method": "VPP2",
        "overall_score": 39.26,
        "avg_sr": 32.26,
        "memory_sr": 55.56,
        "precision_sr": 35.17,
        "long_sr": 37.00,
        "gen_sr": 29.50,
        "open_sr": 4.08,
    },
    {
        "method": "OpenWAM-α",
        "overall_score": 17.18,
        "avg_sr": 11.92,
        "memory_sr": 9.11,
        "precision_sr": 9.25,
        "long_sr": 25.33,
        "gen_sr": 14.83,
        "open_sr": 1.08,
    },
    {
        "method": "Spatial Forcing",
        "overall_score": 12.38,
        "avg_sr": 8.04,
        "memory_sr": 4.11,
        "precision_sr": 10.58,
        "long_sr": 14.58,
        "gen_sr": 9.34,
        "open_sr": 1.58,
    },
    {
        "method": "π₀.₅",
        "overall_score": 11.44,
        "avg_sr": 6.93,
        "memory_sr": 4.67,
        "precision_sr": 5.50,
        "long_sr": 14.67,
        "gen_sr": 8.17,
        "open_sr": 1.67,
    },
    {
        "method": "X-WAM",
        "overall_score": 7.69,
        "avg_sr": 3.83,
        "memory_sr": 4.67,
        "precision_sr": 1.83,
        "long_sr": 9.08,
        "gen_sr": 3.33,
        "open_sr": 0.25,
    },
    {
        "method": "AHA-WAM",
        "overall_score": 4.82,
        "avg_sr": 2.39,
        "memory_sr": 2.78,
        "precision_sr": 2.42,
        "long_sr": 2.67,
        "gen_sr": 3.27,
        "open_sr": 0.83,
    },
    {
        "method": "Fast-WAM",
        "overall_score": 3.48,
        "avg_sr": 2.03,
        "memory_sr": 3.44,
        "precision_sr": 0.00,
        "long_sr": 5.17,
        "gen_sr": 1.11,
        "open_sr": 0.42,
    },
]


def clean_latex(text: str) -> str:
    """Convert common BibTeX/LaTeX markup into clean plain Unicode text."""
    s = text.strip()
    replacements = [
        (r"\&", "&"),
        (r"\%", "%"),
        (r"\_", "_"),
        (r"---", "—"),
        (r"--", "–"),
        ("~", " "),
        (r"\'{a}", "á"), (r"\'a", "á"),
        (r"\'{e}", "é"), (r"\'e", "é"),
        (r"\'{i}", "í"), (r"\'i", "í"), (r"\'{\i}", "í"),
        (r"\'{o}", "ó"), (r"\'o", "ó"),
        (r"\'{u}", "ú"), (r"\'u", "ú"),
        (r'\"{a}', "ä"), (r'\"a', "ä"),
        (r'\"{o}', "ö"), (r'\"o', "ö"),
        (r'\"{u}', "ü"), (r'\"u', "ü"),
        (r"\v{c}", "č"), (r"\v{s}", "š"), (r"\v{z}", "ž"),
        (r"\c{c}", "ç"),
        (r"\o", "ø"),
    ]
    for old, new in replacements:
        s = s.replace(old, new)
    s = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", s)
    s = s.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", s).strip()


def parse_bibtex(bib_path: Path) -> dict[str, dict[str, str]]:
    """Parse balanced-brace BibTeX entries into a dictionary keyed by citation key."""
    text = bib_path.read_text(encoding="utf-8")
    entries: dict[str, dict[str, str]] = {}
    i = 0
    n = len(text)
    while i < n:
        at = text.find("@", i)
        if at == -1:
            break
        brace = text.find("{", at)
        if brace == -1:
            break
        entry_type = text[at + 1 : brace].strip().lower()
        if entry_type == "comment" or entry_type == "string":
            i = brace + 1
            continue
        # Scan balanced braces for whole entry
        depth = 1
        j = brace + 1
        while j < n and depth > 0:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
            j += 1
        body = text[brace + 1 : j - 1]
        i = j
        comma = body.find(",")
        if comma == -1:
            continue
        key = body[:comma].strip()
        rest = body[comma + 1 :]
        fields: dict[str, str] = {"_type": entry_type}
        k = 0
        m = len(rest)
        while k < m:
            while k < m and rest[k] in " \t\r\n,":
                k += 1
            if k >= m:
                break
            eq = rest.find("=", k)
            if eq == -1:
                break
            fname = rest[k:eq].strip().lower()
            k = eq + 1
            while k < m and rest[k] in " \t\r\n":
                k += 1
            if k >= m:
                break
            if rest[k] == "{":
                fdepth = 1
                k += 1
                start = k
                while k < m and fdepth > 0:
                    if rest[k] == "{":
                        fdepth += 1
                    elif rest[k] == "}":
                        fdepth -= 1
                    k += 1
                fval = rest[start : k - 1]
            elif rest[k] == '"':
                k += 1
                start = k
                while k < m and not (rest[k] == '"' and rest[k - 1] != "\\"):
                    k += 1
                fval = rest[start:k]
                k += 1
            else:
                start = k
                while k < m and rest[k] not in ",\r\n":
                    k += 1
                fval = rest[start:k]
            fields[fname] = clean_latex(fval)
        entries[key] = fields
    return entries


def short_authors(author_str: str) -> str:
    if not author_str:
        return ""
    authors = [a.strip() for a in re.split(r"\s+and\s+", author_str) if a.strip()]
    if not authors:
        return ""

    def surname(a: str) -> str:
        if "," in a:
            return a.split(",")[0].strip()
        parts = a.split()
        return parts[-1] if parts else a

    if len(authors) == 1:
        return surname(authors[0])
    if len(authors) == 2:
        return f"{surname(authors[0])} & {surname(authors[1])}"
    return f"{surname(authors[0])} et al."


def sync_assets(r6_dir: Path, assets_dir: Path) -> dict[str, dict[str, int]]:
    assets_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(r6_dir / "Journal-preview.pdf", assets_dir / "survey.pdf")
    shutil.copy2(r6_dir / "Review.pdf", assets_dir / "survey-review.pdf")
    shutil.copy2(r6_dir / "Evidence-companion.zip", assets_dir / "Evidence-companion.zip")

    dims: dict[str, dict[str, int]] = {}
    figs_src = r6_dir / "paper" / "figures"
    for target_stem, src_name in FIGURE_MAP:
        src_pdf = figs_src / src_name
        dst_pdf = assets_dir / f"{target_stem}.pdf"
        dst_png = assets_dir / f"{target_stem}.png"
        dst_webp = assets_dir / f"{target_stem}.webp"
        shutil.copy2(src_pdf, dst_pdf)
        subprocess.run(
            ["pdftoppm", "-png", "-r", "220", "-singlefile", str(dst_pdf), str(assets_dir / target_stem)],
            check=True,
        )
        with Image.open(dst_png) as im:
            dims[target_stem] = {"width": im.width, "height": im.height}
            im.save(dst_webp, format="WEBP", quality=88, method=6)
    return dims


def build_evidence_json(r6_dir: Path) -> dict:
    bib = parse_bibtex(r6_dir / "paper" / "references.bib")
    analysis_dir = r6_dir / "analysis"

    papers_rows = list(csv.DictReader((analysis_dir / "papers.csv").open(encoding="utf-8")))
    comps_rows = list(csv.DictReader((analysis_dir / "comparisons.csv").open(encoding="utf-8")))
    coding_rows = list(csv.DictReader((analysis_dir / "coding_decisions.csv").open(encoding="utf-8")))
    summary_rows = list(csv.DictReader((analysis_dir / "summary.csv").open(encoding="utf-8")))
    illus_rows = list(csv.DictReader((analysis_dir / "illustrations.csv").open(encoding="utf-8")))

    coding_by_rec = {
        int(r["comparison_record"]): r
        for r in coding_rows
        if r["comparison_record"].strip().isdigit()
    }
    illus_by_use = {r["use"]: r for r in illus_rows}

    comparisons = []
    omitted_keys_per_use: Counter[str] = Counter()
    component_directions: Counter[str] = Counter()

    for idx, row in enumerate(comps_rows, start=1):
        key = row["key"]
        bib_info = bib.get(key, {})
        dec = coding_by_rec.get(idx, {})
        granularity = dec.get("granularity", "")
        bundled_omitted = "bundle omitted" in granularity.lower()
        is_specific = row["specific"] == "yes"
        is_downstream = row["downstream"] == "yes"
        if is_specific:
            component_directions[row["direction"]] += 1
        if bundled_omitted:
            omitted_keys_per_use[row["use"]] += 1

        comparisons.append(
            {
                "id": idx,
                "key": key,
                "alias": SYSTEM_ALIASES.get(key, ""),
                "title": bib_info.get("title", key),
                "authors": short_authors(bib_info.get("author", "")),
                "year": bib_info.get("year", ""),
                "venue": bib_info.get("booktitle") or bib_info.get("journal") or ("arXiv" if bib_info.get("eprint") else ""),
                "use": row["use"],
                "use_label": USE_LABELS[row["use"]],
                "endpoint": row["endpoint"],
                "comparison": row["comparison"],
                "other_changes": row["other_changes"],
                "downstream": is_downstream,
                "specific": is_specific,
                "bundled_omitted": bundled_omitted,
                "direction": row["direction"],
                "result": row["result"],
                "locator": row["locator"],
                "url": row["url"],
                "granularity": granularity,
                "rationale": dec.get("rationale", ""),
            }
        )

    # Verify Table 9 exact counts per use
    summary_map = {r["use"]: r for r in summary_rows}
    # Sensitivity papers remaining per use: Action generation 4->2, Execution 6(2)->1, Any use 29->26
    sensitivity_map = {
        "Predictive representation": 0,
        "Policy training": 14,
        "Planning and selection": 9,
        "Action generation": 2,
        "Assessment": 0,
        "Execution and intervention": 1,
        "Any use": 26,
    }
    illus_dim_map = {
        "Predictive representation": "L2",
        "Policy training": "L5",
        "Planning and selection": "L5",
        "Action generation": "L5",
        "Assessment": "Eval. (L5)",
        "Execution and intervention": "L5",
    }

    summary_by_use = []
    for use_key in USE_ORDER:
        label = USE_LABELS[use_key] if use_key != "generate" else "Action generation"
        # match CSV string exactly
        csv_name = {
            "representation": "Predictive representation",
            "train": "Policy training",
            "plan": "Planning and selection",
            "generate": "Action generation",
            "assess": "Assessment",
            "execute": "Execution and intervention",
        }[use_key]
        sr = summary_map[csv_name]
        il = illus_by_use[csv_name]
        summary_by_use.append(
            {
                "use_key": use_key,
                "label": csv_name,
                "core_papers": int(sr["screened"]),
                "execution_papers": int(sr["downstream"]),
                "component_papers": int(sr["specific"]),
                "sensitivity_papers": sensitivity_map[csv_name],
                "illus_dim": illus_dim_map[csv_name],
                "illus_study": il["study"],
                "illus_result": il["reported_result"],
                "illus_key": il["citation_key"],
            }
        )

    any_sr = summary_map["Any use"]
    assert len(papers_rows) == 75
    assert len(comparisons) == 93
    assert int(any_sr["screened"]) == 75
    assert int(any_sr["downstream"]) == 56
    assert int(any_sr["specific"]) == 29

    return {
        "meta": {
            "core_papers": len(papers_rows),
            "comparisons": len(comparisons),
            "execution_papers": int(any_sr["downstream"]),
            "component_papers": int(any_sr["specific"]),
            "sensitivity_papers": 26,
            "component_records": sum(1 for c in comparisons if c["specific"]),
            "bundled_records_omitted": sum(1 for c in comparisons if c["bundled_omitted"]),
            "component_directions": dict(component_directions),
            "evidence_map_date": "2026-11-22",
        },
        "summary_by_use": summary_by_use,
        "comparisons": comparisons,
    }


def build_benchmarks_json(r6_dir: Path) -> dict:
    zpath = r6_dir / "analysis" / "benchmark_tasks.zip"
    with zipfile.ZipFile(zpath) as zf:
        rt_rows = list(csv.DictReader(zf.open("benchmark_tasks/derived/robotwin_profiles.csv").read().decode("utf-8").splitlines()))
        rd_rows = list(csv.DictReader(zf.open("benchmark_tasks/derived/robodojo_profiles.csv").read().decode("utf-8").splitlines()))
        rd_cells = list(csv.DictReader(zf.open("benchmark_tasks/derived/robodojo_cells.csv").read().decode("utf-8").splitlines()))
        summary_json = json.loads(zf.open("benchmark_tasks/derived/summary.json").read().decode("utf-8"))

    rt_profiles = []
    for r in rt_rows:
        rt_profiles.append(
            {
                "record_id": r["record_id"],
                "model": r["model"],
                "setting": r["setting"],
                "mean_gap_pp": float(r["mean_gap_pp"]),
                "median_gap_pp": float(r["median_gap_pp"]),
                "decline_tasks": int(r["decline_tasks"]),
                "tie_tasks": int(r["tie_tasks"]),
                "increase_tasks": int(r["increase_tasks"]),
            }
        )

    rd_profiles = []
    for r in rd_rows:
        rd_profiles.append(
            {
                "policy_key": r["policy_key"],
                "observed": int(r["observed"]),
                "missing": int(r["missing"]),
                "pos_score_zero_sr": int(r["positive_score_zero_success"]),
                "zero_score_zero_sr": int(r["zero_score_zero_success"]),
                "pos_sr": int(r["positive_success"]),
            }
        )
    rd_profiles.sort(key=lambda x: (-x["pos_score_zero_sr"], x["policy_key"]))

    pos_zero_counts = sorted(p["pos_score_zero_sr"] for p in rd_profiles)
    visible_cells = sum(p["observed"] for p in rd_profiles)
    missing_cells = sum(p["missing"] for p in rd_profiles)
    pos_score_zero_sr_total = sum(p["pos_score_zero_sr"] for p in rd_profiles)

    assert len(rt_profiles) == 33
    assert len(rd_profiles) == 66
    assert visible_cells == 3536
    assert missing_cells == 28
    assert pos_score_zero_sr_total == 858
    assert len(rd_cells) == 3564

    return {
        "snapshot_date": "2026-11-10",
        "robotwin": {
            "total_configs": 33,
            "cotrain_configs": sum(1 for p in rt_profiles if p["setting"] == "cotrain"),
            "single_task_configs": sum(1 for p in rt_profiles if p["setting"] != "cotrain"),
            "total_mean_drop": sum(1 for p in rt_profiles if p["mean_gap_pp"] > 0),
            "cotrain_mean_drop": sum(1 for p in rt_profiles if p["setting"] == "cotrain" and p["mean_gap_pp"] > 0),
            "total_all50_drop": sum(1 for p in rt_profiles if p["decline_tasks"] == 50),
            "cotrain_all50_drop": sum(1 for p in rt_profiles if p["setting"] == "cotrain" and p["decline_tasks"] == 50),
            "task_pairs": 1650,
            "profiles": rt_profiles,
        },
        "robodojo": {
            "total_configs": 66,
            "visible_cells": visible_cells,
            "missing_cells": missing_cells,
            "zero_sr_pos_score_cells": pos_score_zero_sr_total,
            "pct": round(100.0 * pos_score_zero_sr_total / visible_cells, 1),
            "median_per_config": int((pos_zero_counts[32] + pos_zero_counts[33]) / 2),
            "min_per_config": pos_zero_counts[0],
            "max_per_config": pos_zero_counts[-1],
            "profiles": rd_profiles,
            "capability_comparison": ROBODOJO_CAPABILITY_ROWS,
            "organize_table_case": {
                "policy": "VPP2",
                "task": "organize_table",
                "score": 63.17,
                "sr_percent": 7.33,
            },
            "source_summary_keys": sorted(summary_json.keys()),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--r6",
        type=Path,
        default=Path(__file__).resolve().parents[2] / "outputs" / "WM_Style_Revision_20261124_r6",
    )
    args = parser.parse_args()

    docs_dir = Path(__file__).resolve().parent
    assets_dir = docs_dir / "assets"
    data_dir = assets_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    dims = sync_assets(args.r6, assets_dir)
    evidence = build_evidence_json(args.r6)
    benchmarks = build_benchmarks_json(args.r6)
    evidence["figure_dims"] = dims

    (data_dir / "evidence.json").write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (data_dir / "benchmarks.json").write_text(
        json.dumps(benchmarks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"Synced 7 figures + 2 PDFs + companion ZIP; built evidence.json "
        f"({evidence['meta']['core_papers']} papers / {evidence['meta']['comparisons']} comparisons) "
        f"and benchmarks.json ({benchmarks['robotwin']['total_configs']} RT / "
        f"{benchmarks['robodojo']['total_configs']} RD)."
    )


if __name__ == "__main__":
    main()
