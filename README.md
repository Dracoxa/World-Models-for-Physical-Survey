<div align="center">

# World Models for Physical AI

### Learning to Predict, Plan, and Act in the Real World

[![Draft PDF](https://img.shields.io/badge/Paper-Working_Draft-2563eb)](paper/preview/main.pdf)
[![LaTeX](https://img.shields.io/badge/LaTeX-Source-008080)](paper/main.tex)
[![Literature](https://img.shields.io/badge/Literature-Seven_Themes-6b7280)](#paper-list)
[![CSV](https://img.shields.io/badge/Data-CSV-22863a)](literature/current/catalog.csv)
[![BibTeX](https://img.shields.io/badge/References-BibTeX-555555)](paper/references.bib)

面向物理智能的世界模型综述与文献导航

</div>

本仓库收集世界模型及相关控制、表示、数据与安全研究，配套综述 **World Models for Physical AI: Learning to Predict, Plan, and Act in the Real World**。

- **讨论主线**：预测什么、动作如何参与、预测在训练或部署中怎样发挥作用。
- **组织方式**：正文保留四部分，文献按七个可交叉的主题检索。
- **当前状态**：采用 ACM Computing Surveys 模板，仍为工作草稿，尚未正式发表。

**文献收集（2026-10-10 快照）**：累计 **781 条暂定去重候选记录**，其中 **763 条附公开检索链接**、18 条链接待补或待查。进入 [最新文献目录](literature/current/README.md)，或下载 [候选主表 CSV](literature/current/catalog.csv)。收录不等于全文核验或最终纳入。

本次更新独立的候选索引；上方 PDF、LaTeX 与 BibTeX 仍是此前公开的工作稿，不与本次目录同版。

<a id="contents"></a>

## Table of Contents

- [Survey Overview · 综述框架](#survey-overview)
- [Foundations & Control · 世界模型基础与控制](#foundations-control)
- [Visual & Video World Models · 视觉与视频世界模型](#visual-video)
- [Latent & Predictive Representations · Latent 与预测表示](#latent-representations)
- [Structured Physics & Multimodal Models · 结构化物理与多模态](#physics-multimodal)
- [Data, Simulation & Embodiment · 数据、模拟与跨本体](#data-simulation-embodiment)
- [World Models, VLA & Planning · 世界模型、VLA 与规划](#policy-planning)
- [Evaluation, Safety & Benchmarks · 评估、安全与 Benchmark](#evaluation-safety)
- [Contributing · 补充与纠错](#contributing)

---

<a id="survey-overview"></a>

## Survey Overview

| 部分 | 主要内容 |
| --- | --- |
| [一、基础与发展脉络](paper/sections/01_foundations.tex) | 概念边界、模型式控制、预测表示与相关综述定位 |
| [二、数据、表示与模型](paper/sections/02_data_models.tex) | 视觉与视频预测、latent dynamics、结构化物理、多模态数据与跨本体泛化 |
| [三、机器人策略融合](paper/sections/03_policy_integration.tex) | 模型式规划、想象中的策略学习、VLA、联合世界与动作模型，以及推理与策略接口 |
| [四、评估、可靠性与前沿](paper/sections/04_evaluation.tex) | 预测质量与决策效用、闭环评估、不确定性、安全约束与运行时护栏 |

> **图示占位：预测与动作接口（待重绘）。**
>
> **图示占位：证据与评估流程（待重绘）。**

---

<a id="paper-list"></a>
<a id="文献目录"></a>

## Paper List

以下是旧协作表快照的浏览示例，不是排名或新增纳入清单。年份不代表最新发表状态；完整分类入口指向最新候选索引，提供题名、年份、论文链接、暂定编号与核查状态。作者、会议和实验结论须另查原文。

> 七类是重叠检索视图，不是七种互斥机制，也不是七章正文。目录包含核心方法、支撑资源及边界对照；不能把收录等同于已核验。

<a id="foundations-control"></a>

### Foundations & Control

> 世界模型基础与控制：学习动力学、模型式强化学习、模型预测控制与想象中的策略学习。

- **[2018] World Models** · [Paper](https://arxiv.org/abs/1803.10122)
- **[2019] Learning Latent Dynamics for Planning from Pixels** · [Paper](https://arxiv.org/abs/1811.04551)

[查看完整分类](literature/current/categories/01-foundations-control.md) · [返回目录](#contents)

<a id="visual-video"></a>

### Visual & Video World Models

> 视觉与视频世界模型：视频预测、动作条件生成与交互式世界模拟。

- **[2024] Genie: Generative Interactive Environments** · [Paper](https://arxiv.org/abs/2402.15391)
- **[2025] Cosmos World Foundation Model Platform for Physical AI** · [Paper](https://arxiv.org/abs/2501.03575)

[查看完整分类](literature/current/categories/02-visual-video.md) · [返回目录](#contents)

<a id="latent-representations"></a>

### Latent & Predictive Representations

> Latent 与预测表示：潜空间动力学、预测嵌入及支撑机器人学习的视觉表示。

- **[2024] Connecting Joint-Embedding Predictive Architecture with Contrastive Self-supervised Learning (C-JEPA)** · [Paper](https://papers.nips.cc/paper_files/paper/2024/hash/04a80267ad46fc730011f8760f265054-Paper-Conference.pdf)
- **[2025] V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning** · [Paper](https://arxiv.org/abs/2506.09985)

[查看完整分类](literature/current/categories/03-latent-representations.md) · [返回目录](#contents)

<a id="physics-multimodal"></a>

### Structured Physics & Multimodal Models

> 结构化物理与多模态：物体、图与网格动力学，3D/4D 表示及接触、触觉和多模态交互。

- **[2016] Interaction networks for learning about objects, relations and physics** · [Paper](https://arxiv.org/abs/1612.00222)
- **[2021] Learning mesh-based simulation with graph networks** · [Paper](https://arxiv.org/abs/2010.03409)

[查看完整分类](literature/current/categories/04-physics-multimodal.md) · [返回目录](#contents)

<a id="data-simulation-embodiment"></a>

### Data, Simulation & Embodiment

> 数据、模拟与跨本体：机器人数据、仿真环境、合成数据与跨机器人迁移；资源不自动等同于世界模型方法。

- **[2019] RoboNet: Large-scale multi-robot learning** · [Paper](https://arxiv.org/abs/1910.11215)
- **[2024] Open x-embodiment: Robotic learning datasets and RT-X models** · [Paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10611477&origin_source=search&origin_method=searchbar)

[查看完整分类](literature/current/categories/05-data-simulation-embodiment.md) · [返回目录](#contents)

<a id="policy-planning"></a>

### World Models, VLA & Planning

> 世界模型、VLA 与规划：预测如何进入动作选择、策略学习、联合建模与策略后训练。

- **[2025] WorldVLA: Towards autoregressive action world model** · [Paper](https://arxiv.org/abs/2506.21539)
- **[2025] DiWA: Diffusion Policy Adaptation with World Models** · [Paper](https://arxiv.org/abs/2508.03645)

[查看完整分类](literature/current/categories/06-policy-planning.md) · [返回目录](#contents)

<a id="evaluation-safety"></a>

### Evaluation, Safety & Benchmarks

> 评估、安全与 Benchmark：分开看预测质量、策略收益与可靠性，涵盖不确定性、安全约束、运行时监测与恢复。

- **[2015] A Comprehensive Survey on Safe Reinforcement Learning** · [Paper](https://www.jmlr.org/papers/volume16/garcia15a.html)
- **[2025] WorldEval: World Model as Real-World Robot Policies Evaluator** · [Paper](https://arxiv.org/abs/2505.19017)

[查看完整分类](literature/current/categories/07-evaluation-safety.md) · [返回目录](#contents)

---

<a id="contributing"></a>

## Contributing

欢迎通过 [Issue](https://github.com/Dracoxa/World-Models-for-Physical-Survey/issues) 或 [Pull Request](https://github.com/Dracoxa/World-Models-for-Physical-Survey/pulls) 推荐论文、纠正错链或补充正式出版版本。

请提供：**论文标题、年份、DOI/arXiv/正式出版链接、所属主题，以及一句与综述相关的理由**。优先使用作者原文或正式出版来源。

完整候选索引与状态说明见 [Latest Literature Catalog](literature/current/README.md)；可下载 [CSV](literature/current/catalog.csv) 检索。旧协作表目录留作 [历史存档](literature/README.md)。补充内容经核对后再进入正文，不直接照收其他仓库的分类或结论。

展示格式参考 [NTUMARS / Awesome-World-Model-for-Robotics-Policy](https://github.com/NTUMARS/Awesome-World-Model-for-Robotics-Policy)，文献内容及研究框架按本项目维护。
