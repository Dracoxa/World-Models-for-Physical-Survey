# 原文核验批次 11：CVPR 2026 预测与策略融合

核验日期：2026-10-02。检索模式为 **rapid-scan（CVPR 2026 定向补充）**。问题限定为：联合视频--动作模型、预测表示和多模态生成究竟怎样进入机器人策略，以及实体结果是否能隔离预测模块的贡献。本批次不把联合生成自动等同于可查询的前向世界模型，也不把部分任务完成率当作完整任务成功率。

## 结论概览

| 论文 | 发表状态 | 机制位置 | 可支撑的窄结论 |
|---|---|---|---|
| [Motus](https://openaccess.thecvf.com/content/CVPR2026/html/Bi_Motus_A_Unified_Latent_Action_World_Model_CVPR_2026_paper.html) | CVPR 2026 正式论文 | 统一的视频、动作、逆动力学与 VLA 生成模式 | 联合视频--动作预训练及视频生成专家与较高的仿真策略性能相关；实体结果证明可部署，但采用部分成功率且未报告评测分母。 |
| [DynBridge](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_DynBridge_Bridging_Imagination_and_Control_through_Interaction_Dynamics_for_Robot_CVPR_2026_paper.html) | CVPR 2026 正式论文 | 轨迹预测监督形成交互 latent，再由动作头执行 | 在同一策略内加入未来交互轨迹监督可改善仿真和小规模实体控制；该 latent 不是候选动作可查询的反事实模型。 |
| [MM-ACT](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_MM-ACT_Learn_from_Multimodal_Parallel_Generation_to_Act_CVPR_2026_paper.html) | CVPR 2026 正式论文 | 文本、未来图像和动作的共享上下文联合监督 | 在 RoboTwin 的匹配训练消融中，图像与文本辅助目标共同提高动作成功率；实体主比较没有单独隔离预测目标。 |

Motus 已在现有 929 条目录中；DynBridge 与 MM-ACT 未按完整题名检出，作为正文补充来源单列。

## 1. Motus

**身份与机制。** CVPR 2026 正式论文。Motus 使用 Mixture-of-Transformer 专家和异步 UniDiffuser 调度，在同一模型中支持视觉语言理解、视频生成、动作生成、逆动力学以及视频--动作联合预测。光流 latent action 用于从无动作视频学习运动先验。

**主要证据与论文结论。** RoboTwin 2.0 的 50 个任务使用每任务 50 条 clean 和 500 条强随机化训练示范，并以每任务 100 次执行评估。表 2 中，Motus 在 clean/randomized 条件下平均为 88.66%/87.02%，X-VLA 为 72.80%/72.84%，$\pi_{0.5}$ 为 42.98%/43.84%。仿真组件消融将完整模型的 77.00% 与去除视频生成专家后的 25.50% 比较。实体实验覆盖 AC-One 和 Agilex-Aloha-2 两个平台，每任务使用 100 条训练轨迹；表 3 报告的是子任务分解后的 partial success rate，Motus 平均为 63.22% 和 59.30%。

**可支撑判断。** 该工作支持“统一视频--动作生成可以作为联合预训练接口，视频生成专家在受控 RoboTwin 消融中对策略性能有重要贡献”。

**局限与待核验。** 实体表没有报告评测 trial 数，且采用部分成功率，不能与完整任务成功率直接比较。仿真主比较中的架构、预训练数据和训练阶段同时变化；只有组件消融更接近隔离视频生成专家，但仍不能证明视频预测是全部增益来源。模型支持多种生成模式，不代表部署时显式滚动或比较候选动作后果。证据位置：第 3、5.2--5.4、6 节，表 2--5，图 6--7。

## 2. DynBridge

**身份与机制。** CVPR 2026 正式论文。系统以未来点轨迹重建和动作模仿共同训练 interaction-dynamics tokens，再通过动作感知聚合器和自回归动作头输出控制。预测表示由观察、指令和历史动作语义形成，但论文没有提供把候选动作送入同一前向模型并比较后果的规划接口。

**主要证据与论文结论。** LIBERO 结果报告 3 个随机种子；表 1 中 DynBridge 在 LIBERO-90 上为 $0.75\pm0.01$，GraphMimic 为 $0.67\pm0.01$，且完整方法只使用每任务 10 条动作标注示范。消融显示移除轨迹预测、分离生成器与动作头、或不用 interaction dynamics 均降低控制性能。实体实验在单台 Franka Research 3 上覆盖五项任务，论文说明结果来自 10 次试验，并以完整模型对比去除 interaction dynamics 的版本。

**可支撑判断。** 该工作支持“未来交互轨迹监督可在策略内部形成有用的预测 latent，并在匹配消融中改善动作输出”。

**局限与待核验。** 实体试验规模小，图 11 仅给完整模型与内部消融，不含强外部策略基线或置信区间。LIBERO 主比较的外部数据和方法结构并非完全一致，不能仅凭排行榜差值归因。作者称其表示具有 causal information，但实验主要验证控制收益与分布变化鲁棒性，没有执行干预识别或反事实因果检验。因此正文将其归为预测辅助策略，而非可查询反事实规划器。证据位置：第 3、4.1--4.4、5 节，表 1，图 4、7--11。

## 3. MM-ACT

**身份与机制。** CVPR 2026 正式论文。MM-ACT 在共享离散 token 空间中并行生成文本、未来图像和动作；Context-Shared Multimodal Learning 从同一上下文联合监督三种输出。未来图像是训练辅助输出，没有在执行时用于候选动作搜索。

**主要证据与论文结论。** LIBERO 四套仿真基准中，动作-only 版本平均为 95.0%，加入长时文本规划后为 96.3%；LIBERO-Long 从 88.0% 增至 93.0%。RoboTwin 八任务的匹配训练比较中，动作-only、加文本、加图像、文本与图像均加入的平均成功率分别为 43.13%、46.50%、48.75% 和 52.38%。三项 Franka 实体任务对每个模型各执行 20 次，MM-ACT、$\pi_0$ 和 OpenVLA-OFT 的平均结果分别为 72.0%、70.0% 和 58.6%。

**可支撑判断。** 该工作支持“未来图像与文本生成目标可作为共享表示监督，在受控仿真训练消融中改善动作生成”。

**局限与待核验。** 实体主比较没有报告 action-only、text-only 和 image-only 版本，因而不能把 72.0% 的实体结果归因于预测辅助目标；相对 $\pi_0$ 的差值只有 2 个百分点、每任务 20 次，论文未给置信区间。RoboTwin 的联合文本与图像条件同时变化，9.25 点增益不能拆成独立贡献。该模型生成未来图像，但未展示动作条件前向查询或反事实规划。证据位置：第 3、4.1--4.4、5 节，表 1--3，图 5。

## 跨论文判断与筛选结论

1. Motus 是本批次最接近联合 world--action model 的工作，但其实体证据采用部分成功率且分母缺失。
2. DynBridge 与 MM-ACT 都证明预测目标可以辅助策略学习；它们不提供候选动作条件的显式前向查询，因此不能用来支持模型预测控制或反事实规划。
3. 三篇工作均提示“生成未来”至少有三种系统含义：可执行时联合生成、训练时表示监督、以及可供规划器查询的动力学模型。综述应分别报告，不能以 world model 标签合并。

## 检索与证据边界

检索词包括 `site:openaccess.thecvf.com/content/CVPR2026/html "world model" robot`、`"world models" embodied`、`"action-conditioned" robot` 和 `predictive planning robot`。官方 CVF 页面返回的 11 个唯一候选中，Motus、Chain of World、4DWorldBench 和 RoboWM-Bench 已在目录；另外 7 篇未按完整题名检出。本批次只深查与策略接口最直接的 DynBridge、Motus 和 MM-ACT，不构成完整 CVPR 2026 会场普查，其余候选仍需标题/摘要筛选和去重。
