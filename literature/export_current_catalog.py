"""Publish metadata-only candidate views without changing the frozen catalog."""

import argparse
from collections import Counter
import csv
from datetime import date
import hashlib
import ipaddress
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit, urlunsplit

from export_catalog import CATEGORIES, markdown, public_url


FIELDS = ["family_id", "title", "year", "categories", "url", "review_state", "link_status"]
STATES = {
    "candidate_pending_review": "待审候选",
    "identity_checked_metadata_only": "仅元数据身份核对",
    "selected_units_extracted_ai": "AI 提取指定内容，待人工复核",
    "selected_units_primary_asserted_human_pending": "指定原文单元提取，待人工复核",
    "selected_method_protocol_limit_units_primary_asserted_human_pending": "指定方法／协议／局限提取，待人工复核",
    "identity_conflict": "身份冲突，暂缓使用",
}


def candidate_url(value):
    parts = urlsplit(value)
    decoded = unquote(value).lower()
    if (not re.fullmatch(r"https?://[^\s<>]+", value)
            or not value.isascii() or not public_url(value)
            or any(word in decoded for word in (
                "target=", "redirect=", "token", "credential", "signature",
                "secret", "password", "api_key", "access_key", "auth="))
            or (parts.hostname or "").endswith((".local", ".internal"))):
        return ""
    try:
        if ipaddress.ip_address(parts.hostname).is_private:
            return ""
    except ValueError:
        pass
    # Discovery links retain source versions; they are not evidence-version approvals.
    return urlunsplit((parts.scheme, parts.netloc, parts.path, parts.query, ""))


def project_rows(source):
    rows, seen = [], set()
    names = {name for name, _ in CATEGORIES}
    for item in source:
        row = {key: item[key].strip() for key in FIELDS[:4] + ["review_state"]}
        identifier = row["family_id"]
        if (not re.fullmatch(r"[A-Za-z0-9_.-]+", identifier) or identifier in seen
                or not row["title"] or row["review_state"] not in STATES):
            raise ValueError(f"Invalid or duplicate candidate: {identifier}")
        seen.add(identifier)
        categories = row["categories"].split(" | ")
        if not categories or set(categories) - names or len(set(categories)) != len(categories):
            raise ValueError(f"Invalid categories: {identifier}")
        if any(re.search(r"/Users/|file:|outputs/|token=|password=", value, re.I)
               for value in row.values()):
            raise ValueError(f"Private data in public metadata: {identifier}")
        link = item["publication_url"].strip()
        row["url"] = candidate_url(link) if link else ""
        row["link_status"] = ("unverified_public_url" if row["url"] else
                              "held_url_review" if link else "missing")
        if row["review_state"] == "identity_conflict":
            row.update(url="", link_status="held_identity_conflict")
        rows.append(row)
    if not rows:
        raise ValueError("Empty candidate snapshot")
    return rows


