# 原文核验批次 09：实体在线学习、虚拟人工纠正与动作跟随

核验日期：2026-10-02。检索模式为 **rapid-scan（快速定向补充）**。问题限定为：世界模型如何参与真实机器人在线学习或纠正数据收集，模型是否能跟随 off-expert 动作，以及失败检测是否真正触发实体干预。本批次不把训练阶段的人工纠正写成部署阶段的安全接管，也不把离线检测写成事故减少。

## 结论概览

| 论文 | 发表状态 | 机制位置 | 可支撑的窄结论 |
|---|---|---|---|
| [WorldSample](https://arxiv.org/abs/2607.02431v1) | 2026 arXiv v1 预印本 | 真实在线 RL 中的反事实合成转移与选择性调度 | 在单任务、固定场景分布内，真实 rollout 可持续校准世界模型，并用筛选后的合成转移减少在线训练步数。 |
| [Hi-WM](https://arxiv.org/abs/2604.21741v2) | 2026 arXiv v2 预印本 | 人在世界模型中纠正、回滚和分支 | 虚拟纠正轨迹可以用于实体策略后训练；它不是运行时物理接管。 |
| [WorldSync / WorldEcho](https://arxiv.org/abs/2608.24885v1) | 2026 arXiv v1 预印本 | off-expert 动作跟随诊断与 intervention-effect 监督 | 专家动作上的生成质量不能代表任意可行动作下的 action faithfulness。 |
| [FoMo-FD](https://arxiv.org/abs/2607.27511v1) | 2026 arXiv v1 预印本 | 手术操作中的动作条件世界模型失败检测 | 固定 conformal 阈值可在实体 dVRK 记录上得到低误报的离线检测结果；尚无在线干预。 |

WorldSample 已在现有 929 条目录中；其余三篇未按完整题名或 arXiv ID 检出，作为正文补充来源单列。

## 1. WorldSample

**身份与机制。** 2026 arXiv 预印本。系统从真实机器人在线 rollout 分支局部反事实动作序列，由经任务适配的 Cosmos-Predict2.5 预测合成转移并经 reward model 标注。Policy-Paced Learning 使用 Q-aware sample selection 控制合成样本组成，并用不确定性调度控制其进入 RL 的比例。

**主要证据与论文结论。** 在单台 Galaxea A1X 的推动、插入、分类、抓放和装配任务上，每任务从 20 条人工示范开始。表 1 报告 WorldSample 平均成功率 82%、在线训练步数 23K、训练时间 64 分钟；HIL-SERL 分别为 56%、56K 和 83 分钟。插入任务消融中，完整系统为 95% 成功、24% intervention rate、10K 步；移除调度后为 61%、43%、18K 步，移除 Q-selection 后为 76%、42%、12K 步。

**可支撑判断。** 该工作支持“世界模型生成的数据需要按策略状态和不确定性选择性使用”，并提供真实在线 RL 与世界模型持续适配的闭环案例。

**局限与待核验。** 论文没有报告每个成功率对应的独立评测 episode 数或方差。完整系统同时改变世界模型在线适配、reward labeling、样本选择和调度，不能把全部增益归因于预测器。主比较的停止规则是各基线训练到收敛，WorldSample 达到收敛或基线 wall-clock 上限，资源口径并非完全单变量。作者局限明确限定在单任务和相对固定场景分布。表 1 附近对 59% 与 23% 所对应资源的文字解释存在歧义，因此本综述只引用原始步数与时间。证据位置：第 3、4.1--4.3、6 节，表 1--2，附录 A。

## 2. Hi-WM

**身份与机制。** 2026 arXiv 预印本。策略在动作条件世界模型中闭环执行；人工在模型 rollout 偏离时接管，缓存并回滚到失败前状态，再采集多个纠正分支。纠正段与原始真实示范合并用于策略后训练。

**主要证据与论文结论。** 单台双臂 YAM-Ultra 上评估 Fold Towel、Push-T 和 Route Rope，覆盖 Diffusion Policy 与 $\pi_0$ 两个策略。表 2 的六个策略--任务组合中，Hi-WM 均高于 base 和无人工纠正的 WM-Closed-Loop；论文报告相对 base 平均提高 37.9 个百分点，相对 WM-Closed-Loop 提高 19.0 个百分点。

**可支撑判断。** 该工作支持“人工可在可交互世界模型中围绕失败状态采集纠正分支，并将其作为实体策略后训练数据”。

**局限与待核验。** 论文未给表 2 实体成功率的试验次数、方差或置信区间。人工决定何时和如何纠正，因此完整收益包含人的状态识别与控制能力。世界模型与实体成功相关系数 $r=0.953$ 的样本仅来自有限策略--任务组合。成本分析最高声称近 4,500 万美元节省，依赖设备部署、人工、场地和推理成本假设，本轮不将该投影写入正文。该方法不是自动报警，也没有在实体执行时接管。证据位置：第 3.1--3.5、4.1--4.5 节，表 2，图 6--7。

## 3. WorldSync 与 WorldEcho

**身份与机制。** 2026 arXiv 预印本。WorldEcho 在专家动作之外构造局部扰动、跨状态重放、策略 rollout 和广覆盖可行动作，并同时测量视觉完整性和 SE(3) 末端轨迹对齐。WorldSync 通过扩大动作覆盖、Action-Forcing Expert 和 intervention-effect supervision 改善动作跟随。

**主要证据与论文结论。** 六种世界模型在 off-expert 查询下，raw NDTW 增加 0.010--0.043 m，视觉失败率增加 6.3--28.1 个百分点。单个实体叠杯任务的两轮策略改进中，WorldSync 与 CtrlWorld 初始成功率均为 48%，最终分别为 68% 和 56%。作者据此认为更强的动作跟随可使世界模型成为更可靠的策略改进环境。

**可支撑判断。** 该工作支持“专家示范分布上的视觉质量不足以验证动作条件世界模型；off-expert 动作覆盖和干预效应应单独评测”。

**局限与待核验。** 实体结果只有一个任务，论文未报告每轮成功率的试验分母。完整 WorldSync 与实体 CtrlWorld 比较不仅改变 intervention-effect supervision，还改变动作覆盖和训练配置；组件消融只在四个 RoboTwin 仿真任务上完成。WorldEcho 的完整性门控依赖分割和评估器，也不是危险后果或安全校准指标。证据位置：第 3.3--3.4、4.2--4.5、5 节，表 1--2，图 5--6。

## 4. FoMo-FD

**身份与机制。** 2026 arXiv 预印本。模型在 DINOv2 latent 上学习动作条件 flow matching，通过把观察到的窗口终点逆向传输到高斯基空间构造 nonconformity score；每任务用成功轨迹做 conformal calibration。

**主要证据与论文结论。** 两个仿真任务和两个实体 dVRK 任务共包含 320 个失败、80 个 held-out 成功 rollout。每任务使用 19 个成功 rollout 校准并固定 $\alpha=0.05$；实体每种失败模式 10 个 rollout，每任务另有 20 个 held-out 成功。聚合结果中，腕部视角 WM-NC 的 failure detection rate 为 96.6%，false-alarm rate 为 1.3%。端到端评分速度为 13.98 Hz，实验控制回路为 10 Hz。

**可支撑判断。** 该工作支持“动作条件 latent dynamics 可在接触密集的手术操作记录上提供经固定阈值校准的失败信号”，并给出明确的实体失败模式分母。

**局限与待核验。** 所有检测均在已记录 rollout 上离线完成，论文明确未连接在线干预。96.6%/1.3% 是仿真与实体四任务的聚合值，不能当作每个实体任务的独立结果。失败模式是预先构造的 20 类，不能代表开放部署中的未知风险；低误报依赖当前校准协议和分布。评分速度超过控制频率只证明计算吞吐可行，不证明报警提前量或干预效果。证据位置：第 III、IV、V、VI 节，表 I，图 3--5。

## 跨论文判断与筛选结论

1. WorldSample 的 intervention rate 来自真实在线 RL 的人类纠正，但世界模型负责训练数据扩展，不负责触发接管。
2. Hi-WM 的人工接管发生在世界模型内部，实体机器人只用于评估后训练策略；它降低硬件占用的逻辑与部署时安全接管不同。
3. WorldSync 解决预测是否服从动作，FoMo-FD 解决执行是否偏离成功动力学；两者都没有展示报警后实体行为如何改变。
4. 本轮严格门槛下没有发现比 FARL 更完整的“世界模型风险预测--在线动作替换--实体训练结果”新证据。当前仍缺同一协议内的检测提前量、在线干预、事故严重度、人工负担和任务恢复终点。

## 检索与证据边界

检索词包括 `world model online intervention failure detection real robot`、`action-conditioned world model safety monitor online intervention physical robot`、`robot world model failure alarm intervention real-world manipulation recovery` 和 `robot failure prediction intervention real robot world model`。候选从项目页回到 arXiv 原文，按实体平台、世界模型位置、动作接口、试验分母和干预终点筛选。本批次是定向 rapid-scan，不构成完整的交互学习或手术机器人安全综述。
