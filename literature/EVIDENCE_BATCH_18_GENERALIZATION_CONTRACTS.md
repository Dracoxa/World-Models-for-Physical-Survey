# 泛化契约：仿真到实体、相机外推与组合任务证据表

核验日期：2026-10-02。检索轮次：R29。范围：从第二轮外部候选中定向核验 world-action model 在仿真到实体、未见相机、未见组合和未见任务配置上的证据。这里的“泛化”按变化轴分别记录，不把不同实验协议合并为单一强度等级。

## 1. Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors

- **身份**：Zixing Wang、Kausik Sivakumar、Jinghuan Shang、Yafei Hu、Zhaoming Xie、Ran Gong、Xiaohan Zhang、Karl Schmeckpeper，*Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors*，arXiv:2606.31101v1，2026-06-30；CVPR 2026 Embodied AI Workshop early result。原文：[arXiv HTML](https://arxiv.org/html/2606.31101v1)。
- **变化轴与接口**：Cosmos Policy 在仿真中联合生成未来视觉、动作和价值；训练使用约 3,200 条自动生成示范与纹理、相机、光照和物体位置随机化，不使用实体示范或实体微调，然后直接部署到 Franka Research 3。
- **主要证据**：香蕉抬升、砖块抬升、开抽屉和草莓入碗各执行 10 次实体试验，成功率分别为 5/10、5/10、2/10 和 2/10，平均 35%。使用 10 或 50 条实体示范训练的 Diffusion Policy 参考分别为 5% 和 25%，但数据来源和结构均不匹配。未见瓶子的抬升只给出成功定性序列，没有重复试验分母。
- **论文结论**：作者认为自动生成仿真数据、域随机化和视频先验的组合可以使 WAM 获得非零零样本实体操作能力。
- **可支撑判断**：该工作支持“WAM 可以在没有实体示范或实体微调的条件下实现有限的 sim-to-real 实体成功”，不支持 WAM 相对其他策略结构的因果优势，也不支持高可靠部署。
- **局限/待核验**：仅一台机器人、四项任务且每项 10 次；没有训练数据与计算匹配的架构消融；视频先验、域随机化和联合视频--动作目标未被分别隔离；35% 平均成功率意味着多数实体试验仍失败。作者将其明确标为后续完整工作的 early result。

## 2. Selective Cross-View Consistency

- **身份**：Bingqi Huang、Bingchuan Wei、Yingkai Cai、Zhaokui Wang，*Selective Cross-View Consistency for World Action Models: Held-Out Viewpoint Robustness Without Test-Time Camera Information*，arXiv:2608.21402v1，2026-08-07；预印本。原文：[arXiv HTML](https://arxiv.org/html/2608.21402v1)。
- **变化轴与接口**：同一物理状态从不同相机渲染为训练对。选择性交叉视角一致性只约束动作块、未来本体感知和价值等视角不变量，而保留未来图像随相机变化；部署时不需要相机参数、深度或测试时视图合成。
- **主要证据**：作者在 LIBERO-Plus 相机轨道上构建 carve-and-hold-out 协议，并用相同基础 checkpoint、相同训练对、预算和噪声日程的零一致性权重对照隔离目标函数作用。第一 seed 的轨道外推桶由 63.8% 提升至 76.0%，差值 12.2 点、95% CI [7.4, 17.0]；第二 seed 差值 15.5 点、CI [11.7, 19.4]。另外两个相机轴复现较小增益；训练范围内插值无增益。极端复合视角下 object suite 反而下降 40.4 点。
- **论文结论**：作者认为结构化 WAM 输出必须按变换规律选择一致性坐标，且相机鲁棒性需要把分布匹配、插值和外推分开报告。
- **可支撑判断**：该工作支持“未来图像与动作等输出具有不同相机变换规律，错误的一致性约束会损害预测；匹配对照下的选择性约束可改善部分未见视角外推”。
- **局限/待核验**：全部闭环结果来自仿真；WAM 本体没有实体机器人验证；需要同状态跨视角训练对；只考察 scene camera，腕部相机扰动不在范围内；没有测试失败或恢复状态，且复合极端视角存在明显退化。

## 3. Temporal Ratio

- **身份**：Utkarsh A. Mishra、Yongxin Chen、Danfei Xu、Yang Liu、Xi Chen、Jiayuan Mao，*Understanding and Mitigating the Video-Action Generalization Gap via Temporal Ratio*，arXiv:2607.08127v1，2026-07-09；预印本。原文：[arXiv HTML](https://arxiv.org/html/2607.08127v1)。
- **变化轴与接口**：Temporal Ratio 衡量动作 token 对预测未来 latent 与当前观测 token 的注意力比值。推理时 guidance 在 TR 较高的规划阶段增强语言和长时未来条件，在精细操作阶段减弱。
- **主要证据**：LIBERO OOD 每任务 50 回合、3 seeds，最佳 unguided 与 guided 版本的 OOD 平均成功率为 55.7% 和 59.4%，ID 平均约为 94%。实体 YAM 训练集含 24 项任务和 5,600 回合；八项组合测试每方法共 60 次，unguided 由 71.7% 提升到 guided 的 83.3%，而匹配训练预算的 π0、π0.5 和 Cosmos Policy 分别为 36.7%、55.0% 和 12.5%。
- **论文结论**：作者认为组合泛化需要预测未来本身有用，也需要动作头在规划阶段实际依赖这些未来；固定增强可能在预测不可靠时放大错误。
- **可支撑判断**：该工作支持“动作对未来表示的依赖会随任务阶段变化，运行时选择性 guidance 可在一个实体平台的未见对象--容器组合上提高成功率”。它不支持跨机器人或开放分布泛化。
- **局限/待核验**：实体结果来自一个双臂 YAM 平台，没有报告置信区间或跨训练 seed；Cosmos Policy 在该多任务数据上未成功训练，削弱结构间比较；完整方法同时改变视频特征提取、联合训练和推理 guidance；guidance 每次重规划需要最多三次视频前向，降低控制频率，错误未来会被进一步放大。

## 4. Zero-WAM

- **身份**：Jiaming Zhou、Qihang Zhang、Gangwei Xu、Cunxin Fan、Yujie Zhao、Ruilin Wang、Yiming Luo、Shuai Yang、Xing Zhu、Yujun Shen、Junwei Liang、Yinghao Xu，*Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization*，arXiv:2608.26103v2，2026-08-27；预印本。原文：[arXiv HTML](https://arxiv.org/html/2608.26103v2)。
- **变化轴与接口**：因果视频--动作模型使用单段人类视频作为测试时任务说明，联合预测未来机器人视频与可执行动作。HumanGen 包含 74.2K 人类--机器人配对、覆盖 8.6K 任务；实体平台仍用少量已见任务数据适配机器人运动学。
- **主要证据**：七项未见 RoboTwin 任务每任务每 seed 100 次、3 seeds，Zero-WAM 平均 46.95%，LingBot-VA 为 17.45%，WAN-Action 为 10.98%。实体双臂 Franka 上评估未见对象--容器组合、三物体顺序操作和桌腿插入，每类报告 30 次试验；Zero-WAM 分别为 53.3%、33.3% 和 16.7%，语言条件 LingBot-VA 为 43.3%、10.0% 和 0%。
- **论文结论**：作者认为人类视频可作为开放任务的上下文接口，任务平衡预训练和未来块预测有助于从已见任务组合到未见配置的迁移。
- **可支撑判断**：该工作支持“人类视频提示可以指定未见任务配置，并在同一机器人平台上优于一个语言提示基线”。它不是零机器人数据学习：实体评测前仍使用 252 个已见任务人类--机器人配对适配该平台。
- **局限/待核验**：实体比较改变了提示模态，Zero-WAM 使用人类视频而基线使用详细语言，不能把差异归因于 WAM 结构；组件消融全部在仿真完成；实体只覆盖固定台面和一套双臂 Franka，绝对成功率仍低；没有跨机器人、跨操作者、动态场景或显著更长任务验证。

## 5. 综合判断

四项工作检验的不是同一种泛化。Sim-to-real WAM 改变训练环境，SCVC 改变相机，Temporal Ratio 重组对象与目标，Zero-WAM 改变任务配置与提示。它们共同支持把“泛化”写成变化轴、适配预算、闭环终点和试验分母的组合，而不是模型标签。当前仍没有同一 WAM 在多机器人、多操作者和真实开放分布上以统一协议复现的证据。
