# 原文核验批次 12：CVPR 2026 物理表示与规划边界

更新：2026-10-02。范围：R19 中尚未深查的 5 篇 CVPR 2026 官方论文。该批次是定向证据提取，不是完整 venue census，也不据发表状态推高证据强度。

## 1. Dexterous World Models

- **身份**：Byungjun Kim 等，CVPR 2026，官方论文页：[CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html)。
- **预测与接口**：视频扩散模型输入已知静态 3D 场景沿相机轨迹的渲染和第一视角手部网格轨迹，预测交互造成的视觉残差。候选手部动作可分别生成结果，再以 VideoCLIP 文本相似度或末帧 LPIPS 排序。
- **主要证据**：视频 benchmark 共 144 个样本，包括 48 个留出的 TRUMANS 动态相机样本、48 个 TASTE-Rob 静态相机样本和 48 个 Aria 动态相机样本；每个样本生成 3 次并取平均。表 1 报告 DWM 在三个子集的所列视频指标上优于比较方法。
- **可支撑判断**：静态场景渲染与像素对齐的手部轨迹可以形成可查询的视觉后果接口；该接口可以用于候选手部运动的目标匹配。
- **局限 / 待核验**：动作排序只在图 7 给出定性示例，没有任务成功率、重复试验或真实执行；输入是人体手部轨迹和已重建场景，不是机器人控制量。不能据此推出闭环机器人规划有效。
- **证据位置**：第 3.4、4、4.2 节；表 1--3；图 7。

## 2. Physical Object Understanding with a Physically Controllable World Model

- **身份**：Rahul Venkatesh 等，CVPR 2026，官方论文页：[CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Venkatesh_Physical_Object_Understanding_with_a_Physically_Controllable_World_Model_CVPR_2026_paper.html)。
- **预测与接口**：7B GPT 式自回归模型在局部 RGB、光流、相机与指针 token 上学习任意条件分布；训练使用 300 万段真实 RGB 视频，约 1.4 万亿 token。稀疏光流 patch 作为虚拟 poke，用于查询局部干预后的运动分布。
- **主要证据**：点提示 SpelkeBench 中，PhyWM 的 AR / mIoU 为 0.541 / 0.681；DragAMove 部件 mIoU 为 0.410，高于所列 FPT 的 0.287 和 MotionI2V 的 0.073。无提示分割并非所有指标最优，例如 AP 低于 ProMerge，AR 和 mIoU 低于 SAM2。
- **可支撑判断**：对预测分布进行局部视觉干预，可以提取可动物体、关节部件与支撑关系等结构。
- **局限 / 待核验**：论文明确将光流与相机条件称为真实动作数据的廉价代理；虚拟 poke 不是标定力或电机命令，3D 编辑也不是实体操作。不能据此推出模型掌握机器人动作动力学或闭环控制。
- **证据位置**：第 2、3、4.3--4.7 节；表 1；图 2、4--6。

## 3. PhysInOne

- **身份**：Siyuan Zhou 等，CVPR 2026，官方论文页：[CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_PhysInOne_Visual_Physics_Learning_and_Reasoning_in_One_Suite_CVPR_2026_paper.html)。
- **数据与任务**：153,810 个合成动态 3D 场景、200 万视频、71 类力学/光学/流体/磁学现象；每个场景包含 12 个静态视角和 1 个移动视角，并提供几何、语义、运动、物性和文本标签。数据按 8:1:1 划分，3D 资产只属于一个划分。
- **主要证据**：视频生成实验使用 83,650 对训练样本和 772 个小测试样本。表 2 的收益依模型与微调方法而异：SVD 的 SFT 将 PMF 从 2.753 提至 3.147，但 SVD 的 LoRA/FLT 更低；CogVideoX LoRA 的 PMF 为 2.869，略低于基础模型的 2.877。长、短期预测使用 103 个场景，物性估计只使用 20 个场景。
- **可支撑判断**：PhysInOne 提供资产隔离、可控多视角和密集物理标签，可用于测试合成域内的视觉物理学习。
- **局限 / 待核验**：全部数据由 UE5 Chaos、Taichi MPM 和 Doriflow SPH 等模拟器生成，作者也承认模拟器并非完全物理保真；没有机器人动作、实体场景或真实传感器验证。不能把部分微调收益概括为所有模型一致改善，更不能推出真实 Physical AI 可迁移性。
- **证据位置**：第 3、4.1--4.3 节；表 2--5；附录的数据与模拟设置。

