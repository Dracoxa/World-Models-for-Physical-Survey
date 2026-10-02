<a id="top"></a>

<div align="center">

# World Models for Physical AI

**面向物理智能的世界模型：概念、模型、策略融合与可靠性**

ACM Computing Surveys 综述工作仓库 · 论文草稿与七类文献索引

<p>
  <a href="paper/preview/main.pdf"><img src="https://img.shields.io/badge/Draft-v0.2-167D8D" alt="Draft v0.2"></a>
  <a href="paper/main.tex"><img src="https://img.shields.io/badge/Target-ACM_CSUR-555555" alt="Target venue: ACM CSUR"></a>
  <a href="#literature"><img src="https://img.shields.io/badge/Topics-7-477B45" alt="7 literature topics"></a>
  <a href="literature/catalog.csv"><img src="https://img.shields.io/badge/Category_records-929-9B5C32" alt="929 category records, not unique papers"></a>
</p>

<p>
  <a href="paper/preview/main.pdf"><b>论文 PDF</b></a> ·
  <a href="#literature"><b>文献导航</b></a> ·
  <a href="paper/references.bib"><b>BibTeX</b></a> ·
  <a href="literature/WRITING_GAPS.md"><b>待补方向</b></a> ·
  <a href="#contributing"><b>参与整理</b></a>
</p>

</div>

---

> **当前版本：v0.2 第一轮内容稿。** 四部分正文、1 图、7 表、31 条参考文献，尚非投稿定稿。文献目录的 **929 条为分类记录**，保留跨主题重复，不代表唯一论文数或已核验论文数。详见[写作进度与证据说明](WRITING_STATUS.md)。

<a id="overview"></a>

## 研究概览

围绕“预测如何服务于物理交互与决策”组织综述，连接数据与表示、预测模型、机器人策略，以及评估和安全。四部分构成正文主线，七类文献目录承担检索与协作，两者不要求一一对应。

<p align="center">
  <a href="paper/figures/fig01_prediction_policy_interfaces.png">
    <img src="paper/figures/fig01_prediction_policy_interfaces.png" width="880" alt="预测与控制接口概念图：直接策略、推理器审查候选动作、显式后果预测三种接口。">
  </a>
</p>

<p align="center"><sub>图 1 · 预测与控制接口。概念示意，不表示实验性能或模型排名。<a href="paper/figures/fig01_prediction_policy_interfaces.pdf">矢量 PDF</a> · <a href="paper/build_figure.py">绘图源码</a></sub></p>

<a id="outline"></a>

## 四部分正文

| 部分 | 核心内容 | 正文入口 |
|:---|:---|:---|
| I · 概念基础与研究范围 | 定义与纳入边界、发展脉络、已有综述与本文定位 | [Foundations and Scope](paper/sections/01_foundations.tex) |
| II · 数据、表示与模型 | 动作数据、视觉预测、潜在表示、结构化物理、跨场景与跨本体泛化 | [Data, Representations, and Predictive Models](paper/sections/02_data_models.tex) |
| III · 与机器人策略的融合 | 模型式规划、想象学习、视觉计划、联合世界与动作模型、Astra 专题 | [Integration with Robot Policies](paper/sections/03_policy_integration.tex) |
| IV · 评估、可靠性与前沿 | 预测质量与决策收益、不确定性、安全约束、恢复机制和研究方向 | [Evaluation, Reliability, and Research Directions](paper/sections/04_evaluation.tex) |

<a id="literature"></a>

## 七类文献导航

按研究主题进入分类页，或下载 [CSV 总表](literature/catalog.csv) 按年份、作者与来源筛选。[完整目录与统计口径](literature/README.md) · 快照日期：2026-10-01。

| 分类 | 检索方向 | 分类记录 |
|:---|:---|---:|
| [01 · 世界模型基础与控制](literature/categories/01-foundations-control.md) | 学习动力学、模型式强化学习、模型预测控制 | 96 |
| [02 · 视觉与视频世界模型](literature/categories/02-visual-video.md) | 动作条件视频预测、交互模拟、长时滚动 | 61 |
| [03 · Latent 与预测表示](literature/categories/03-latent-representations.md) | 潜在动力学、预测表征、表征与控制的连接 | 75 |
| [04 · 结构化物理与多模态](literature/categories/04-physics-multimodal.md) | 三维结构、接触与形变、触觉和力觉 | 54 |
| [05 · 数据、模拟与跨本体](literature/categories/05-data-simulation-embodiment.md) | 机器人数据、模拟数据、人类视频、跨本体对齐 | 192 |
| [06 · 世界模型、VLA 与规划](literature/categories/06-policy-planning.md) | 预测与策略耦合、动作生成、规划与重规划 | 199 |
| [07 · 评估、安全与 Benchmark](literature/categories/07-evaluation-safety.md) | 闭环评估、风险与校准、约束与恢复机制 | 252 |

