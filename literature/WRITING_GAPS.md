# 边写边补：文献与内容缺口

更新：2026-10-02；对应正文 v0.2。检索模式为 **rapid-scan（快速定向补充）**，不是穷尽检索或逐篇全文深核。

## 本轮补了什么

正文从 8 条参考文献扩到 111 条。大部分是将协作表已有文献引入正文；下列 62 项在当前 929 条目录中按标题或标识符检索未找到，作为补充记录另列。目录快照仍按 929 条分类记录统计。

| 补充论文与公开入口 | 主分类 | 本轮用途 | 核对深度 / 下一步 |
|---|---|---|---|
| Cosmos Policy [ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/748becc400a57c0e31cfe6a2e7951467-Abstract-Conference.html) | 世界模型与 VLA、规划 | 动作、未来状态和价值的联合建模；直接策略与规划模式 | 已读方法相关正文；正式发表版本元数据已核定 |
| WorldArena [论文](https://arxiv.org/abs/2602.08971) | 评估、安全与 Benchmark | 区分视觉质量和功能用途 | 已核原始论文摘要与评估范围；逐项协议待提取 |
| WorldArena 2.0 [论文](https://arxiv.org/abs/2605.17912v1) | 评估、安全与 Benchmark | 多模态、交互用途和平台扩展 | 已访问正文；各平台实验范围下一轮逐项核对 |
| SafeDreamer [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/ece182f93af26c64187ba3f7dfd4309a-Abstract-Conference.html) | 评估、安全与 Benchmark | 世界模型中的成本约束与安全规划 | 已核成本定义、主实验、消融和作者局限；见核验批次 02 |
| Recovery RL [RA-L 2021](https://doi.org/10.1109/LRA.2021.3070252) | 评估、安全与 Benchmark | 恢复策略作为互补安全机制 | 已核正式版本、方法与实验范围；不将其归为生成式 WM |
| Control Barrier Functions: Theory and Applications [ECC 2019](https://doi.org/10.23919/ECC.2019.8796030) | 世界模型基础与控制；交叉安全 | 解释形式保证与经验安全结果的区别 | 已核正式版本、来源与范围；具体定理假设和与学习模型的连接待补 |
| Do World Models Make Better Robots? [综述](https://arxiv.org/abs/2609.29669v1) | 评估、安全与 Benchmark | 近期综述定位与评估组织方式 | 已查看正文与比较表；不照搬其文献统计与优先性主张 |
| Safety Guardrails for LLM-Enabled Robots [论文](https://arxiv.org/abs/2503.07885v2) | 评估、安全与 Benchmark | 语义世界模型、LTL 计划约束与越狱攻击 | 已核实体与仿真实验、试验分母和作者局限；见核验批次 03 |
| Verifiable Foundation Models for Robot Safety [论文](https://arxiv.org/abs/2606.23754v1) | 评估、安全与 Benchmark | 可验证低维安全模块、选择性护盾与实体迁移 | 已核 18 回合实体试验、认证域和传感器前提；见核验批次 03 |
| Rethinking World Models for Safety-Critical Embodied Systems [观点](https://arxiv.org/abs/2609.03774v2) | 评估、安全与 Benchmark | 2026 风险知情世界模型研究议程 | 已核全文；无自身实验，不参与方法效果比较 |
| TouchWorld [论文](https://arxiv.org/abs/2607.07287v2) | 结构化物理与多模态 | 触觉子目标预测与快速残差控制的分层接口 | 已核实体任务、预测表、消融和作者局限；见核验批次 04 |
| DexTouch-WM [论文](https://arxiv.org/abs/2609.20649v2) | 结构化物理与多模态；数据与跨本体 | 人类触觉与动作对齐、策略评估代理和合成数据 | 已核数据规模、真实评价和混合下游结果；见核验批次 04 |
| ParticleFormer [CoRL 2025](https://proceedings.mlr.press/v305/huang25c.html) | 结构化物理与多模态 | 点云多材料动力学与实体 MPPI | 已核正式版本、任务、动作接口和三次实体 rollout 限制；见核验批次 04 |
| MVISTA-4D [ICML 2026](https://proceedings.mlr.press/v306/wang26jw.html) | 结构化物理与多模态 | 多视角 RGB-D 未来与测试时动作反演 | 已核正式版本、消融、实体对比和推理时延；见核验批次 04 |
| Navigation World Models [CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/html/Bar_Navigation_World_Models_CVPR_2025_paper.html) | 世界模型与 VLA、规划 | 显式未来视图、CEM 规划与候选策略重排 | 已核正式版本、离线规划协议和失败边界；见核验批次 06 |
| NavWAM [论文](https://arxiv.org/abs/2606.13494v1) | 世界模型与 VLA、规划 | 联合未来--价值--动作预测与实体闭环 | 已核 24 个实体 episode、离线预测头消融和失败标签；预印本，见核验批次 06 |
| Failure-Aware RL [论文](https://arxiv.org/abs/2601.07821v1) | 世界模型与 VLA、规划；评估与安全 | 短视风险预测后切换恢复策略 | 已核三个 Franka 任务、50 episode/任务、仿真 critic 消融和失败指标口径；预印本，见核验批次 07 |
| Foresight [论文](https://arxiv.org/abs/2606.23085v1) | 评估、安全与 Benchmark | 动作条件世界模型 latent 上的长时失败检测与 conformal 阈值 | 已核实体 ROC-AUC、跨策略迁移、校准假设和时延；预印本，见核验批次 08 |
| KnowNo [CoRL 2023](https://proceedings.mlr.press/v229/ren23a.html) | 评估、安全与 Benchmark；边界对照 | conformal prediction set 到选择性求助的决策接口 | 已核实体试验、help rate 与规划假设；非世界模型，见核验批次 08 |
| CoFineLLM [L4DC 2026](https://proceedings.mlr.press/v331/wang26c.html) | 评估、安全与 Benchmark；边界对照 | 同时优化覆盖、预测集大小与求助率 | 已核 PMLR 正式摘要；硬件 OOD 详细协议仍待全文提取，见核验批次 08 |
| ThriftyDAgger [CoRL 2021](https://proceedings.mlr.press/v164/hoque22a.html) | 评估、安全与 Benchmark；边界对照 | 人工干预频率、持续时间和上下文切换成本 | 已核单任务实体分母及人工动作数；非世界模型，见核验批次 08 |
| Hi-WM [论文](https://arxiv.org/abs/2604.21741v2) | 世界模型与 VLA、规划；数据与跨本体 | 在可交互世界模型内采集人工纠正分支用于实体策略后训练 | 已核三任务、两策略和基线；实体试验分母缺失，预印本，见核验批次 09 |
| WorldSync / WorldEcho [论文](https://arxiv.org/abs/2608.24885v1) | 视觉与视频世界模型；评估与 Benchmark | off-expert 动作跟随、视觉完整性和干预效应对齐 | 已核 50 任务协议、仿真消融和单任务实体策略改进；预印本，见核验批次 09 |
| FoMo-FD [论文](https://arxiv.org/abs/2607.27511v1) | 评估、安全与 Benchmark；结构化物理与多模态 | 手术操作中的动作条件 latent 失败检测 | 已核固定校准阈值、实体失败模式分母和吞吐；仅离线检测，预印本，见核验批次 09 |
| Dream2Fix [论文](https://arxiv.org/abs/2603.13528v1) | 世界模型与 VLA、规划；数据与跨本体 | 世界模型合成失败--纠正数据及实体闭环执行 | 已核两个 50 次实体设置、指标口径和单平台边界；预印本，见核验批次 10 |
| REBOOT [论文](https://arxiv.org/abs/2609.22591v1) | 数据、模拟与跨本体；评估与安全 | 阶段级真实失败与人工恢复数据、有效续接状态定义 | 已核 2,160 条轨迹、18 任务和单操作者边界；未评估自主恢复，见核验批次 10 |
| VLA-FixBench [ICML 2026](https://proceedings.mlr.press/v306/yan26r.html) | 评估、安全与 Benchmark；边界对照 | 停止、回滚、三维纠正和误触发代价 | 已核正式论文；35 点增益为人工上界，实体分母未明，见核验批次 10 |
| AgentChord [论文](https://arxiv.org/abs/2605.11951v1) | 世界模型与 VLA、规划；边界对照 | 预编译恢复分支、状态修复后重新接入原任务 | 已核六个实体任务、20 次/任务和预设故障边界；非世界模型，见核验批次 10 |
| VLAW [ICML 2026](https://proceedings.mlr.press/v306/guo26i.html) | 世界模型与 VLA、规划；数据与跨本体 | 实体失败 rollout 校准世界模型，再以筛选后的合成 rollout 更新 VLA | 已核五类实体任务、两轮更新和等实体 rollout 对照；见核验批次 09 |
| Task-Sufficient World Models [ICML 2026](https://proceedings.mlr.press/v306/feng26aa.html) | 世界模型基础与控制；Latent 与预测表示 | 主动探测与结构化表示共同学习任务充分 latent | 已核四套仿真基准、5-seed 结果、表示探测和组件消融；无实体机器人验证，见核验批次 09 |
| V-JEPA Policy [论文](https://arxiv.org/abs/2609.37250v1) | Latent 与预测表示；世界模型与 VLA、规划 | 冻结预测视觉表示、future-latent predictor 与 action expert 的直接耦合 | 已核 future-loss 匹配消融、DROID predictor 预训练和两项实体任务；单 seed、额外上游预算和非动作条件预测边界见核验批次 19 |
| Latent Reasoning VLA [ICML 2026](https://proceedings.mlr.press/v306/bai26h.html) | 世界模型与 VLA、规划；边界对照 | 当前观测与指令预测 future latent，再由逆动力学监督和动作头生成动作 | 已核全文、仿真消融及四类实体任务分母；无候选动作条件的前向接口，保留为边界对照 |
| DynBridge [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_DynBridge_Bridging_Imagination_and_Control_through_Interaction_Dynamics_for_Robot_CVPR_2026_paper.html) | 世界模型与 VLA、规划；边界对照 | 未来轨迹重建与动作模仿共同学习交互 latent | 已核全文、三种仿真协议和五项实体任务；10 次实体试验、无候选动作查询，见核验批次 11 |
| MM-ACT [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.html) | 世界模型与 VLA、规划；边界对照 | 文本、未来图像和动作共享上下文联合监督 | 已核全文、仿真消融和三项实体任务；实体主比较未隔离预测目标，见核验批次 11 |
| Dexterous World Models [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html) | 视觉与视频世界模型；规划接口 | 手部轨迹条件的视觉后果与候选排序 | 已核 144 样本 benchmark 和定性动作排序；无执行试验，见核验批次 12 |
| Physical Object Understanding with a Physically Controllable World Model [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Venkatesh_Physical_Object_Understanding_with_a_Physically_Controllable_World_Model_CVPR_2026_paper.html) | 结构化物理与多模态；边界对照 | 视觉代理干预、对象与支撑关系发现 | 已核训练规模和结构理解结果；光流 poke 不是机器人动作，见核验批次 12 |
| PhysInOne [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_PhysInOne_Visual_Physics_Learning_and_Reasoning_in_One_Suite_CVPR_2026_paper.html) | 数据、模拟与跨本体 | 大规模合成物理视频、密集标签与资产隔离划分 | 已核数据协议和混合微调结果；无机器人动作或真实验证，见核验批次 12 |
| GeoWorld [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_GeoWorld_Geometric_World_Models_CVPR_2026_paper.html) | Latent 与预测表示；规划边界 | 双曲 latent 与教学视频程序步骤规划 | 已核 CrossTask/COIN 匹配比较；不等于机器人动作执行，见核验批次 12 |
| DriveDreamer-Policy [论文](https://arxiv.org/abs/2604.01765v1) | 世界模型与 VLA、规划；自动驾驶 | 深度、未来视频和轨迹的有序联合监督 | 已核 NAVSIM v1/v2、组件消融与伪深度边界；无物理车辆闭环，见核验批次 13 |
| VTAM [论文](https://arxiv.org/abs/2603.23481v1) | 结构化物理与多模态；世界模型与 VLA、规划 | 视觉--触觉--动作联合生成与接触控制 | 已核 80 次/模型实体比较和十次消融；预测质量仅定性，见核验批次 13 |
| JOPAT [论文](https://arxiv.org/abs/2605.23856v1) | 世界模型与 VLA、规划；结构化物理 | future latent、二维点轨迹、可见性和动作联合去噪 | 已核 LIBERO 匹配消融和四任务各十次实体试验；点跟踪监督及小样本受限，见核验批次 14 |
| VAMPO [论文](https://arxiv.org/abs/2603.19370v1) | 世界模型与 VLA、规划 | 用专家未来 latent 奖励后训练视频预测器 | 已核 predictor-only 与动作重适配分解；实体分母缺失、检查点波动，见核验批次 14 |
| Audio-WM [论文](https://arxiv.org/abs/2512.08405v1) | 结构化物理与多模态 | 未来音频作为操作策略的前瞻输入 | 已核 30 次实体任务和仿真 lookahead；非动作条件且无匹配实体消融，见核验批次 14 |
| DexWM [论文](https://arxiv.org/abs/2512.13644v2) | 世界模型与 VLA、规划；数据与跨本体 | 人类手部视频预训练、关键点动作和 latent CEM | 已核仿真比较及 12 次实体抓取；仍使用四小时模拟机器人适配，见核验批次 14 |
| DriveWAM [论文](https://arxiv.org/abs/2605.28544v1) | 世界模型与 VLA、规划；自动驾驶 | 生成未来 latent 条件动作和选择性 KV memory | 已核 NAVSIM、PhysicalAI-AV 与缓存消融；作者筛选测试集、无车辆闭环，见核验批次 15 |
| NoiseGate [论文](https://arxiv.org/abs/2605.07794v1) | 世界模型与 VLA、规划 | 学习 per-latent 去噪时间作为动作信息门控 | 已核 50 任务主比较与 15 任务消融；单 seed、仿真 rollout 后训练，见核验批次 15 |
| DAWN [论文](https://arxiv.org/abs/2605.11550v1) | 世界模型与 VLA、规划；自动驾驶 | 短 latent rollout 与动作假设递归双向修正 | 已核 NAVSIM/nuScenes、双向交互和 rollout 时延消融；无真实车辆，见核验批次 15 |
| WALL-WM [论文](https://arxiv.org/abs/2606.01955v2) | 世界模型与 VLA、规划；数据与跨本体 | 事件级视频--动作预训练和可变长执行 | 已核实体 Task Progress 与 RoboTwin；关键消融同时改变多视角模块，实体分母缺失，见核验批次 15 |
| ADriver-I [论文](https://arxiv.org/abs/2311.13549v1) | 世界模型与 VLA、规划；自动驾驶 | 早期 interleaved 控制--视频递归生成接口 | 已核控制和视频指标；持续驾驶仅模型内定性递归，无真实闭环，见核验批次 15 |
| WorldLens [CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/papers/Liang_WorldLens_Full-Spectrum_Evaluations_of_Driving_World_Models_in_Real_World_CVPR_2026_paper.pdf) | 评估、安全与 Benchmark；自动驾驶 | 生成、重建、动作跟随、下游任务和人类偏好联合评价 | 已核正式版本与扩展稿；闭环为五条生成模拟序列，无道路车辆，见核验批次 16 |
| ManipArena [论文](https://arxiv.org/abs/2603.28545v2) | 评估、安全与 Benchmark；数据与跨本体 | 分层 shift、部分完成度和实体策略比较 | 已核至少 1,050 次实体桌面试验；每任务十次且训练配方影响排序，见核验批次 16 |
| Beyond Task Success [论文](https://arxiv.org/abs/2609.07126v1) | 评估、安全与 Benchmark | 表示、预测、规划和结果的 stage-wise sensing degradation 诊断 | 已核配对 50 个仿真任务；主结果置信区间均含零，见核验批次 16 |
| Test-Time Scaling for WAMs [论文](https://arxiv.org/abs/2607.17454v1) | 世界模型与 VLA、规划；评估与 Benchmark | 跨视角几何候选筛选和选择性额外采样 | 已核三套仿真 benchmark、四 seed 和延迟；无实体机器人，见核验批次 16 |
| Trusted Imagination Attack [论文](https://arxiv.org/abs/2606.22966v1) | 评估、安全与 Benchmark | 被 verifier 或 planner 信任的预测 latent 完整性 | 已核白盒攻击、reactive null 和单任务闭环 MPC；不能外推为普遍脆弱，见核验批次 16 |
| WAM--VLA Robustness Study [论文](https://arxiv.org/abs/2603.22078v5) | 评估、安全与 Benchmark；世界模型与 VLA、规划 | 七类扰动下的模型族轮廓与推理时延 | 已核 RoboTwin 2.0-Plus/LIBERO-Plus；训练数据和来源异配，不做因果排名，见核验批次 16 |
| TacPAC [论文](https://arxiv.org/abs/2609.05266v1) | 结构化物理与多模态；世界模型与 VLA、规划 | 预测触觉缓存驱动动作块内实时纠正 | 已核五任务、每方法任务 20 次实体试验和延迟；单平台/传感器，见核验批次 17 |
| DreamAvoid [论文](https://arxiv.org/abs/2605.11750v2) | 世界模型与 VLA、规划；评估、安全与 Benchmark | 关键阶段触发、未来视频候选排序与实体动作替换 | 已核四任务、160 次/方法和失败审计；预测时暂停高层执行，见核验批次 17 |
| WHIRL [论文](https://arxiv.org/abs/2609.06009v1) | 世界模型与 VLA、规划；评估、安全与 Benchmark | 用实体接管标签训练前瞻 intervention head 并进行 actor 风险整形 | 已核五项实体任务与组件对照；单 seed、单操作者、任务内随机化，见核验批次 17 |
| Sim-to-real WAM [论文](https://arxiv.org/abs/2606.31101v1) | 数据、模拟与跨本体；世界模型与 VLA、规划 | 纯仿真示范与域随机化后的零样本实体部署 | 已核四任务、每任务 10 次；35% 平均成功且无匹配架构消融，见核验批次 18 |
| Selective Cross-View Consistency [论文](https://arxiv.org/abs/2608.21402v1) | 世界模型与 VLA、规划；评估、安全与 Benchmark | 区分 WAM 输出的视角不变量与协变量并测试相机外推 | 已核匹配对照、两 seed 和置信区间；仅仿真且复合极端视角可退化，见核验批次 18 |
| Temporal Ratio [论文](https://arxiv.org/abs/2607.08127v1) | Latent 与预测表示；世界模型与 VLA、规划 | 测量动作对预测未来的依赖并按任务阶段门控 guidance | 已核 LIBERO 三 seed 与实体 60 次/方法；单平台且完整方法改变多项组件，见核验批次 18 |
| Zero-WAM [论文](https://arxiv.org/abs/2608.26103v2) | 数据、模拟与跨本体；世界模型与 VLA、规划 | 人类视频作为未见任务配置的上下文接口 | 已核七项仿真任务与三类实体任务；基线提示模态不同且仍需平台适配数据，见核验批次 18 |

DreamZero 并不是库中缺失：原目录 `S06-0115` 使用正式标题 **World Action Models are Zero-shot Policies** [论文](https://arxiv.org/abs/2602.15922)。本轮只补正文引用，不另计一篇。两篇综述 `2605.00080`、`2609.16074` 也已在原目录中。

ContactWorld 也不是新增条目：原目录 `S06-0119` 已收录，本轮只将题名、作者和版本更新到 arXiv v3，并在正文按接触表示与预测规划讨论。

导航与驾驶批次的 5 篇也都来自现有目录，没有增加前五批形成的 14 项补充记录。核验后已更正两个关键身份：目录 `S07-0120` 的 `2408.14197` 是 AAAI 2025 的 Drive-OccWorld，不是 Drive-WM；`S06-0109` 的 NavForesee 当前按 arXiv:2512.01550v2 预印本记录，未沿用原表的 CVPR 2026 正式发表标注。

闭环导航批次中，DreamerNav 与 NavThinker 已在现有目录；NWM 与 NavWAM 未检出，因此补充记录由 14 项增至 16 项。实体证据已经不再是完全空白，但仍集中在受控演示或单平台小样本。

记忆与恢复批次中，Mem-World、WorldScape Policy 2.0、ViFailback 与 LIBERO-Recover 均在现有目录；Failure-Aware RL 未检出，因此补充记录增至 17 项。该批次闭合了机制分类，但跨平台实体状态恢复仍是缺口。

风险校准与干预代价批次中的 Foresight、KnowNo、CoFineLLM 与 ThriftyDAgger 均未按完整题名或标识符检出，因此补充记录增至 21 项。该批次补齐了检测、求助和人工负担的评估接口，但尚未出现同一真实机器人协议内从世界模型报警到在线干预、事故后果和恢复完成的完整证据链。

实体在线学习与虚拟纠正批次中，WorldSample 对应原目录 `S06-0121`；Hi-WM、WorldSync 与 FoMo-FD 未检出，因此补充记录增至 24 项。截至该批次，这些工作补齐了真实在线 RL、模型内人工纠正、off-expert 动作跟随和手术失败检测，但未改变上一批次的核心缺口：只有 FARL 接近从世界模型风险预测到实体动作替换，且仍缺事故严重度、报警提前量与失败后任务恢复。

失败后恢复批次中的 Dream2Fix、REBOOT、VLA-FixBench 与 AgentChord 均未检出，因此补充记录增至 28 项。Dream2Fix 补入世界模型合成失败数据到实体纠正的闭环，REBOOT 给出有效续接状态与真实恢复示范，VLA-FixBench 和 AgentChord 提供非世界模型的诊断回滚与任务续接边界。核心缺口收窄为：跨平台、跨操作者、开放故障且同时报告校准报警、事故后果和最终任务完成的世界模型恢复证据。

ICML 2026 PMLR 卷的定向检查新增 VLAW、Task-Sufficient World Models 与 Latent Reasoning VLA 三项，补充记录增至 31 项。三项均已完成原文级核验并进入正文：前两项分别提供实体模型--策略共进化和仿真主动探索--结构化表示证据；Latent Reasoning VLA 的 future latent 不接收候选动作，作为预测辅助策略的边界对照，不计为核心世界模型。

CVPR 2026 定向检查从 11 个官方页面候选中全文核验 8 篇。Motus 已在原目录中，不另计；DynBridge、MM-ACT、DWM、PhyWM、PhysInOne 与 GeoWorld 进入正文或补充清单，使目录外补充记录增至 37 项。ModularAgent 也完成核验，但因仅覆盖 DMC 仿真且未承担当前正文的独立论断，只保留在证据批次 12。该轮把联合生成、视觉代理干预、合成数据、程序步骤规划和可执行机器人控制分开记录。

R22 第一队列的 DriveDreamer-Policy、VTAM、JOPAT、VAMPO、Audio-WM 与 DexWM 均未在目录中命中，补充记录由 37 项增至 43 项。它们进入正文时分别按训练时预测监督、触觉联合生成、结构化 future state、预测器后训练、外生音频前瞻和人类视频迁移讨论，不合并成 WAM 性能排名。

R22 第二队列的 DriveWAM、NoiseGate、DAWN、WALL-WM 与 ADriver-I 也均未在目录中命中，补充记录增至 48 项。五篇完成全文核验并按不同推理接口进入正文；当前仍无任何一篇同时提供多平台真实闭环、匹配的预测机制消融和可复算不确定性。

R27 从 359 条增量候选中按评估、安全、鲁棒性与故障诊断词筛出 23 个题名，并全文核验其中 6 篇，补充记录增至 54 项。WorldLens 是正式 CVPR 2026 论文，其余五篇按当前预印本版本处理。该轮补齐了实体 benchmark、阶段级退化诊断、预测候选筛选和预测完整性攻击面，但没有闭合真实机器人在线干预、跨平台复现或开放故障恢复证据链。

R28 定向全文核验 TacPAC、DreamAvoid、WHIRL 与 CoWAM。前三篇进入正文，补充记录增至 57 项；CoWAM 因只有仿真而保留为 selector 评估边界。该轮补入动作块内实时纠正、关键阶段实体候选重排和接管风险学习，但三项实体证据仍各自限于单一平台，没有跨操作者或真实分布偏移复现。

R29 定向全文核验 sim-to-real WAM、SCVC、Temporal Ratio 与 Zero-WAM，补充记录增至 61 项。该轮把训练环境、相机、对象--目标组合和测试时任务提示拆成四种泛化契约；仍没有同一 WAM 在多个实体平台或操作者间按统一协议复现。

R31 在 V-JEPA 2 正式版本核查中发现并全文核验 V-JEPA Policy，补充记录增至 62 项。该工作填补预测视觉 latent 与 action expert 耦合的直接消融，但 predictor 不读取候选动作，且额外 DROID 预训练不是同总预算比较。

## 接下来优先补哪些

“缺”表示当前稿件的证据尚不充分，不表示这个领域没有论文。检索词是下一轮入口，不是已完成的检索。

| 对应七类文献 | 当前正文已有支撑 | 还缺的关键内容 | 下一轮检索入口 | 优先级 |
|---|---|---|---|---|
| 世界模型基础与控制 | PlaNet、PETS、Dreamer、TD-MPC2、MBPO | 状态估计、部分可观测性与经典控制的联系；最新 latent-control 进展 | `world model belief state partial observability`; `latent model predictive control 2026` | 中 |
| 视觉与视频世界模型 | UniPi、UniSim、DreamZero、Cosmos Policy | 2026 大规模交互模拟；长时滚动、动作一致性与失败案例 | `action-conditioned video world model interactive simulator 2026`; `long horizon rollout failure` | 高 |
| Latent 与预测表示 | Dreamer、TD-MPC2、V-JEPA 2 | 新预测目标的系统比较；2026 JEPA 与动作表示、策略耦合方法 | `predictive representation robot action JEPA 2026`; `latent world model policy ablation` | 高 |
| 结构化物理与多模态 | GNS、TesserAct、OmniVTA、ContactWorld、TouchWorld、DexTouch-WM、ParticleFormer、MVISTA-4D、TacPAC | 长时组合接触、跨触觉硬件迁移、力觉校准与场景无关的形变动力学 | `compositional contact world model`; `cross sensor tactile world model`; `force calibrated predictive control` | 高 |
| 数据、模拟与跨本体 | DROID、Open X-Embodiment、UniSim、REBOOT | 人类第一视角数据、跨本体动作对齐；恢复数据的跨操作者采集与训练测试重叠核查 | `egocentric video robot action alignment`; `multi-operator robot recovery dataset`; `cross embodiment dynamics` | 高 |
| 世界模型与 VLA、规划 | 规划、想象学习、联合模型、Astra 接口；WorldSample、VLAW、Hi-WM、WorldSync、Dream2Fix、WHIRL、DreamAvoid；导航/驾驶闭环；Mem-World、WorldScape 2.0 与 FARL | 跨平台实体复现；开放故障后的状态恢复；虚拟纠正数据与实体纠正数据的等预算比较 | `cross-platform physical robot recovery world model`; `virtual intervention versus physical correction robot`; `world model online recovery ablation` | 最高 |
| 评估、安全与 Benchmark | WorldArena 系列、SafeDreamer、FARL、Foresight、FoMo-FD、DreamAvoid、WHIRL、VLA-FixBench、AgentChord、ViFailback 与 LIBERO-Recover | **仍缺完整世界模型实体证据链**：带 abstention 的校准触发、跨操作者/平台外推、真实分布偏移、事故严重度、检测提前量和开放故障恢复 | `world model calibrated abstention real robot`; `failure alarm lead time incident severity`; `cross-platform calibrated robot recovery` | 最高 |

下一轮优先补每个薄弱方向 2–3 篇能够真正进入比较表的代表工作。满足“不同机制、明确预测量、明确动作接口、可定位实验”的需要后再扩量，不以凑篇数代替覆盖。

## 表格参考与实现

本轮新增 7 表，加上已有 Astra 表，共 8 表：近期综述定位、数据资源、预测空间、策略融合、导航与驾驶接口、Astra 来源、评估协议、安全机制。均为可编辑 LaTeX 表，不是截图。

- Lu 等 [2026 综述](https://arxiv.org/html/2609.16074v1)：参考按类别分组的方法表、指标与资源分表的组织方式。
- Hou 等 [2026 综述](https://arxiv.org/html/2605.00080v1)：参考在架构比较中显式记录预测与动作的连接。
- Jena 等 [2026 综述](https://arxiv.org/html/2609.29669v1)：参考综述定位与评估协议比较表的用途。

已查看上述 HTML 排版表格，并读到 Lu 等源包的章节 LaTeX 片段。完整源码下载超时，因此没有声称完整检查或复用其表格源码。我们的实现沿用仓库已有 `booktabs`、`tabularx`，使用分组行、自动换行和少量横线；未复制原表数据、覆盖勾叉或能力排名。

## 本轮检索与证据边界

检索日期：2026-10-01。以现有目录为起点，定向搜索后回到 arXiv、PMLR、NeurIPS/ICLR 会议记录及作者项目页面。代表查询：

1. `world models physical AI survey 2026 arxiv robot world action survey`
2. `world models survey 2026 embodied intelligence taxonomy evaluation survey latex`
3. `DreamZero World Action Models are Zero shot Policies 2026 arxiv`
4. `Cosmos Policy fine tuning video models visuomotor control 2026 arxiv`
5. `WorldArena 2026 benchmark embodied world models arxiv`
6. `SafeDreamer world models safety constraints ICLR 2024 paper`
7. `site.proceedings.mlr.press Recovery RL Safe Reinforcement Learning Learned Recovery Zones`
8. `site.arxiv.org control barrier functions theory applications Ames 2019`

现有目录与论文正文是两层记录：库里有论文不等于已读、已核或已在正文引用。本轮补的是方法级概述与文献定位，没有新增跨论文成功率排名，也没有宣称复现。部分早期论文通过 arXiv 可读版本引用，正式出版信息、完整作者列表与版本统一留待第二轮。

## 第一轮自查

| 稿件判断 | 支撑与状态 |
|---|---|
| 在线规划与想象训练是不同的模型使用位置 | PETS/PlaNet 与 Dreamer/MBPO 的方法描述支持；不推导谁普遍更优 |
| 预测与动作可以联合建模 | DreamZero、Cosmos Policy 支持方法级描述；不据此断言因果物理理解 |
| 视觉质量与功能评估应分别记录 | WorldArena 系列提供相关评估设计；我们的比较框架是综述组织选择 |
| 成本约束、恢复与形式保证是不同安全机制 | SafeDreamer、CPO、Recovery RL、CBF 提供各自背景；不混写为统一安全保证 |
| 触觉、导航、驾驶和分布外安全已被充分覆盖 | **不成立**；已有小规模实体闭环、校准式失败检测、预测式避险和外部纠正，但检测到在线干预的因果链、跨平台状态恢复、长时组合接触和真实分布偏移仍是缺口 |

自查结论：定位方面不声称“首个”或“最全面”；写作方面四部分已连通；实验支撑仅到方法概述和已有来源；评估覆盖仍有明确空缺；机制区分保留预测、策略、控制和防护的边界。下一轮再压缩重复论述、增加具体技术细节，并将正文里的写作阶段说明移到协作记录。
