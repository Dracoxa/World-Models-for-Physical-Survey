<div align="center">

# 面向物理智能的世界模型

**接口、实验证据与下游效用**

World Models for Physical AI

[![Project website](https://img.shields.io/badge/Website-GitHub_Pages-1d4ed8?style=flat-square)](https://dracoxa.github.io/World-Models-for-Physical-Survey/)
[![Survey PDF](https://img.shields.io/badge/PDF-Survey-0f766e?style=flat-square)](docs/assets/survey.pdf)
[![Line-numbered PDF](https://img.shields.io/badge/PDF-Line_Numbered-334155?style=flat-square)](docs/assets/survey-review.pdf)
[![Evidence Companion](https://img.shields.io/badge/Data-Evidence_Companion-b45309?style=flat-square)](docs/assets/Evidence-companion.zip)
[![Literature Catalogue](https://img.shields.io/badge/Index-Literature_Catalogue-64748b?style=flat-square)](literature/current/README.md)

[English](README.md) · **简体中文** · [Evidence Explorer / 证据浏览器](https://dracoxa.github.io/World-Models-for-Physical-Survey/explorer.html)

</div>

## 预测什么时候能改善决策？

世界模型预测环境如何演化。这些预测可以用来监督策略训练、给候选计划评分、辅助生成动作、评估策略，或在执行中修正动作。本综述沿着三个问题展开：**预测什么、动作如何参与、预测由谁在何时使用**。定量分析以机器人操作为主，驾驶和导航案例用于比较不同领域的预测接口。

<p align="center">
  <a href="https://dracoxa.github.io/World-Models-for-Physical-Survey/#findings">
    <img src="docs/assets/figure-04.webp" alt="Fast-WAM Base、V-JEPA Policy 和 Fast-WAM Joint 在训练和部署阶段如何使用预测" width="840">
  </a>
</p>

[浏览七张论文插图](https://dracoxa.github.io/World-Models-for-Physical-Survey/#findings) · [查看三项拟议验证实验](https://dracoxa.github.io/World-Models-for-Physical-Survey/#tests)

## 主要发现

- **训练监督和部署时的预测要分别检验。** Fast-WAM Base 在训练中加入视频预测后，RoboTwin 平均成功率从 83.8% 升至 91.8%。部署时，该策略直接生成动作。[Fast-WAM 原文](https://arxiv.org/html/2603.16666v2#S4)
- **离线指标和闭环结果可以给出不同排序。** 在 RoboCasa 上，X-WAM 用几何评分选择候选时的闭环成功率为 82.5%，用一致性评分时为 77.4%。离线误差恢复指标则更偏向一致性评分。[GeoBoN 表 3](https://arxiv.org/html/2607.17454v1#S4.SS4)
- **模拟器的评估一致性与生成数据的训练价值需要分别衡量。** 在 DexTouch-WM 中，WM-Mix 对已有策略的评估与实机评分更一致。在另一组训练实验里，使用 WM-Robot 生成的数据后，三种学习器中有两种取得了更高的实机得分。[DexTouch-WM 表 III–IV](https://arxiv.org/html/2609.20649v2#S4)

## 证据和基准

| 入口 | 可以查到什么 |
| --- | --- |
| [证据图谱](https://dracoxa.github.io/World-Models-for-Physical-Survey/explorer.html#evidence) | 从 **75 篇选定研究**中提取 **93 条比较记录**。其中 56 篇报告任务执行结果，29 篇贡献 30 条符合本文定义的组件对照。排除 4 条涉及组合改动的记录后，仍有 26 篇含有这类对照。 |
| [RoboTwin 2.0](https://dracoxa.github.io/World-Models-for-Physical-Survey/explorer.html#benchmarks) | 33 个配置共 **1,650 对**同任务的干净与随机化场景结果。随机化后，32 个配置的平均成功率下降。 |
| [RoboDojo](https://dracoxa.github.io/World-Models-for-Physical-Survey/explorer.html#benchmarks) | 66 个配置共 **3,536 个**已报告的任务条件单元。其中 858 个单元的完成率为零，但获得了正的进度分。 |

证据图谱描述本综述选取的研究。两项基准使用 2026 年 11 月 10 日的快照，按各自的评价单位统计。

## 下载与引用

- [论文 PDF](docs/assets/survey.pdf) · [带行号 PDF](docs/assets/survey-review.pdf)
- [证据包](docs/assets/Evidence-companion.zip)，含原文对照记录、分析工作簿和基准快照
- [文献检索目录](literature/current/README.md) · [CSV](literature/current/catalog.csv)

```bibtex
@misc{anonymous2026worldmodelsphysical,
  title  = {World Models for Physical AI: Interfaces, Experimental Evidence, and Downstream Utility},
  author = {{Anonymous Author(s)}},
  year   = {2026},
  url    = {https://dracoxa.github.io/World-Models-for-Physical-Survey/},
  note   = {Anonymous survey manuscript}
}
```

[在官网复制 BibTeX](https://dracoxa.github.io/World-Models-for-Physical-Survey/#cite) · [反馈或纠错](https://github.com/Dracoxa/World-Models-for-Physical-Survey/issues/new)