def render_category(name, rows, snapshot_date):
    lines = [f"# {name}", "",
             "[仓库首页](../../../README.md) · [最新目录](../README.md) · [CSV](../catalog.csv)", "",
             f"候选发现索引快照：{snapshot_date}；本主题 {len(rows)} 条暂定论文族记录。", "",
             "> 七类可重叠，不能相加作为唯一论文数。题名、年份与链接仍可能需要核对；收录不代表全文核验、最终纳入或独立人工复核。", "",
             "---", ""]
    for row in rows:
        year = row["year"] if row["year"] != "pending_review" else "年份待核"
        link = f"[Paper](<{row['url']}>)" if row["url"] else "链接待补／待核（不提供待查链接）"
        lines.extend([
            f'- <a id="{row["family_id"].lower()}"></a> **[{markdown(year)}] {markdown(row["title"])}** · {link}<br>',
            f'  `{row["family_id"]}` · {STATES[row["review_state"]]}', "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def export_snapshot(source_path, destination, snapshot_date):
    date.fromisoformat(snapshot_date)
    with source_path.open(encoding="utf-8-sig", newline="") as file:
        rows = project_rows(csv.DictReader(file))
    counts = Counter(row["review_state"] for row in rows)
    links = Counter(row["link_status"] for row in rows)
    digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
    batch = source_path.parent.parent.name
    if not re.fullmatch(r"WM_Goal_Batch_\d{4}-\d{2}-\d{2}_\d+", batch):
        batch = "未登记"
    pages = destination / "categories"
    pages.mkdir(parents=True, exist_ok=True)
    navigation = []
    for name, slug in CATEGORIES:
        selected = [row for row in rows if name in row["categories"].split(" | ")]
        navigation.append(f"| [{name}](categories/{slug}.md) | {len(selected)} |")
        (pages / f"{slug}.md").write_text(render_category(name, selected, snapshot_date), encoding="utf-8")
    with (destination / "catalog.csv").open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: "'" + value if value.lstrip().startswith(("=", "+", "-", "@"))
                             else value for key, value in row.items()})
    readme = ["# 最新候选文献目录", "",
              "[仓库首页](../../README.md) · [下载 CSV](catalog.csv) · [旧目录存档](../README.md)", "",
              f"候选发现索引快照：**{snapshot_date}**；共 **{len(rows)} 条暂定论文族记录**。", "",
              f"其中 **{links['unverified_public_url']} 条提供公开检索链接**；**{len(rows) - links['unverified_public_url']} 条不提供链接**"
              f"（身份冲突 {links['held_identity_conflict']} 条、链接待查 {links['held_url_review']} 条、链接缺失 {links['missing']} 条）。", "",
              "> 这是候选检索目录，不是最终纳入清单。链接尚未逐条联网或与原文核对；能打开也不代表题名匹配。作者、会议、发表状态和实验结论不在本次公开导出范围。引用前须核对原文与实际使用版本。", "",
              "## 七类入口", "", "| 主题 | 暂定论文族归属数 |", "| --- | ---: |", *navigation, "",
              "七类是重叠检索视图；一篇可出现在多个主题，不相加作为唯一论文数。", "",
              "## 核查状态", "",
              "状态沿用累计主表的登记字段；附加证据卡不自动改变整篇论文状态。下面都不代表全文验收或独立人工复核。", "",
              "| 主表登记状态 | 记录数 |", "| --- | ---: |",
              *[f"| {label} | {counts[state]} |" for state, label in STATES.items()], "",
              "## 版本与来源", "",
              "本次只更新候选索引。首页链接的 PDF、LaTeX 与 BibTeX 仍是此前公开的工作稿，不与本次索引同版，也没有随着目录同步升级。", "",
              "旧目录包含 929 条分类记录，其中 15 条非论文占位；清洗后为 758 个暂定论文族。本次累计记录包含旧条目，不与 929 或 758 相加；暂定合并结果仍需复核。旧存档可能保留已发现的错链，不作为当前检索入口。", "",
              f"来源批次：`{batch}`；文件：`master_table.csv`。", "",
              f"源文件 SHA-256：`{digest}`。", "",
              "本次只导出题名、年份、暂定编号、主题、公开链接和核查状态；不导出内部备注、本地路径、学生信息、证据数字或论文 PDF。", "",
              "维护：使用 `export_current_catalog.py`，传入累计主表 CSV 和快照日期；它只生成本目录，不覆盖冻结目录、正文或原始表格。", ""]
    (destination / "README.md").write_text("\n".join(readme), encoding="utf-8")
    return rows


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("master_csv", type=Path)
    parser.add_argument("snapshot_date")
    args = parser.parse_args()
    rows = export_snapshot(args.master_csv, Path(__file__).resolve().parent / "current", args.snapshot_date)
    print(f"Published candidate metadata: {len(rows)} records, {sum(bool(row['url']) for row in rows)} links.")
