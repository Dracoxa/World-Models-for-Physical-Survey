# JEPA 策略最近邻：人类视频预训练与训练期预测监督证据表

核验日期：2026-10-02。检索轮次：R32。范围：以 V-JEPA Policy 为锚点核验两项最接近的 JEPA--VLA/WAM 工作，区分人类视频预训练、训练期状态转移监督和部署期在线预测。

## 1. VLA-JEPA

- **身份**：Jingwen Sun、Wenyao Zhang、Zekun Qi、Shaojie Ren、Zezhi Liu、Hanxin Zhu、Guangzhong Sun、Xin Jin、Zhibo Chen，*VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model*，arXiv:2602.10098v2，2026-02-14；预印本。原文：[arXiv HTML](https://arxiv.org/html/2602.10098v2)，[arXiv record](https://arxiv.org/abs/2602.10098)。
- **版本说明**：arXiv 记录显示 v2 修订于 2026-02-14，但实验 HTML 的标题页显示 2026-08-24。本文按 arXiv 版本记录日期引用，并保留该元数据不一致。
- **去重结果**：完整题名与 arXiv ID 未在 929 条目录命中；已存在于首轮外部候选表，来源为 NTUMARS 与 OpenMOSS。本轮将其从发现线索升级为原文核验补充记录。

### 模型接口

- Qwen3-VL 从当前多视角观测和语言产生 latent-action tokens；冻结的 V-JEPA2 编码器提供未来 world-state targets，未来帧不进入 VLM 输入。
- 人类视频只使用 latent state-prediction loss；机器人数据同时使用状态预测与 flow-matching action loss。预训练包含 220K Something-Something-v2 视频和 76K DROID 轨迹，实体后训练使用三项任务共 100 条示范。
- 该系统学习训练期状态转移表征和动作头，但不在部署时查询候选动作的未来后果，因此不属于显式在线 rollout planner。

### 主要证据与结论

**证据 A：人类视频消融呈现基准依赖。** 在论文内部对照中，加入人类视频后 LIBERO 平均成功率从 96.1% 变为 97.2%，LIBERO-Plus 从 62.9% 变为 79.5%；但 SimplerEnv 的两个机器人平均值分别从 78.4/57.3 变为 65.2/57.3。作者也明确写道，移除人类视频在 LIBERO 和 SimplerEnv 上没有显著下降，并可在 SimplerEnv 上更高。证据位置：Section 4.3，Tables 1--3；Section 4.5，Q1。

**论文结论。** 作者认为人类视频更主要地改善已有技能在视觉扰动下的稳定性，而不是直接提供机器人动作轨迹或精细物理动力学。

**可支撑判断。** 该证据支持“在 VLA-JEPA 的固定训练配方中，人类视频与 LIBERO-Plus 鲁棒性提升相关，但收益不能外推到所有基准”。它不支持“人类视频普遍提升控制性能”。

**证据 B：实体结果范围有限。** 论文在一台 Franka Research 3 上测试 ID、任务 OOD 和对象布局 OOD，每项任务 10 次。附录报告香蕉任务中 VLA-JEPA 与 $\pi_{0.5}$ 均约 50%，货架任务所有模型均失败；正文还指出 VLA-JEPA 的指令跟随弱于 $\pi_{0.5}$，可能抓取错误对象。证据位置：Section 4.4；Appendix B。

**可支撑判断。** 实体结果说明方法可在一个平台上接受受控测试，并暴露任务 OOD 失败；“较少触碰安全边界”来自论文观察，不是校准风险、事故率或独立安全研究。

### 局限与待核验

- 完整方法同时改变 VLM、V-JEPA2 targets、220K 人类视频、76K 机器人轨迹和联合目标，跨方法总分不能归因于 JEPA 单一机制。
- 论文未提供可将人类视频增益与等计算、等数据量控制分开的消融；不同基准上的方向不一致。
- 实体试验每任务 10 次，且未见训练 seed、方差或置信区间报告。
- latent action 不是部署时可由候选机器人动作查询的 action-conditioned forward model。

## 2. JEPA-WAM

- **身份**：Yihan Lin、Jiawei He、Shifeng Bao、Chen Zhao、Yang Li、Xiaobo Wang、Yan Wang、Cheng Chi、Jing Zhang，*JEPA-WAM: Learning Vision-Language-Action Policies with Joint-Embedding World Modeling*，arXiv:2608.09381v1，2026-08-10；预印本。原文：[arXiv HTML](https://arxiv.org/html/2608.09381v1)，[arXiv record](https://arxiv.org/abs/2608.09381)。
- **去重结果**：arXiv ID 已在 929 条目录的 `S01-0067`、`S02-0036`、`S06-0035` 和 publication family `PF-S01-0067` 命中。因此它增加正文引用和核验记录，但不增加目录外补充数。

### 模型接口

- 冻结的 V-JEPA 2.1 编码器定义 target space；共享 predictor 同时接受 transition supervision 并为连续动作生成提供表征。
- 目标是空间结构化的 current--future joint embedding，而不是唯一未来图像。部署时移除 target encoder、transition prediction head 和 transition loss，只保留当前观测到动作的策略路径。
- 因此该工作检验预测目标如何塑造策略训练，不执行部署期未来生成、候选动作后果查询或显式搜索。

### 主要证据与结论

**证据 A：同训练设置下的表示、目标和接口消融。** 在 LIBERO-Plus 的统一 policy-training setup 中，DINO+SigLIP、禁用 transition prediction 的 V-JEPA-only、future-only target、intermediate-layer alignment、full-hidden action conditioning 和完整 JEPA-WAM 的平均成功率分别为 73.2%、77.0%、77.3%、76.5%、73.1% 和 79.2%。证据位置：Section 4.3，Table 4。

**论文结论。** 作者认为 V-JEPA 表示本身贡献一部分鲁棒性，joint current--future target、final shared predictor 和专用 action placeholders 进一步改善该配方。

**可支撑判断。** 该消融支持“在 JEPA-WAM 的匹配训练协议内，训练期 transition target 和接口设计具有局部增量贡献”。它不能把与外部模型的总分差异归因于预测目标，也没有多 seed 不确定性。

**证据 B：实体协议与指标。** 在 AgileX COBOT Magic 双臂平台的五项任务上，每项 ID/OOD 设置各 10 次，指标是 normalized task-completion score 而非二元成功率。JEPA-WAM 相对 $\pi_0$ 的平均分为 59.82/54.18 对 51.82/22.50；在 $\pi_{0.5}$ 上加入同一 JEPA 目标后为 90.34/84.68，对照为 77.52/72.50。证据位置：Section 4.4；Appendix E，Table 15 及逐回合记录。

**证据 C：表示探测包含反向结果。** joint target 对去除端点位移后的 14 维残余轨迹预测将平均 $R^2$ 从 0.485 提高到 0.582，配对差异 95% CI 为 [0.082, 0.112]；但直接端点位移预测中 endpoint difference 为 0.740，joint target 为 0.718，配对差异为 -0.022，95% CI 为 [-0.036, -0.009]。证据位置：Appendix C.2，Tables 9--10。

**可支撑判断。** joint target 更适合论文定义的区间轨迹结构，但并非对所有 transition probes 都更优；这项负向控制应与正向结果共同保留。

### 局限与待核验

- 部署时不运行 transition prediction，不能描述为在线 imagination、replanning 或显式模型式控制。
- 实体结果来自一个平台、每任务每设置 10 次，并使用可给部分完成度的 normalized score；不能改写为二元成功率。
- 未见多训练 seed、方差或显著性报告；外部基线还使用不同的预训练资源。
- joint target 主要编码任务共享的视觉时间结构；论文也承认同一观测在不同指令下产生不同转移时可能表达不足。

## 3. 综合判断

三项相邻工作占据不同接口位置：VLA-JEPA 用人类视频训练 latent transition/action tokens，JEPA-WAM 在训练期用 transition target 塑造共享策略表征，V-JEPA Policy 则在部署时运行 predictor 并把其 context states 送入 action expert。最稳妥的共同结论是：JEPA-style predictive supervision 已有论文内部的局部消融支持，但只有 V-JEPA Policy 在部署时显式运行 predictor；三者都没有提供候选动作条件的在线后果 rollout。该结论适用于当前三篇预印本及其报告协议，不是对所有 JEPA/VLA 方法的普遍排序。
