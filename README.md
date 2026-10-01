# World Models for Physical AI

ACM Computing Surveys 综述工作仓库。当前为 **v0.1 写作初稿**，不是已完成或已投稿版本。

## 阅读入口

- [论文 PDF](paper/preview/main.pdf)
- [LaTeX 主文件](paper/main.tex)
- [七类文献检索目录](literature/README.md)
- [929 条分类记录 CSV](literature/catalog.csv)
- [写作进度与证据说明](WRITING_STATUS.md)
- [图 1：预测与控制接口](paper/figures/fig01_prediction_policy_interfaces.png)

## 文章结构

1. 世界模型的概念基础与研究范围。
2. 面向物理交互的数据、表示与模型。
3. 世界模型与机器人策略的系统融合。
4. 评估、可靠性、安全与研究前沿。

七类文献目录用于检索和协作，四部分用于正文组织，两者不要求一一对应。

## ACM Computing Surveys 模板

稿件使用官方 `acmart` 文档类、`\acmJournal{CSUR}` 和 `ACM-Reference-Format` 参考文献样式。当前采用 `manuscript,review,anonymous` 单栏带行号的工作稿配置，延续项目原始材料；匿名选项是此稿的工作设置，不表示已确认期刊的匿名要求。

最终投稿前应依据 [CSUR 作者指南](https://dl.acm.org/journal/csur/author-guidelines)核对当期规定，补齐作者、机构和元数据。当前没有编造 DOI、卷期或录用日期。CSUR 的期刊排版预览可将文档类选项改为 `acmsmall`；审稿稿件的具体设置仍以编辑部要求为准。

安装包含 `acmart` 的 TeX Live / MacTeX 后，在 `paper/` 中运行：

```sh
latexmk -pdf -no-shell-escape -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

`paper/preview/main.pdf` 是已编译的审阅快照。修改正文后需要重新编译并更新此快照。

## 文献目录更新

```sh
python literature/export_catalog.py path/to/workbook.xlsx
```

导出依赖 `openpyxl`。分类记录保留跨主题重复，尚未完成逐篇真实性和结论核查；公开目录提供题名与来源检索，正文仅使用已核对的相关出处。

## 图表源文件

`paper/build_figure.py` 使用 Matplotlib 生成 PDF、SVG 和 PNG。矢量文件用于论文，PNG 用于预览。图 1 是接口概念图，不包含实验统计或模型能力排名。
