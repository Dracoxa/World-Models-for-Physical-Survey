# Policy and Embodied World-Model Evaluation: WoW-World-Eval and RoboWorld

核验日期：2026-10-02。检索轮次：R35。范围：补充实体 world-model 能力评价与生成式世界模型作为 robot-policy evaluator 两个不同层次的证据。两篇均按 arXiv 原文核验，当前记录为预印本。

## 1. WoW-World-Eval

- **身份**：Chun-Kai Fan et al., *Wow, wo, val! A Comprehensive Embodied World Model Evaluation Turing Test*, arXiv:2601.04137v1，2026-01-07。原文：[arXiv 记录](https://arxiv.org/abs/2601.04137v1)，[HTML 全文](https://arxiv.org/html/2601.04137)。
- **设计**：以 609 条真实机器人操作样本构造 benchmark，使用 22 项指标评价 perception、planning、prediction、generalization 和 execution 等能力。人工评价由 15 位领域专家完成，覆盖 1,200 余段真实与生成视频。
- **人类对齐证据**：总体自动分数与人工评分的 Pearson $r=0.93$、Spearman $\rho=0.91$。但各自动指标到总分的映射参数是在人工评分开发集上通过 K-fold CV 选择并冻结的。因此该相关系数说明该评分体系在作者设定中的人工对齐，不应描述为独立、外部的人类验证，更不能替代物理任务效用。
- **可执行性探针**：IDM Turing Test 将生成视频输入在真实执行序列上训练的 GC-IDM，再把推断动作用于九项实体操作任务。作者报告不同的执行成功率，最高的 WoW-wan 为 40.74%，WoW-cosmos2 为 18.52%。这支持把视觉逼真度和动作可执行性分开测量；结果依赖该 IDM、动作映射与九个任务，不能外推为普遍的真实机器人控制能力。
- **可支撑判断**：多维 benchmark 应同时报告感知、人类偏好、物理一致性、规划和执行相关端点；单一视频质量分数不足以代表 embodied capability。
- **不能支撑**：不能由 $r=0.93$ 推出生成视频更有用或控制成功率更高；不能由 IDM 测试推导任意执行策略都能复现生成轨迹。
- **证据位置**：样本与指标见 Section 3；人工评分相关性见 Section 4.3、Figure 3；IDM 实体执行见 Section 4.4、Table 5；指标映射调参见 Appendix 9.6；真实视频 IDM replay 校验见 Appendix 10.3。

## 2. RoboWorld

- **身份**：Byeongguk Jeon et al., *RoboWorld: Fast and Reliable Neural Simulators for Generalist Robot Policy Evaluation*, arXiv:2607.01060v4，2026-07-15 修订。原文：[arXiv v4 记录](https://arxiv.org/abs/2607.01060v4)，[HTML 全文](https://arxiv.org/html/2607.01060)。
- **方法**：RoboWorld 以 DROID 数据训练 action-conditioned autoregressive video world model，使用 Step Forcing 减少自回归 rollout 的 train-test context mismatch，并以 task-progress-aware VLM rubric 对闭环生成视频评分。策略在生成观察中闭环运行，初始条件取自 RoboArena。
- **主要证据**：作者对八个当时公开的 policy 运行 4,186 个生成 rollout，并与 RoboArena 真实世界 leaderboard 比较，报告 Pearson $r=0.989$、Spearman $\rho=0.970$。关键统计单位是八个 policy 的聚合结果，而非 4,186 个独立 policy；复制八个 policy 的完整 benchmark 估算约 100 H100 GPU 小时。以任务进度 rubric 代替二值成功评分后，policy 排名的 Spearman 相关由 $0.922$ 提高至 $0.970$。
- **局限**：世界模型训练数据 DROID 与测试 RoboArena 的设置相关；基准快照和 policy 范围有限。作者指出长时操作中的持续接触与物体一致性仍是限制。因此相关结果是特定 benchmark 上 policy ranking 的代理有效性，不是不同 robot、任务或分布上的外部复现，更不是安全认证。
- **可支撑判断**：评估 world-model-based policy evaluator 时，需直接对照真实 policy 排名、说明相关性统计单位和计算成本，并单独检验生成误差及评分器误差。
- **不能支撑**：不能把 4,186 条 rollout 当作相关分析的 4,186 个独立样本；不能据高相关声称可取代实体测试。
- **证据位置**：训练数据与八个 policy 的范围见 Section 5.1 及其前文脚注；相关性、初始条件、计算成本见 Section 5.3、Figure 5；评分 rubric 消融见 Section 5.4；长时接触局限见 Section 7。

## 3. 综合定位

WoW-World-Eval 主要是 embodied video/world-model 能力 benchmark；RoboWorld 主要把生成式 world model 用作 policy-evaluation proxy。前者强调能力覆盖及人类/IDM评价，后者强调生成环境内的闭环 policy ranking 与真实 leaderboard 的一致性。二者补充了不同证据层，不构成同一量表，也不宜作模型优劣直接比较。