目录是候选文献索引，不等于正文引用清单。32 条记录暂缺可导出的公开链接；本轮另列的补充来源不计入上述快照。发表状态、版本与实验结论仍需回到原始来源核对。

<a id="updates"></a>

## 进展与下一步

| 日期 | 更新 |
|:---|:---|
| 2026-10-02 | 重整仓库首页，提供图示、四部分正文入口与七类文献导航。 |
| 2026-10-01 | v0.2 第一轮内容稿：四部分正文、1 图、7 表、31 条参考文献；同步 929 条分类记录。 |

下一轮优先补充下列内容，具体文献、检索词和核对状态见[边写边补清单](literature/WRITING_GAPS.md)：

- [ ] 三维、接触、形变、触觉与力觉的模型级原始论文。
- [ ] 导航与驾驶中的预测控制，以及预测预训练和推理时预测的消融。
- [ ] 真实机器人分布外风险、校准、干预成本和安全机制。
- [ ] 人类视频、失败与恢复数据、跨本体动作对齐。
- [ ] 正式出版版本、检索筛选记录与全文证据位置的统一核查。

<a id="contributing"></a>

## 参与整理

通过 [Issue](https://github.com/Dracoxa/World-Models-for-Physical-Survey/issues) 提交补充或纠错，或通过 [Pull Request](https://github.com/Dracoxa/World-Models-for-Physical-Survey/pulls) 修改文献与正文。建议同时提供：

1. **可定位的论文**：完整题名、作者、年份、DOI 或 arXiv 链接；注明预印本或正式发表版本。
2. **分类与用途**：对应七类中的哪一类，以及能够支撑综述中的哪项讨论。
3. **可核查的证据**：原文章节、图表或页码；区分实验观察、作者结论与综述判断。

更正现有记录时请附目录编号。跨主题归类不视为新增独立论文，项目报告与扩展稿中的重合实验也不作为独立重复验证。

<a id="development"></a>

## 编译与维护

<details>
<summary><b>ACM Computing Surveys 模板与论文编译</b></summary>

主文件：[paper/main.tex](paper/main.tex)；参考文献：[paper/references.bib](paper/references.bib)。

稿件使用官方 `acmart` 文档类、`\acmJournal{CSUR}` 和 `ACM-Reference-Format` 参考文献样式。当前采用 `manuscript,review,anonymous` 单栏带行号的工作稿配置，延续项目原始材料；匿名选项是此稿的工作设置，不表示已确认期刊的匿名要求。

最终投稿前应依据 [CSUR 作者指南](https://dl.acm.org/journal/csur/author-guidelines)核对当期规定，补齐作者、机构和元数据。当前没有编造 DOI、卷期或录用日期。CSUR 的期刊排版预览可将文档类选项改为 `acmsmall`；审稿稿件的具体设置仍以编辑部要求为准。

安装包含 `acmart` 的 TeX Live / MacTeX 后，在 `paper/` 中运行：

```sh
latexmk -pdf -no-shell-escape -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

`paper/preview/main.pdf` 是已编译的审阅快照。修改正文后需要重新编译并更新此快照。

</details>

<details>
<summary><b>从协作表更新文献目录</b></summary>

在仓库根目录运行：

```sh
python literature/export_catalog.py path/to/workbook.xlsx
```

导出依赖 `openpyxl`。分类记录保留跨主题重复，尚未完成逐篇真实性和结论核查；公开目录提供题名与来源检索，正文仅使用已核对的相关出处。

</details>

<details>
<summary><b>图表源文件</b></summary>

`paper/build_figure.py` 使用 Matplotlib 生成 PDF、SVG 和 PNG。矢量文件用于论文，PNG 用于预览。图 1 是接口概念图，不包含实验统计或模型能力排名。

</details>

---

首页编排参考 [NanoResearch](https://github.com/OpenRaiser/NanoResearch)，研究内容与文献目录独立整理。

<p align="right"><a href="#top">返回顶部</a></p>
