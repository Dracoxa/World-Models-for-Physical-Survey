# JEPA-VLA：预测预训练表示迁移证据表

核验日期：2026-10-02。检索轮次：R33。范围：核验冻结视频预测表示是否作为视觉先验改善 VLA，并区分表征迁移、下游预测监督和部署期世界模型查询。

## 1. 论文身份与去重

- **身份**：Shangchen Miao、Ningya Feng、Jialong Wu、Ye Lin、Xu He、Dong Li、Mingsheng Long，*JEPA-VLA: Video Predictive Embedding is Needed for VLA Models*，arXiv:2602.11832v1，2026-02-12；预印本。原文：[arXiv HTML](https://arxiv.org/html/2602.11832v1)，[arXiv record](https://arxiv.org/abs/2602.11832)。
- **去重结果**：完整题名与 arXiv ID 未在 929 条目录、第二轮增量候选、写作缺口或正文参考文献命中；已存在于首轮外部候选表，来源为 NTUMARS，优先级为高。本轮将其从发现线索升级为原文核验补充记录。
- **纳入理由**：它提供 V-JEPA 2 表征进入 VLA 的直接内部对照，同时构成一个重要边界：使用由预测预训练得到的 encoder，不等于下游系统仍在训练或查询世界模型。

## 2. 模型接口

- 冻结 V-JEPA 2 encoder 从最近两帧提取 embeddings，作为当前历史的额外视觉条件输入动作模型。
- 对从头训练或缺少大规模机器人预训练的 VLA，embeddings 直接拼接；对 OpenVLA-OFT 类预训练策略，通过稀疏 gated cross-attention 融合。
- 下游训练没有 future target、transition loss 或 action-conditioned forward model；推理时也不生成未来状态或比较候选动作。因此本文最适合作为 predictive-pretraining representation transfer，而不是在线 world-model planning 的证据。

## 3. 主要证据与结论

**证据 A：同实现策略中的表征融合对照。** 在只使用十分之一 LIBERO 数据的 basic VLA 中，加入冻结 V-JEPA 2 embeddings 后，LIBERO 平均成功率从 61.65% 变为 69.05%，LIBERO-Plus 从 18.9% 变为 25.6%。在作者实现的 OpenVLA-OFT 配方中，LIBERO 平均成功率从 90.30% 变为 96.40%；RoboTwin 2.0 六任务 easy/hard 平均值从 54.8/9.3 变为 73.5/17.7。证据位置：Section 4.3，Tables 1--4。

**论文结论。** 作者认为视频预测预训练得到的视觉 embeddings 能补充 task-relevant state information 和 successful-demo temporal priors，并改善数据效率与分布变化表现。

**可支撑判断。** 这些内部对照支持“在论文的 basic VLA 与 OpenVLA-OFT 实现中，增加 V-JEPA 2 encoder 及相应 fusion module 与更高成功率相关”。它不能把增益单独归因于预测预训练目标，因为表示容量、额外 encoder、融合模块和计算量同时变化。

**证据 B：冻结表示 probes。** 作者冻结 V-JEPA 2、DINOv2 和 SigLIP 特征，再训练轻量 head 估计当前任务相关状态、任务无关扰动或十步后的状态残差。V-JEPA 2 在任务相关回归和未来残差预测上报告更低误差，在照明与背景回归上误差更高。证据位置：Section 2；Appendix A；Figure 2。

**可支撑判断。** probes 支持“在该数据划分和监督 head 下，V-JEPA 2 特征更容易恢复作者定义的任务相关变量，并较少编码两类 nuisance labels”。未来残差 head 在成功示范上学习，输入不含候选动作；它不能证明 encoder 已识别因果动力学或能预测不同动作的后果。

**证据 C：实体任务。** 一台 Piper 单臂机器人执行一个碗放盘任务；训练集为 100 条示范，并另训 22 条示范版本。论文称每个模型进行 10 次独立试验，并报告标准、布局和照明变化下的成功率。证据位置：Section 4.1，Table 5；Appendix E。

**可支撑判断。** 该实验提供单平台、单任务的物理可行性信号，但不能支撑跨任务或跨平台泛化。Table 5 出现 33.3% 和 66.7%，而附录只写“每个模型 10 次”，未明确这些列是否各自另有分母；在分母澄清前，不把这些百分数换算成成功次数。

## 4. 局限与待核验

- **组件归因**：matched baseline 同时增加大型冻结 encoder、projection/cross-attention 和额外输入；没有在 mainstream VLA 设置中进行等参数、等延迟的 DINO/SigLIP encoder 对照。
- **表征替换表存在标签异常**：Table 7 的 HTML 中 `Baseline+DINOv2` 出现两次且数值不同；该表不能在标签澄清前支持完整 encoder 排名。
- **复现设置敏感**：作者自己的 OpenVLA-OFT baseline 为 90.30%，官方论文数值为 95.35%；完整方法 96.40% 与官方数值不是同实现、同批量的严格对照。
- **统计不足**：未见多训练 seed、方差或显著性报告；LIBERO-Plus 通过四个已选择 checkpoints 取平均，不能替代独立训练重复。
- **实体范围与分母**：一个平台、一个任务，且分条件成功率与“10 次/模型”说明不完全对应。
- **系统成本**：论文未报告增加 V-JEPA 2 encoder 和 fusion 后的端到端控制延迟、显存或能耗。

## 5. 综合判断

JEPA-VLA 补充了当前证据图谱中“预测预训练表示直接迁移到策略”的位置。它比 VLA-JEPA 和 JEPA-WAM 更靠前：预测目标只存在于 V-JEPA 2 的上游预训练，下游策略本身没有 transition objective；它也比 V-JEPA Policy 更弱地暴露 predictor，因为部署时只运行 encoder。最稳妥的结论是，视频预测预训练特征在论文的多个内部策略对照中具有增量效用；该效用不能自动等同于下游世界模型、在线 imagination 或因果动作后果预测。
