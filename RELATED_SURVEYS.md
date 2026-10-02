# 同类开源调研与差异化定位

更新日期：2026-10-02。检索方式为 `rapid-scan`：通过 GitHub 仓库检索、网页检索和论文入口交叉核对，目标是发现可借鉴、可追踪的近邻项目，不声称穷尽全部相关仓库。仓库活跃度与关注度只用于判断维护价值，不作为论文质量证据。

## 最接近的论文配套仓库

| 项目 | 论文或状态 | 主要范围 | 对本项目的直接价值 | 使用时的边界 |
|---|---|---|---|---|
| [tsinghua-fib-lab/World-Model](https://github.com/tsinghua-fib-lab/World-Model) | [ACM Computing Surveys 2025](https://doi.org/10.1145/3746449) | 通用世界模型、视频生成、具身与城市智能 | 最接近目标期刊；可参考综述叙事、路线图和持续更新方式 | 范围明显宽于 Physical AI，不宜照搬其应用分类 |
| [NTUMARS/Awesome-World-Model-for-Robotics-Policy](https://github.com/NTUMARS/Awesome-World-Model-for-Robotics-Policy) | [arXiv:2605.00080](https://arxiv.org/abs/2605.00080) | 机器人策略、学习模拟器、评估、数据和视频世界模型 | 与我们的“预测如何进入策略”主线最接近；其 benchmark 和 dataset 分区适合交叉补漏 | 当前为预印本；具体结论仍需回到原始论文核验 |
| [Li-Zn-H/AwesomeWorldModels](https://github.com/Li-Zn-H/AwesomeWorldModels) | [arXiv:2510.16732v3](https://arxiv.org/abs/2510.16732v3) | 具身世界模型；功能、时间建模和空间表示三轴分类 | 适合核对表示类型、自动驾驶/机器人覆盖和物理一致性评价 | 分类粒度很细，不应让我们的四部分正文退化为长目录 |
| [JiahuaDong/Awesome-World-Models](https://github.com/JiahuaDong/Awesome-World-Models) | 2026 TechRxiv 综述配套仓库 | 强化学习、观测生成、latent、对象中心模型及机器人/驾驶/科学应用 | 已持续补入 ICML、ECCV 2026 条目，适合做会议级更新检查和 benchmark/指标交叉核对 | 范围远宽于 Physical AI；仓库标签和性能汇总需回原始论文验证 |
| [clearlab-sustech/WorldModelSurvey](https://github.com/clearlab-sustech/WorldModelSurvey) | [arXiv:2607.00836](https://arxiv.org/abs/2607.00836) | 从 world model 到 world action model 的机器人教程 | 定义图、输入输出接口图和四类 WAM 范式清楚，适合检查概念图表达 | 是简明教程而非大规模证据综述 |
| [FutureTwT/awesome-world-models-for-vla-agents](https://github.com/FutureTwT/awesome-world-models-for-vla-agents) | 2026 TechRxiv 预印本配套仓库 | World Planner、World Action Model、World Synthesizer、World Simulator | 适合补 VLA 集成方式、基础模型、指标和 benchmark | 只覆盖 VLA 近邻，不代表全部 Physical AI |
| [OpenMOSS/Awesome-WAM](https://github.com/OpenMOSS/Awesome-WAM) | [arXiv:2605.12090](https://arxiv.org/abs/2605.12090) | Cascaded / Joint World Action Models、训练数据与评估 | WAM 与 VLA 交叉部分更新快，并提供 benchmark 组织和论文解读 | “首次”或能力比较等主张必须独立核对，不能由仓库自述直接支撑 |
| [RCL-Robotics/Awesome-World-Action-Models](https://github.com/RCL-Robotics/Awesome-World-Action-Models) | [arXiv:2609.16074](https://arxiv.org/abs/2609.16074) 的配套仓库 | WAM、VLA、基础方法、数据、指标、benchmark 与组件 | 提供机器可读目录、分类审查和逐篇阅读记录，适合复核身份、角色与分类修正 | 564 条是多类 bibliographic records，不是 564 个核心 WAM，也不能替代原文核验 |
| [world-action-models/awesome-world-action-models](https://github.com/world-action-models/awesome-world-action-models) | [arXiv:2606.20781](https://arxiv.org/abs/2606.20781) 的配套仓库 | Render-and-Decode、Latent-Only、Video-Generation-Free 三类 WAM | 其纳入规则明确要求预测未来进入动作生成、评分、训练或检查，适合校验我们的动作接口边界 | 范围聚焦 action path；不覆盖所有被动视频、模拟器、物理数据或独立安全层 |

## 适合持续追踪的文献库

| 项目 | 特点 | 建议用途 |
|---|---|---|
| [knightnemo/Awesome-World-Models](https://github.com/knightnemo/Awesome-World-Models) | 覆盖游戏、驾驶、具身、科学、latent、评估等多个分支 | 用于高召回发现新论文，再回原始来源筛选 |
| [leofan90/Awesome-World-Models](https://github.com/leofan90/Awesome-World-Models) | 大规模整理视频、具身、VLA、驾驶、数据集与 benchmark | 用于检查七类目录是否存在明显主题漏项 |
| [LMD0311/Awesome-World-Model](https://github.com/LMD0311/Awesome-World-Model) | 长期跟踪自动驾驶、机器人和近期综述 | 用于发现最新条目和专题综述，不直接采用其发表状态标签 |
| [OpenEnvision/Awesome-World-Modeling](https://github.com/OpenEnvision/Awesome-World-Modeling) | 以生成式、表征式和 agentic world modeling 组织大型目录 | 用于术语扩展、历史线索和跨领域检索词发现 |
| [NeuraLiying/Awesome-World-Models](https://github.com/NeuraLiying/Awesome-World-Models) | 340+ 条目，按视频、机器人、3D/4D、物理模拟、效率和评估等主题组织 | 用于季度级高召回补漏，尤其检查 2026 robotics、physics-grounded 与 benchmark 条目 |
| [autonomousdrivingkr/Awesome-Physical-AI](https://github.com/autonomousdrivingkr/Awesome-Physical-AI) | 从感知、表示、世界模型到规划、控制，并列出数据、仿真和工具链 | 用于检查 Physical AI 系统栈中的非论文资源与 sim-to-real 基础设施，不作为世界模型论文边界 |
| [w-xb/awesome-agentic-robotics](https://github.com/w-xb/awesome-agentic-robotics) | 覆盖机器人记忆、规划、世界模型、验证、失败检测与恢复 | 用于第 3、4 部分的邻域检索，尤其发现非世界模型安全层和恢复系统作为边界对照 |
| [NJU3DV-LoongGroup/Embodied-World-Models-Survey](https://github.com/NJU3DV-LoongGroup/Embodied-World-Models-Survey) | 对应 [arXiv:2507.00917](https://arxiv.org/abs/2507.00917)，并列整理物理模拟器、机器人能力和世界模型 | 用于补模拟器物性、传感器、机器人平台与 world-model 训练环境，不直接作为方法效果证据 |

这些列表的作用是“发现”，不是“证明”。进入正文的论文仍应核对题名、作者、版本、发表状态、实验环境、关键图表和可支撑结论。

## 必须纳入定位的非 GitHub 近邻

[Kirchner、Purschke 与 Knoll（2026）](https://doi.org/10.1007/s44163-026-02122-1) 已发表开放获取综述 **A survey of world models for physical AI with uncertainty representation and control**。本轮未检索到明确的配套 GitHub 仓库，但其题目、范围和控制视角与本项目高度重合，不能只列入一般背景。

它以六个设计维度组织方法：状态抽象、时间动力学、不确定性来源与处理、结构先验、观测模态和决策耦合，并强调闭环控制、校准、规划器利用模型误差和 sim-to-real。我们的差异化不应建立在“首次讨论 Physical AI、控制或安全”上，而应落在以下可检验位置：

1. 以“预测目标—动作接口—系统用途—证据类型”作为贯穿全文的统一分析单位。
2. 将模型能力与证据强度绑定，明确区分离线预测、仿真闭环和真实机器人闭环。
3. 单独分析世界模型与 VLA/WAM、推理器和安全防护层的系统关系，而不是把它们合并为同一模型类别。
4. 用可更新的七类文献目录和证据字段支持正文，而不是只提供静态参考文献表。

## 下一轮怎么用

- **正文定位**：优先逐表核对 Kirchner et al.、Hou et al.、Li et al. 与本稿的范围差异，删除无法守住的“更全面”“首次”等表达。
- **文献补漏**：已将 NTUMARS、Li-Zn-H、OpenMOSS 三个仓库与本项目 929 条分类记录做题名和 arXiv ID 去重；结果见[新增候选摘要](literature/EXTERNAL_CANDIDATES.md)和[完整候选 CSV](literature/external_candidates.csv)。
- **更新源分层**：JiahuaDong、NeuraLiying、Awesome-Physical-AI 与 agentic-robotics 暂作为发现源登记；RCL-Robotics、NUS WAM survey 与 NJU3DV 已完成单独增量去重，结果见[增量候选摘要](literature/EXTERNAL_CANDIDATES_DELTA_2026-10-02.md)和[增量候选 CSV](literature/external_candidates_delta_2026-10-02.csv)。359 条是待筛发现池，其中 14 条被至少两个来源共同收录，不能直接并入论文语料或原文证据。
- **图表设计**：参考这些仓库的组织维度，但图表数据只从已核原文提取；优先做“预测空间 × 动作接口 × 验证环境”矩阵。
- **GitHub 维护**：保留当前 CSV 和七类 Markdown 的可检索结构，后续增加“已核验”状态，而不是继续堆叠未经核验的数量。

## 本轮检索记录

| 来源 | 代表查询 | 作用 |
|---|---|---|
| GitHub repository search | `awesome world models`、`world model survey robotics`、`world models embodied survey` | 发现开源论文库与专题列表 |
| Web search | `site:github.com world models embodied AI survey GitHub` | 补足 GitHub 搜索未召回的论文配套仓库 |
| Title search | 具体综述题名 + `GitHub` | 核对论文入口、仓库归属和是否存在配套项目 |
| Repository inspection | README、论文链接、最近提交、许可证 | 区分论文配套仓库、资源列表和个人笔记 |

2026-10-02 的更新扫描另检查了 JiahuaDong、NeuraLiying、Awesome-Physical-AI、agentic-robotics 与 operator22th 五个仓库。前四项因能补充正式综述更新、Physical AI 系统栈或安全恢复邻域而保留；operator22th 清单结构较简、元数据字段不足，暂不加入持续追踪表。

同日的第二次增量扫描新增检查 RCL-Robotics、NUS WAM survey、NJU3DV 模拟器综述库，以及若干个人维护的 WAM/VLA 清单。前三项分别因机器可读分类审查、明确的 action-path 纳入规则和模拟器--世界模型并列视角而保留；个人聚合清单与上述来源高度重叠，暂不单列。随后对三个保留来源完成独立增量去重；新增发现池仍与原冻结候选和正文证据分开统计。

检索盲点：本轮未进行 GitHub 全量 API 翻页、引文网络追踪或逐仓库链接完整性检查；部分 2026 项目仍处于预印本阶段。后续做正式 related-work 比较时，应以出版页面或 arXiv 当前版本为准。
