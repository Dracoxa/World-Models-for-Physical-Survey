# 外部调研库去重后新增候选

生成日期：2026-10-02。该文件由 `compare_external_surveys.py` 生成，是待核验候选，不代表已纳入正文。

## 快照与口径

- RCL-Robotics/Awesome-World-Action-Models @ 7985fa2
- world-action-models/awesome-world-action-models @ 9be4441
- NJU3DV-LoongGroup/Embodied-World-Models-Survey @ 185871d
- 本地基线：929 条分类记录，825 个规范化题名；跨类别重复保留。
- 去重顺序：arXiv ID、规范化题名、相似度不低于 0.94 的近似题名。
- GitHub 仓库条目只用于发现；候选数量不代表纳入数量、证据数量或已核验论文数量。

## 去重结果

| 来源 | 提取 arXiv 条目 | 已在目录 | 已在补充材料追踪 | 题名待解析 | 新增候选 |
|---|---:|---:|---:|---:|---:|
| RCL | 456 | 123 | 75 | 1 | 257 |
| NUS-WAM | 110 | 25 | 51 | 1 | 33 |
| NJU3DV | 149 | 43 | 22 | 1 | 83 |

3 个来源合并后得到 633 个唯一 arXiv ID，其中 359 个未在本地目录或已跟踪材料中找到。完整清单见配套 CSV。

## 优先核验候选

展示“最高”优先级，以及被至少两个近邻仓库共同收录的“高”优先级条目。优先级是检索排序，不是质量评价或纳入决定。

| 优先级 | 年份 | 论文 | 来源 | 排序原因 |
|---|---:|---|---|---|
| 最高 | 2026 | [DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning (DriveDreamer-Policy)](https://arxiv.org/abs/2604.01765) | NUS-WAM, RCL | 多源交叉、2026 新作且命中薄弱方向：geometry、planning |
| 最高 | 2026 | [VTAM: Video-Tactile-Action Models for Complex Physical Interaction Beyond VLAs (VTAM)](https://arxiv.org/abs/2603.23481) | NUS-WAM, RCL | 多源交叉、2026 新作且命中薄弱方向：tactile |
| 高 | 2026 | [DriveWAM: Video Generative Priors Enable Scalable World-Action Modeling for Autonomous Driving (DriveWAM)](https://arxiv.org/abs/2605.28544) | NUS-WAM, RCL | 被多个近邻仓库收录 |
| 高 | 2026 | [NoiseGate: Learning Per-Latent Timestep Schedules as Information Gating in World Action Models (NoiseGate)](https://arxiv.org/abs/2605.07794) | NUS-WAM, RCL | 被多个近邻仓库收录 |
| 高 | 2026 | [Point Tracking Improves World Action Models (JOPAT)](https://arxiv.org/abs/2605.23856) | NUS-WAM, RCL | 被多个近邻仓库收录 |
| 高 | 2026 | [The DAWN of World-Action Interactive Models (DAWN)](https://arxiv.org/abs/2605.11550) | NUS-WAM, RCL | 被多个近邻仓库收录 |
| 高 | 2026 | [VAMPO: Policy Optimization for Improving Visual Dynamics in Video Action Models (VAMPO)](https://arxiv.org/abs/2603.19370) | NUS-WAM, RCL | 被多个近邻仓库收录 |
| 高 | 2026 | [WALL-WM: Carving World Action Modeling at the Event Joints (WALL-WM)](https://arxiv.org/abs/2606.01955) | NUS-WAM, RCL | 被多个近邻仓库收录 |
| 高 | 2025 | [Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control](https://arxiv.org/abs/2503.14492) | NJU3DV, RCL | 被多个近邻仓库收录 |
| 高 | 2025 | [FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2501.09747) | NJU3DV, RCL | 被多个近邻仓库收录 |
| 高 | 2025 | [Learning Robot Manipulation from Audio World Models (Audio-WM)](https://arxiv.org/abs/2512.08405) | NUS-WAM, RCL | 被多个近邻仓库收录 |
| 高 | 2025 | [World Models for Learning Dexterous Hand-Object Interactions from Human Videos](https://arxiv.org/abs/2512.13644) | NUS-WAM, RCL | 被多个近邻仓库收录 |
| 高 | 2023 | [ADriver-I: A General World Model for Autonomous Driving](https://arxiv.org/abs/2311.13549) | NJU3DV, RCL | 被多个近邻仓库收录 |
| 高 | 2022 | [DexGraspNet: A Large-Scale Robotic Dexterous Grasp Dataset for General Objects Based on Simulation](https://arxiv.org/abs/2210.02697) | NJU3DV, RCL | 被多个近邻仓库收录 |

## 人工验收要求

每篇候选进入七类目录前，至少核对题名、作者、版本、发表状态、任务环境、动作是否进入预测、是否闭环使用，以及能够支撑正文的具体图表或章节。自动匹配不能替代全文核验。
