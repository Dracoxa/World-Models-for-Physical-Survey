# V-JEPA Policy：预测表示与动作策略耦合证据表

核验日期：2026-10-02。检索轮次：R31。范围：核验最新 V-JEPA 系列工作如何把冻结的预测视觉表示连接到动作生成，并区分匹配组件消融、额外上游预训练和跨方法比较。

## 1. 论文身份与纳入理由

- **身份**：Yang Zhang、Jiangyuan Zhao、Chenyou Fan、Jiayu Hu、Xiu Yuan、Chenjia Bai、Xiu Li，*V-JEPA Policy: Building Effective World-Action Models on Predictive Visual Latents*，arXiv:2609.37250v1，2026-09-29；预印本。原文：[arXiv HTML](https://arxiv.org/html/2609.37250v1)，[arXiv record](https://arxiv.org/abs/2609.37250v1)。
- **去重结果**：按完整题名与 arXiv ID 检查 929 条分类目录、首轮外部候选、第二轮增量候选、补充清单和正文参考文献，均未命中。它是冻结语料之后的 corpus amendment，不改写 929 条目录快照。
- **纳入理由**：该工作直接回答当前正文的高优先级缺口：预测视觉 latent 如何在不继承完整视频生成器的情况下进入 action policy；同时提供匹配的 future-loss 消融和带明确分母的实体双臂试验。

## 2. 模型接口

- 冻结 V-JEPA 2.1 编码器定义视觉 latent 空间；instruction-conditioned predictor 从当前多视角观测、语言和本体状态预测未来视觉 latent。
- predictor 和 flow-matching action expert 在下游示范上联合训练。动作 expert 读取 predictor 各层 context-position key--value states；predictor 不读取候选动作，预测的未来也不用于显式候选动作 rollout 或搜索。
- 推理时先运行一次 predictor，再用 10 次 Euler 步生成动作块。因此它属于 future-informed policy，而不是可查询的 action-conditioned forward planner。

## 3. 主要证据与结论

**证据 A：显式未来监督的匹配消融。** 在固定冻结编码器、下游数据、训练 seed、batch size、更新次数和 action chunk 配置的 LIBERO / LIBERO-Plus 实验中，context-only、保留 future queries 但去除 future loss、完整模型的平均成功率分别为 92.55/65.86、91.65/68.81 和 97.25/79.25。完整模型相对 no-future-loss 控制在两套协议上分别高 5.60 和 10.44 个百分点。证据位置：Appendix D，Table 9。

**论文结论。** 作者认为收益不只来自增加 future-query 路径，显式 future-latent 监督会改善与动作生成耦合的表示。

**可支撑判断。** 该消融支持“在 V-JEPA Policy 的固定架构和训练协议内，显式 future-latent supervision 对仿真控制与分布偏移性能有增量贡献”。它不能证明所有 JEPA 表示或所有 WAM 都会获得同样收益。

**证据 B：预测器预训练与实体结果。** 只在 DROID 视频--指令对上预训练 predictor 100,000 步、不使用动作标签或 action expert，再以相同下游协议训练策略。相对从零初始化 predictor，LIBERO-Plus 从 79.25% 变为 91.50%，RoboCasa-GR1 从 50.92% 变为 55.58%。在 TianJi Marvin 双臂平台上，每项任务 20 次：Table Cleanup 从 11/20 变为 15/20，Saucer Racking 从 7/20 变为 17/20。证据位置：Section 5.4，Tables 3 and 5；Appendices B and E。

**论文结论。** 作者认为 action-free 视频上的 future-modeling knowledge 可以通过同一 latent 空间迁移到下游动作学习。

**可支撑判断。** 结果支持“额外 predictor-only 视频预训练与该系统在三套仿真协议和两个实体任务上的更高成功率相关”，并且实体分母明确。它不是同总计算预算比较：预训练版本增加了 100,000 步上游训练。

## 4. 局限与待核验

- **因果接口边界**：predictor 不以候选动作作为输入，因而不能支撑“模型预测了不同动作的物理后果”或“系统进行了显式模型式规划”。
- **训练重复不足**：future-loss 消融固定一个训练 seed，未报告跨 seed 方差或置信区间；成功率差异不应写成跨模型普遍规律。
- **额外预训练预算**：scratch 与 pretrained-predictor 只匹配下游训练；后者额外使用 DROID 数据和 100,000 步训练，不能称为无额外成本的结构收益。
- **实体范围有限**：仅一个双臂平台、两个任务、每项 20 次；物体恢复到规范配置且光照不变，不能推出开放场景、跨平台或跨操作者泛化。
- **跨方法比较不完全匹配**：实体基线采用各自原生微调日程，作者明确说明不是严格 compute-matched；外部基线表也包含不同预训练资源。
- **系统时延边界**：178.17 ms 是 RTX 4090 上 action-prediction core 的 300 次计时，排除传感器 I/O、后处理和执行器通信，不是端到端控制延迟。

## 5. 综合判断

V-JEPA Policy 是当前稿件中少数同时提供未来监督匹配消融、额外 predictor 预训练对照和带实体分母结果的最新 WAM。最可靠的结论是局部的：在该固定政策架构内，未来 latent 监督和额外 action-free predictor 预训练分别贡献了可测的增量。它不构成可查询动作后果模型，也不支持跨论文的“预测表示优于生成模型”排名。
