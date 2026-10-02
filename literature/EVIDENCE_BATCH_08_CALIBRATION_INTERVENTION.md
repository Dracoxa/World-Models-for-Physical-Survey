# 原文核验批次 08：分布偏移校准、选择性求助与干预代价

核验日期：2026-10-02。检索模式为 **rapid-scan（快速定向补充）**。问题限定为：世界模型的风险信号是否经过校准，报警之后是否真正改变机器人行为，以及人类求助和接管代价如何记录。本批次不把 conformal prediction 写成任意分布偏移下的无条件保证，也不把非世界模型方法改写为世界模型。

## 结论概览

| 论文 | 发表状态 | 机制位置 | 可支撑的窄结论 |
|---|---|---|---|
| [Foresight](https://arxiv.org/abs/2606.23085v1) | 2026 arXiv v1 预印本 | 动作条件世界模型 latent 上的失败检测 | 预测 latent 可作为跨若干策略的长时失败监测信号；当前实体证据是离线检测，不是在线干预。 |
| [KnowNo](https://proceedings.mlr.press/v229/ren23a.html) | CoRL 2023 正式论文 | LLM 规划器的 conformal 求助接口 | 在其规划假设下，校准预测集可把任务覆盖要求连接到求助决策，并显式报告 help rate。 |
| [CoFineLLM](https://proceedings.mlr.press/v331/wang26c.html) | L4DC 2026 正式论文 | 面向较小预测集的 conformal finetuning | 近期正式工作开始把覆盖与求助频率共同作为优化目标，并报告硬件 OOD 演示。 |
| [ThriftyDAgger](https://proceedings.mlr.press/v164/hoque22a.html) | CoRL 2021 / PMLR 2022 正式论文 | 基于新颖性和风险的人工接管门控 | 干预次数、持续时间、人工动作数和注意力切换应与任务成功一起报告。 |

四篇均未在现有 929 条目录中按完整题名或 arXiv ID 检出，作为正文补充来源单列。

## 1. Foresight

**身份与机制。** 2026 arXiv 预印本。系统以 V-JEPA 2-AC 为动作条件世界模型，使用预测 latent 和因果序列模型输出逐步失败分数，再用成功轨迹上的 functional conformal prediction 构造随时间变化的报警阈值。检测器只访问视觉观测和策略产生的动作块，不访问策略内部状态。

**主要证据与论文结论。** 三个仿真基准中，Transformer 版本的 balanced accuracy 分别为 $0.94\pm0.06$、$0.80\pm0.10$ 和 $0.78\pm0.02$。实体数据由遥操作采集，覆盖 ReactorX 上的 ACT、$\pi_{0.5}$、SmolVLA 和 Franka 上的 GR00T N1.5；对应 ROC-AUC 为 $0.93\pm0.01$、$0.87\pm0.03$、$0.79\pm0.09$ 和 $0.89\pm0.10$，其中 SmolVLA 设置低于 RND 的 $0.82\pm0.03$。作者据此认为动作条件世界模型表示适合长时失败监测。

**可支撑判断。** 该工作支持“动作条件预测 latent 可以为若干长时操作策略提供失败检测特征”，并把误报控制与校准集明确联系起来。

**局限与待核验。** 实体 rollouts 上只离线评价检测器，没有把报警接到停止、求助或恢复动作，因此不能推出实体事故减少。显著性水平按方法和基准选择以最大化 balanced accuracy，不是预先固定的安全运行点；跨策略迁移明显不对称。conformal 误报保证依赖 exchangeability 或校准与部署分布匹配。H200 上 Transformer 总时延为 183.64 ms，超过 99% 来自世界模型主干。证据位置：第 4.4、5.1--5.4、6 节，表 2--4、14，附录 8--9、14。

## 2. KnowNo

**身份与机制。** CoRL 2023 正式论文。KnowNo 为 LLM 规划器构造 conformal prediction set：集合为单元素时执行，否则请求人类从候选中消除歧义。

**主要证据与论文结论。** 实体多步桌面任务每种方法 50 次试验。KnowNo 的 plan success 为 0.76、task success 为 0.74、逐步 help rate 为 0.58；Simple Set 的 plan success 同为 0.76，逐步 help rate 为 0.72；No Help 的 task success 为 0.38。实体移动操作实验中，KnowNo 与 Simple Set 的 plan success 均为 0.87，而 help rate 分别为 0.67 和 0.81。作者据此认为校准预测集可在覆盖要求下减少不必要求助。

**可支撑判断。** 该工作支持“选择性执行需要同时报告任务覆盖和求助频率”，可作为世界模型报警之后如何进入决策的边界对照。

**局限与待核验。** 该方法不是世界模型。保证依赖 i.i.d./exchangeability 假设和正确的人类帮助；论文假设环境对象已经以文本正确 grounding，且规划动作可由低层策略成功执行，因此未校准感知误差、动力学偏差或控制失败。证据位置：第 3--5 节，实体实验表 1--2，局限部分。

## 3. CoFineLLM

**身份与机制。** L4DC 2026 正式论文。系统在 conformal prediction 框架中微调 LLM 规划器，使正确动作保持在预测集中的同时缩小集合；集合非单元素时请求人类帮助。

**主要证据与论文结论。** PMLR 正式页面报告在多个语言指令规划问题上，相比 uncertainty-aware 和 uncertainty-agnostic finetuning 基线，预测集大小和 help rate 均持续改善，并包含硬件 OOD 场景演示。

**可支撑判断。** 该工作支持“覆盖并不是唯一目标，预测集大小和求助率也可进入训练目标”，并提供 2026 年正式发表的选择性规划进展。

**局限与待核验。** 该方法不是世界模型。本轮只使用 PMLR 正式摘要支撑上述方法级判断，没有从全文提取硬件任务分母、具体 shift、效果数字和失败案例；在完成全文协议核验前不用于定量比较，也不能外推到感知和低层控制安全。证据位置：PMLR 正式摘要；全文实验细节待核。

## 4. ThriftyDAgger

**身份与机制。** CoRL 2021、PMLR 2022 正式论文。robot-gated interactive imitation learning 根据状态新颖性或较低任务完成概率请求监督，并让用户指定目标干预频率；监督负担由注意力切换与干预持续时间共同构成。

**主要证据与论文结论。** da Vinci 实体线缆布置使用 25 条离线示范和 1,500 个环境步，每种方法各进行 15 次自主和 15 次干预辅助评估。ThriftyDAgger 自主成功 12/15，干预辅助成功 15/15，平均干预次数为 0.40，人工动作数为 $1.5\pm3.1$；HG-DAgger 对应为 10/15、15/15、0.40 和 $2.7\pm3.5$。另有 10 人的三机器人仿真用户研究。

**可支撑判断。** 该工作提供干预负担的可操作指标：干预次数相同仍可能有不同的人工动作量、持续时间和上下文切换成本。

**局限与待核验。** 该方法不是世界模型。实体证据只有一个线缆任务和每条件 15 次试验；100% 指干预辅助下的 15/15，不能解释为广泛实体可靠性。用户注意力结果来自仿真三机器人队列。证据位置：第 III--VI 节，表 III--IV。

## 跨论文判断与仍缺证据

1. 失败分数、校准报警、求助、动作接管和任务恢复是五个不同接口。只有前两项不能证明安全收益。
2. ROC-AUC 是阈值无关的区分指标，不能替代部署阈值下的误报率、漏报率、检测提前量和事故减少量。
3. conformal coverage 依赖可陈述的分布假设；进入新的机器人、策略、操作者或接触条件后，应重新验证或校准，而不是沿用“分布无关”口号。
4. 下一轮仍需寻找把世界模型报警接入在线停止、求助或恢复，并在真实分布偏移下报告 incident severity、lead time、help duration 和 task completion 的跨平台研究。

## 检索与证据边界

本轮从 `world model uncertainty calibration robot safety 2026`、`robot failure detector conformal real world`、`robot ask for help conformal planning` 和 `robot intervention cost physical evaluation` 定向检索，回到 arXiv 与 PMLR 原始页面和论文。Foresight 是直接世界模型证据；KnowNo、CoFineLLM 和 ThriftyDAgger仅作为“报警之后如何决定与计量”的边界对照。本批次不是完整的选择性预测或交互模仿学习综述。
