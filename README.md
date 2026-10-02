# World Models for Physical AI

**Learning to Predict, Plan, and Act in the Real World**

面向物理智能的世界模型综述与文献导航：从动力学与预测表示，到机器人规划、策略学习和安全评估。

[论文 PDF](paper/preview/main.pdf) · [LaTeX 源码](paper/main.tex) · [七类文献](#文献目录) · [CSV 下载](literature/catalog.csv) · [BibTeX](paper/references.bib)

---

## 综述框架

本综述围绕三个问题组织讨论：**预测什么、动作如何参与、预测如何用于决策与执行**。正文采用 ACM Computing Surveys 模板，目前为写作中的草稿，尚未正式发表。

| 部分 | 主要内容 |
| --- | --- |
| [一、基础与发展脉络](paper/sections/01_foundations.tex) | 概念边界、模型式控制、预测表示与相关综述定位 |
| [二、数据、表示与模型](paper/sections/02_data_models.tex) | 视觉与视频预测、latent dynamics、结构化物理、多模态数据与跨本体泛化 |
| [三、机器人策略融合](paper/sections/03_policy_integration.tex) | 模型式规划、想象中的策略学习、VLA、联合世界与动作模型，以及 Astra 等推理与策略接口 |
| [四、评估、可靠性与前沿](paper/sections/04_evaluation.tex) | 预测质量与决策效用、闭环评估、不确定性、安全约束与运行时护栏 |

<details>
<summary>查看预测与控制接口示意图</summary>

![预测与控制接口：直接动作生成、推理审查策略建议、显式预测动作后果](paper/figures/fig01_prediction_policy_interfaces.png)

示意图用于区分不同系统接口，不表示所有系统都具有显式世界模型，也不构成性能排名。

</details>

## 文献目录

按研究主题检索论文；同一工作可能出现在多个类别中。

| 主题 | 检索方向 |
| --- | --- |
| [世界模型基础与控制](literature/categories/01-foundations-control.md) | 学习动力学、model-based RL、MPC、想象与控制 |
| [视觉与视频世界模型](literature/categories/02-visual-video.md) | 视频预测、动作条件生成、交互式世界模拟 |
| [Latent 与预测表示](literature/categories/03-latent-representations.md) | 潜空间动力学、JEPA、预测表征与机器人视觉表示 |
| [结构化物理与多模态](literature/categories/04-physics-multimodal.md) | 3D/4D、物体与粒子、接触与触觉、多模态物理交互 |
| [数据、模拟与跨本体](literature/categories/05-data-simulation-embodiment.md) | 机器人数据、仿真、合成数据、跨机器人迁移 |
| [世界模型、VLA 与规划](literature/categories/06-policy-planning.md) | 预测驱动规划、视觉动作模型、策略学习、推理与动作融合 |
| [评估、安全与 Benchmark](literature/categories/07-evaluation-safety.md) | 预测与闭环评估、安全学习、不确定性、运行时监测与恢复 |

目录是候选文献索引，不代表所有条目的元数据与实验结论均已核验。论文版本与发表状态应以原始来源为准。

## 阅读与使用

- **了解整体内容**：阅读 [论文 PDF](paper/preview/main.pdf)，按上方四部分框架定位章节。
- **查找相关工作**：进入主题分类页，或下载 [文献 CSV](literature/catalog.csv) 按标题、作者、年份和来源筛选。
- **引用与修改**：正文引用见 [BibTeX](paper/references.bib)；写作源文件位于 [paper/](paper/)。

## 补充文献

欢迎通过 [Issue](https://github.com/Dracoxa/World-Models-for-Physical-Survey/issues) 或 [Pull Request](https://github.com/Dracoxa/World-Models-for-Physical-Survey/pulls) 推荐论文、纠正错链或补充正式出版版本。

请提供：**论文标题、年份、DOI/arXiv/正式出版链接、所属主题，以及一句与综述相关的理由**。优先使用作者原文或正式出版来源。
