# Physically Grounded JEPA：状态对齐与目标条件规划

核验日期：2026-10-02。检索轮次：R34。范围：检查动作条件 JEPA 中的物理状态监督是否改善目标条件规划，并区分仿真证据与实体机器人证据。

## 1. 论文身份与去重

- **身份**：Muyuan Liu、Yue Huang、Zheng Liang、Xiang Gao，*Toward Physically Grounded JEPA World Models for Goal-Conditioned Robotic Planning*，arXiv:2609.03565v2，2026-09-19。arXiv 页面说明该工作被 IROS 2026 Workshop on Physical World Models for Scaling Embodied AI 接收；该记录不是 IROS 主会论文。原文：[arXiv HTML v2](https://arxiv.org/html/2609.03565)，[arXiv 记录](https://arxiv.org/abs/2609.03565v2)。
- **去重结果**：题名与 arXiv ID 未在冻结的 929 行分类目录中命中；在 RCL-Robotics 的后续增量发现清单中找到。本文据原文核验后作为正文补充引用，不回写已冻结的 929 行底表。
- **定位**：它与 JEPA-VLA、VLA-JEPA、JEPA-WAM 的区别在于部署阶段保留 action-conditioned predictor，并用 CEM 比较候选动作序列；不是仅把预测表征用于策略训练。

## 2. 模型与规划接口

- 视觉编码器将观测映射到 192 维 latent，action-conditioned predictor 根据当前 latent 和动作块预测下一 latent；未来像素不重建。
- 训练目标由 latent prediction、inverse dynamics（从连续 latent 预测已执行动作）和 state alignment 组成。State-alignment head 用相邻 latent 对回归任务给定的物理量；实验使用各任务提供的完整物理状态监督，包括构型和运动相关量。这是训练期特权监督。
- 部署时只保留 encoder 与 predictor。系统从目标图像编码目标 latent，用 CEM 在 latent rollout 上优化动作序列，执行后获取新观测并重复规划。

## 3. 主要证据与结论

**证据 A：同一论文内的 state-alignment 消融。** 在 TwoRoom、Reacher、PushT 和 OGBench-Cube 四个仿真任务中，IDM-only 版本的规划成功率分别为 94%、63%、83%、85%；加入 state alignment 后分别为 100%、85%、98%、87%。作者方法的数值对每个版本使用三个独立训练 seed，并在每个 seed 上评估相同的 50 个固定起点--目标问题。证据位置：Section III-A--III-B，Table I。

**可支撑判断。** 这项内部消融支持：在所测仿真任务和既定训练/规划流程内，state-alignment loss 相对于 IDM-only 版本提高了四项任务的报告成功率。Table I 没有给出这些成功率的 seed 间方差或置信区间，不能据此判断不确定性范围。

**证据 B：与已发表基线的数值比较。** Table I 列出 DINO-WM、PLDM 和 LeWorldModel 的 100/79/74/86、97/78/78/65、87/86/96/74；原文脚注明确说这些 baseline mean values 取自 LeWorldModel，而不是本研究按同一代码和新 seed 重跑。SA+IDM 在 Reacher 的 85% 低于列出的 LeWorldModel 86%，在 TwoRoom、PushT、OGBench-Cube 则较高。

**可支撑判断。** 这些数值提供跨论文的背景参照，不能作为严格统一协议下的算法排名或显著性证据。

**证据 C：latent 轨迹诊断。** 在 OGBench-Cube 的 100 条固定观测轨迹上，LeWorldModel、IDM 和 SA+IDM 的平均 temporal-straightening 分数分别为 0.69、0.62、0.55；transition energy 达到 95% 所需的平均子空间维数分别为 17、30.2、32.8。LeWorldModel 的 straightening 更高但规划成功率低于 SA+IDM。证据位置：Section III-C，Table II、Figures 3--4。

**可支撑判断。** 该分析说明单一 trajectory-straightening 指标不必与规划成功率同向变化；它是四任务研究中的表示诊断，不证明高维 transition subspace 本身导致了更好控制。

## 4. 局限与待核验

- 所有规划评估都在四个仿真基准完成，没有实体机器人闭环试验；不能据标题中的“physically grounded”推断已在真实物理系统验证。
- State alignment 使用各仿真任务提供的完整物理状态作为训练监督。部署虽不需要该 head，但从视觉学习到状态相关 latent 的可用性依赖这类特权标签。
- 相对 DINO-WM、PLDM、LeWorldModel 的数字取自既有论文报告值；只有 IDM 与 SA+IDM 属于本文的内部消融。不能将跨论文数字写成受控复现实验。
- 作者方法报告三个 seed，但 Table I 未给出方差、置信区间或逐 seed 结果；固定的 50 个起终点问题也不等于更广环境分布上的独立样本。
- 论文没有直接比较预测误差，也没有证明状态对齐通过提升预测准确度而改善规划；可确认的是规划成功率消融和 latent 轨迹统计。
- α、β 在 PushT validation split 上选择，并将相同值用于四个任务；外部有效性仍需在其他数据与机器人上检查。

## 5. 综合判断

该工作填补了综述中“训练时用测量状态约束 action-conditioned latent dynamics，部署时再以 latent rollout 做规划”的接口位置。其最强证据是四个模拟基准上的 state-alignment/IDM 内部消融；它没有实体机器人证据，也没有跨论文受控排名或预测误差--规划收益因果链。正文只用它支撑仿真中的规划接口与局部消融，不扩展为真实 Physical AI 的验证结论。
