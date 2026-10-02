# 外部调研库去重新增候选

生成日期：2026-10-02。该文件由 `compare_external_surveys.py` 生成，是待核验候选，不代表已纳入正文。

## 快照与口径

- NTUMARS/Awesome-World-Model-for-Robotics-Policy @ 5f69b4e
- Li-Zn-H/AwesomeWorldModels @ 9de513c
- OpenMOSS/Awesome-WAM @ aa6cd05
- 本地基线：929 条分类记录，825 个规范化题名；跨类别重复保留。
- 去重顺序：arXiv ID、规范化题名、相似度不低于 0.94 的近似题名。

## 去重结果

| 来源 | 提取 arXiv 条目 | 已在目录 | 已在补充材料追踪 | 新增候选 |
|---|---:|---:|---:|---:|
| NTUMARS | 148 | 56 | 2 | 90 |
| Li-Zn-H | 169 | 31 | 1 | 137 |
| OpenMOSS | 97 | 33 | 1 | 63 |

三个来源合并后得到 341 个唯一 arXiv ID，其中 253 个未在本地目录中找到。完整清单见 [external_candidates.csv](external_candidates.csv)。

首批 5 篇候选已完成原文核验并进入正文，证据边界见[原文核验批次 01](EVIDENCE_BATCH_01.md)。其余条目仍是待筛候选。

## 优先核验候选

展示“最高”优先级，以及被至少两个近邻仓库共同收录的“高”优先级条目。优先级是检索排序，不是质量评价或纳入决定。

