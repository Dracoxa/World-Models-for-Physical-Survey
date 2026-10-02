# 实体在线干预、执行期纠正与接管风险学习证据表

核验日期：2026-10-02。检索轮次：R28。范围：从第二轮外部候选中筛选能够把预测信号连接到实体动作改变或实体在线学习的工作。本批次是定向证据补充，不表示已完成全部安全、纠正或跨平台研究的系统检索。

## 1. TacPAC

- **身份**：Zipei Ma、Xiaofei Wei、Junzhe Jiang、Shunlin Lu、Li Zhang，*TacPAC: Tactile Prediction and Real-Time Action Correction in World-Action Models for Contact-Rich Manipulation*，arXiv:2609.05266v1，2026-09-04；预印本。原文：[arXiv HTML](https://arxiv.org/html/2609.05266v1)。
- **预测与动作接口**：基础 WAM 联合生成未来视觉、触觉和动作块；执行前缓存预测触觉与动作内部状态。每个新触觉帧触发单次 tactile-expert 前向计算，仅改写尚未执行的动作后缀。
- **主要证据**：单台 Flexiv Rizon 4、两枚 InTac S1 传感器和两路相机上评测五项接触密集任务。每个方法--任务组合执行 20 次，所有尝试均计入。视觉-only、仅触觉预测、去掉预测缓存和完整 TacPAC 的五任务平均成功率分别为 22%、37%、47% 和 64%；最强外部基线 T-Rex 为 48%。完整方法每次纠正平均 30.4 ms，约 32.9 Hz；仅 1.6% 的纠正调用跨过一个或更多控制步。
- **论文结论**：作者认为触觉预测和执行期纠正互补，当前触觉应对照计划时预期的接触来解释，而不是只作为额外的即时输入。
- **可支撑判断**：该工作支持“预测触觉可以成为执行期闭环纠正的参照”，且提供了预测、纠正和缓存访问的组件级实体对照。它不支持跨机器人或跨触觉硬件泛化。
- **局限/待核验**：仅一个机器人和传感器配置；每格 20 次且未报告跨 seed 方差或显著性检验；所有方法虽共享重置和预算，但 Dream-Tac 的 gating 参数为当前传感器另行调整。没有外部扰动、未知物体或跨平台测试，也没有把损伤严重度作为连续指标。

## 2. DreamAvoid

- **身份**：Xianzhe Fan、Yuxiang Lu、Shenyuan Gao、Xiaoyang Wu、Ruihua Han、Manling Li、Hengshuang Zhao，*DreamAvoid: Critical-Phase Test-Time Dreaming to Avoid Failures in VLA Policies*，arXiv:2605.11750v2，2026-09-23；预印本。原文：[arXiv HTML](https://arxiv.org/html/2605.11750v2)。
- **预测与动作接口**：因果 Dream Trigger 检测关键阶段；系统从基础 VLA 采样多个动作块，用动作条件视频模型生成短时未来，再以 Dream Evaluator 排序并执行最高分候选。
- **主要证据**：AgileX PiperX 平台的套杯、插充电器、开盖和螺钉插入四项任务中，每个方法每任务 40 次，共 160 次/方法。DA-ABL 成功 116/160（72.5%），基础策略为 78/160（48.8%），GPC-RANK 为 87/160（54.4%）。每条实体轨迹触发 1--3 次干预；单次干预约 2.133 s，期间暂停高层 ROS 指令并保持最后位置。对 44 个 DA-ABL 失败回合的事后审计中，2 次没有及时触发；其余 42 次里有 6 个致错动作被高估，36 个已被判为低值的动作仍因候选池中没有更好选择而执行。
- **论文结论**：作者认为稀疏关键阶段的显式未来模拟可以在实体精细操作中减少局部错误升级，并比全程重规划节省累计推理时间。
- **可支撑判断**：该工作把“检测关键阶段--预测候选后果--改变实体动作”连成同一闭环协议，支持测试时选择性未来模拟的实体效用。它支持的是经验任务成功，不是经认证的碰撞规避或分布偏移安全。
- **局限/待核验**：关键阶段标签、触发器、evaluator 适配和采样参数仍按任务设置；高层执行在预测期间暂停，因此不能外推到连续高速系统；相对排序即使识别到所有候选都危险仍会执行最高分候选。实体实验使用一个平台，未测试新机器人、操作者变化或开放分布偏移。

## 3. WHIRL

- **身份**：Jiaju Yin、Zhenhui Zhang、Lixin Xu、Heng Zhang、Jun Shao、Yating Feng、Arash Ajoudani、Renjing Xu，*How to Learn from What a Human Would Avoid? Intervention-Aware World Models with Real-World RL for Dexterous Manipulation*，arXiv:2609.06009v1，2026-09-05；作者注明已被 CoRL 2026 接收，尚未用正式 proceedings 记录替换。原文：[arXiv HTML](https://arxiv.org/html/2609.06009v1)。
- **预测与动作接口**：实体 HIL-RL 期间，脚踏接管状态为 latent world model 的下一状态 intervention-probability head 提供监督；该预测通过 actor-side risk shaping 抑制进入操作者会接管的状态。最终成功率测试关闭接管，只保留紧急停止。
- **主要证据**：单台 Franka FR3 与 16-DoF LEAP Hand 上覆盖抓取、放置、抽屉和三阶段长任务五项实体任务。各方法共享 15--30 条示范、行为先验、残差动作空间和操作者规则。与无 world model 的 HIL residual-RL 基线相比，WHIRL 在各任务的最终成功率高 15--30 个百分点；三个抓取类任务各 30 次，Pull Drawer 与 Long Horizon 各 20 次。Pull Drawer 的最终 rolling-5 step-weighted 接管比例由 0.113 降至 0.018。去掉 actor 对 intervention head 的使用会延迟两个核验任务上的接管比例收敛。
- **论文结论**：作者认为人类接管不应只作为一次性纠正，还可训练前瞻接管概率并用于策略风险整形，从而降低后续训练期人工负担。
- **可支撑判断**：该工作支持“接管标签可被世界模型转化为策略学习的前瞻风险信号”，并以最终无接管的实体成功率避免把人工救援直接计作自主成功。它不是运行时报警自动触发纠正的实验。
- **局限/待核验**：每个任务--方法组合只有一个 seed 和一名操作者；评测只覆盖训练标记范围内的位置与接近偏移，不含新物体、布局、操作者、手形或平台。两个长任务的单侧未校正 Fisher 检验仅达到约 0.08--0.09；intervention head 继承该操作者的接管阈值与习惯。

## 4. 本批次筛选边界

[CoWAM](https://arxiv.org/html/2608.02578v1)同样使用预测候选执行选择性干预，并通过同候选池、预先提交决策和配对统计较好地隔离 selector 效果；但其八项任务全部为仿真。本批次目标是补实体动作改变和实体在线学习，因此记录为方法学边界，不计入正文新增证据或参考文献数量。

## 5. 综合判断

三项工作覆盖互不等价的接口：TacPAC 在动作块执行过程中进行高频触觉纠正；DreamAvoid 在关键阶段暂停并重排候选动作；WHIRL 将训练期人类接管转化为策略风险整形。它们共同表明，预测只有连接到明确的动作改变时才构成干预证据。现有证据仍集中在单平台、任务内设置：没有一项同时完成跨平台、跨操作者、真实分布偏移、事故严重度和开放故障后状态恢复。