## 4. GeoWorld

- **身份**：Zeyu Zhang 等，CVPR 2026，官方论文页：[CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_GeoWorld_Geometric_World_Models_CVPR_2026_paper.html)。
- **预测与接口**：Hyperbolic JEPA 学习双曲 latent，几何强化学习调整能量函数；CEM 以 800 个样本、80 个 elite 和 10 次迭代搜索程序动作标签序列。
- **主要证据**：CrossTask 含 4.7K 视频、83 个任务和 105 个动作标签；COIN 含 11,287 个视频、180 个任务和 778 个动作标签。匹配的 ViT-g384 视频设置中，GeoWorld 相对 V-JEPA 2 的 SR 在 CrossTask T=3/T=4 从 50.16/35.01 提至 51.71/37.04，在 COIN 从 42.74/31.63 提至 45.29/33.29。图像设置的增益更不均匀。
- **可支撑判断**：在这两个教学视频数据集上，几何化 latent 与能量规划可以提高标注程序步骤的匹配率，尤其可作为长时程序规划的表示案例。
- **局限 / 待核验**：动作是教学视频中的离散步骤标签，指标是与标注序列的 SR、mAcc 和 mIoU，不是机器人执行成功；没有实体、动力学或控制频率验证。不能把该结果表述为物理动作规划已验证。
- **证据位置**：第 3.2、3.3、4.1--4.5 节；表 1--3。

## 5. ModularAgent

- **身份**：Yu-Wei Zhan 等，CVPR 2026，官方论文页：[CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Zhan_ModularAgent_A_Task-Aware_Modular_Framework_for_Joint_Optimization_of_Multimodal_CVPR_2026_paper.html)。
- **预测与接口**：以 RSSM 为动力学核心，在 MLLM 与世界模型之间进行任务感知融合，并用文本条件奖励联合优化 imagined behavior。
- **主要证据**：实验只覆盖 DeepMind Control Suite 的 Cheetah、Walker、Quadruped 与 Stickman 离线 locomotion 数据。表 1 以 10 个随机种子报告归一化 episodic reward：总体为 0.91±0.02，高于 FOUNDER 的 0.87±0.03；但 Cheetah run 上 FOUNDER 为 0.81±0.02，高于 ModularAgent 的 0.79±0.02。主要组件消融只在 Walker 的三个任务进行。
- **可支撑判断**：在所测 DMC 设置内，语义表征与 latent dynamics 的双向联合优化可以作为多任务控制接口的一种实现。
- **局限 / 待核验**：没有真实图像、机器人平台、接触操作或实体部署，跨环境结果也受同一套仿真任务家族限制。该工作暂不进入正文核心论证，仅作为“仿真语义--动力学耦合”候选保留。
- **证据位置**：第 3、4.1--4.4 节；表 1--2；图 3。

## 批次综合

这五篇不应被合并成同一类“机器人世界模型进展”。DWM 提供手部轨迹到视觉后果的候选比较；PhyWM 用视觉代理干预提取物理结构；PhysInOne 是合成数据与 benchmark；GeoWorld 评估教学视频中的程序步骤规划；ModularAgent 评估 DMC latent control。它们分别补足数据、表示、查询和规划边界，但没有一篇同时证明真实机器人动作条件、闭环规划和跨场景可靠性。