| 优先级 | 年份 | 论文 | 来源 | 排序原因 |
|---|---:|---|---|---|
| 最高 | 2026 | [A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268) | Li-Zn-H | 2026 新作且命中薄弱方向：3d |
| 最高 | 2026 | [Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation](https://arxiv.org/abs/2607.01060) | Li-Zn-H | 2026 新作且命中薄弱方向：evaluation |
| 最高 | 2026 | [Interactive World Simulator for Robot Policy Training and Evaluation](https://arxiv.org/abs/2603.08546) | Li-Zn-H, NTUMARS, OpenMOSS | 2026 新作、多源交叉且命中薄弱方向：evaluation |
| 最高 | 2026 | [Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669) | NTUMARS | 2026 新作且命中薄弱方向：4d |
| 最高 | 2026 | [MVISTA-4D: View-Consistent 4D World Model with Test-Time Action Inference for Robotic Manipulation](https://arxiv.org/abs/2602.09878) | OpenMOSS | 2026 新作且命中薄弱方向：4d |
| 最高 | 2026 | [Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action Model](https://arxiv.org/abs/2604.03181) | NTUMARS | 2026 新作且命中薄弱方向：3d |
| 最高 | 2026 | [OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation](https://arxiv.org/abs/2603.19201) | OpenMOSS | 2026 新作且命中薄弱方向：contact、tactile |
| 最高 | 2026 | [Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation](https://arxiv.org/abs/2606.03159) | Li-Zn-H | 2026 新作且命中薄弱方向：closed loop |
| 最高 | 2026 | [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/abs/2604.26694) | NTUMARS, OpenMOSS | 2026 新作、多源交叉且命中薄弱方向：4d |
| 最高 | 2026 | [View Planning with Multi-Turn VLM Agents](https://arxiv.org/abs/2605.29563) | Li-Zn-H | 2026 新作且命中薄弱方向：planning |
| 最高 | 2026 | [World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy](https://arxiv.org/abs/2602.06508) | Li-Zn-H, NTUMARS | 2026 新作、多源交叉且命中薄弱方向：closed loop |
| 最高 | 2026 | [World-Value-Action Model: Implicit Planning for Vision-Language-Action Systems](https://arxiv.org/abs/2604.14732) | NTUMARS, OpenMOSS | 2026 新作、多源交叉且命中薄弱方向：planning |
| 最高 | 2026 | [Wow, wo, val! A Comprehensive Embodied World Model Evaluation Turing Test](https://arxiv.org/abs/2601.04137) | NTUMARS | 2026 新作且命中薄弱方向：evaluation |
| 最高 | 2025 | [3DFlowAction: Learning Cross-Embodiment Manipulation from 3D Flow World Model](https://arxiv.org/abs/2506.06199) | Li-Zn-H, OpenMOSS | 多源交叉且命中薄弱方向：3d、cross embodiment |
| 最高 | 2025 | [Geometry-aware 4D Video Generation for Robot Manipulation](https://arxiv.org/abs/2507.01099) | Li-Zn-H, OpenMOSS | 多源交叉且命中薄弱方向：4d、geometry |
| 最高 | 2025 | [TesserAct: Learning 4D Embodied World Models](https://arxiv.org/abs/2504.20995) | Li-Zn-H, NTUMARS, OpenMOSS | 多源交叉且命中薄弱方向：4d |
| 最高 | 2025 | [World-in-World: World Models in a Closed-Loop World](https://arxiv.org/abs/2510.18135) | Li-Zn-H, NTUMARS | 多源交叉且命中薄弱方向：closed loop |
| 高 | 2026 | [AIM: Intent-Aware Unified world action Modeling with Spatial Value Maps](https://arxiv.org/abs/2604.11135) | NTUMARS, OpenMOSS | 2026 新作 |
| 高 | 2026 | [Causal World Modeling for Robot Control (LingBot-VA)](https://arxiv.org/abs/2601.21998) | NTUMARS, OpenMOSS | 2026 新作 |
| 高 | 2026 | [DexWorldModel: Causal Latent World Modeling towards Automated Learning of Embodied Tasks](https://arxiv.org/abs/2604.16484) | NTUMARS, OpenMOSS | 2026 新作 |
| 高 | 2026 | [DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control](https://arxiv.org/abs/2603.10448) | NTUMARS, OpenMOSS | 2026 新作 |
| 高 | 2026 | [Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666) | NTUMARS, OpenMOSS | 2026 新作 |
| 高 | 2026 | [Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://arxiv.org/abs/2603.19312) | Li-Zn-H, NTUMARS | 2026 新作 |
| 高 | 2026 | [Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482) | Li-Zn-H, NTUMARS | 2026 新作 |
| 高 | 2026 | [VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model](https://arxiv.org/abs/2602.10098) | NTUMARS, OpenMOSS | 2026 新作 |
| 高 | 2026 | [WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL](https://arxiv.org/abs/2602.13977) | Li-Zn-H, NTUMARS, OpenMOSS | 2026 新作 |
| 高 | 2026 | [World-Gymnast: Training Robots with Reinforcement Learning in a World Model](https://arxiv.org/abs/2602.02454) | NTUMARS, OpenMOSS | 2026 新作 |
| 高 | 2025 | [F1: A Vision-Language-Action Model Bridging Understanding and Generation to Actions](https://arxiv.org/abs/2509.06951) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [Large Video Planner Enables Generalizable Robot Control](https://arxiv.org/abs/2512.15840) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [NovaFlow: Zero-shot Manipulation via Actionable Flow from Generated Videos](https://arxiv.org/abs/2510.08568) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [PhysWorld: Robot Learning from a Physical World Model](https://arxiv.org/abs/2511.07416) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [RoboEnvision: A Long-Horizon Video Generation Model for Multi-Task Robot Manipulation](https://arxiv.org/abs/2506.22007) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [RynnVLA-002: A Unified Vision-Language-Action and World Model](https://arxiv.org/abs/2511.17502) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process](https://arxiv.org/abs/2511.01718) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [Unified Video Action Model](https://arxiv.org/abs/2503.00200) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators](https://arxiv.org/abs/2510.00406) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [Video Generators are Robot Policies](https://arxiv.org/abs/2508.00795) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [VideoVLA: Video Generators Can Be Generalizable Robot Manipulators](https://arxiv.org/abs/2512.06963) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [WMPO: World Model-based Policy Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2511.09515) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [World-Env: Leveraging World Model as a Virtual Environment for VLA Post-Training](https://arxiv.org/abs/2509.24948) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs](https://arxiv.org/abs/2512.15692) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2025 | [villa-X: Enhancing Latent Action Modeling in Vision-Language-Action Models](https://arxiv.org/abs/2507.23682) | Li-Zn-H, OpenMOSS | 被多个近邻仓库收录 |
| 高 | 2023 | [Learning to Act from Actionless Videos through Dense Correspondences](https://arxiv.org/abs/2310.08576) | NTUMARS, OpenMOSS | 被多个近邻仓库收录 |

## 人工验收要求

每篇候选进入七类目录前，至少核对题名、作者、版本、发表状态、任务环境、动作是否进入预测、是否闭环使用，以及能够支撑正文的具体图表或章节。自动匹配不能替代全文核验。
