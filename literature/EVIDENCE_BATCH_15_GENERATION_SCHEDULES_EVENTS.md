# 原文核验批次 15：递归驾驶、生成调度与事件级执行

更新：2026-10-02。范围：R22 第二队列中的 DriveWAM、NoiseGate、DAWN、WALL-WM 与 ADriver-I。五篇均按当前 arXiv 版本处理。本批次关注预测在推理时如何进入动作生成：作为先生成的未来、反复更新的 latent、可学习的去噪门控、事件级执行单元，或递归生成环境。不同论文的驾驶指标、仿真成功率和实体 Task Progress 不做横向排名。

## 1. DriveWAM

- **身份**：Chen Shi 等，*DriveWAM: Video Generative Priors Enable Scalable World-Action Modeling for Autonomous Driving*，arXiv:2605.28544v1，2026-05-27；原文：[arXiv HTML](https://arxiv.org/html/2605.28544v1)。
- **预测与接口**：以 Wan2.2-TI2V-5B 为视频骨干，将历史视频与 ego action 组织成因果时序。每个推理块先生成未来视频 latent，再以该生成 latent 为条件解码动作；新真实观测到达后重新锚定历史。冻结的 Qwen3-VL-8B 提供分块语义引导，选择性 KV memory 以相关性和冗余度维持有界的视频、动作缓存。
- **主要证据**：NAVSIM v1 报告单前视相机 PDMS 90.1，但该基准是数据驱动的 non-reactive predictive-driver-model 评价。PhysicalAI-AV 使用真实驾驶日志，论文从 1,700 小时、306,152 个 20 秒片段中选择 100k 训练片段，并自建 1,000 片段测试子集；DriveWAM 的 4 秒 ADE/FDE 为 0.83/2.47。相同 100k、50k iteration 设置下，无预训练但保留视频监督为 1.10/3.26，保留预训练但移除视频监督为 1.23/3.79，两者均有时为 0.83/2.47。全 KV、FIFO 与选择性记忆的 4 秒 ADE/FDE 分别为 0.83/2.47、1.40/3.47、0.89/2.52；选择性记忆将 300 秒 profile 的缓存从 3.07 GB 降到 0.25 GB。
- **可支撑判断**：DriveWAM 提供了“生成的未来 latent 直接作为动作读出条件”以及“长时历史以有界记忆参与后续预测”的明确系统接口；其部件实验支持预训练视频初始化、继续视频监督和选择性记忆在本协议中的联合价值。
- **局限 / 待核验**：没有真实车辆闭环试验。PhysicalAI-AV 只评估日志上的轨迹误差，外部基线的训练数据量和模型规模不同；1,000 片段测试集由作者使用 VLM 标签和兴趣分数筛选，不是官方完整测试集。预训练与视频监督消融没有在保持其余动作架构完全一致时单独替换“生成未来”为 oracle、空白或停止梯度条件，因此不能把全部增益归因于推理时未来生成。4k--100k 片段均训练 50k iteration，也不构成严格 scaling law。
- **证据位置**：第 3.1--3.3、4.1--4.4 节；表 1--5；附录 A--C。

## 2. NoiseGate

- **身份**：Wen Huang 等，*NoiseGate: Learning Per-Latent Timestep Schedules as Information Gating in World Action Models*，arXiv:2605.07794v1，2026-05-08；原文：[arXiv HTML](https://arxiv.org/html/2605.07794v1)。
- **预测与接口**：在联合视频--动作 MoT 中，为每个未来视频 latent 分配独立扩散时间，而动作 token 保持统一全局时间。第一阶段以独立噪声训练 WAM；第二阶段冻结 WAM，仅用 GRPO 和仿真任务成功奖励训练 Gating Policy Network，决定每个未来 latent 在每一步被“揭示”多少。
- **主要证据**：RoboTwin random-scene 主比较采用 Fast-WAM 风格、batch 1024 配置，50 个任务各 100 episode；Stage-1 WAM 平均成功率 92.58%，NoiseGate 为 94.28%，提高 1.70 个百分点。受控调度消融使用较小的 Motus-derived、batch 128 配置和 15 个任务：共享时间为 57.5%，独立噪声 Stage-1 为 61.3%，手工单调调度为 63.4%，学习调度为 67.5%。GRPO 使用单一 seed 42、50 个 epoch、每 epoch 8 个 episode、8 个 rollout worker。
- **可支撑判断**：在同一冻结 WAM 之上，任务奖励训练的 per-latent 调度可改变未来视频 latent 对动作生成的有效信息量，并在该仿真协议中带来小幅主结果提升；受控小规模实验进一步支持独立噪声训练与学习调度的组合价值。
- **局限 / 待核验**：主比较与 15 任务消融使用不同训练规模，不能把 10.0 点消融差值与 94.28% 主结果拼成同一设置。论文只报告一个随机种子，没有方差或显著性；任务共享、训练 seed 和 episode 相关性使 1.70 个百分点不能自动视为稳健增益。第二阶段依赖在线仿真 rollout 和稀疏成功奖励，不是无交互的推理优化。没有真实机器人验证，作者也将大规模多任务通用调度留作未来工作。
- **证据位置**：第 3--5 节；表 1--2；附录 A、D、E。

## 3. DAWN

- **身份**：Hongbo Lu 等，*The DAWN of World-Action Interactive Models*，arXiv:2605.11550v1，2026-05-12；原文：[arXiv HTML](https://arxiv.org/html/2605.11550v1)。
- **预测与接口**：将当前视觉压缩为少量语义 latent，先由动作去噪器生成轨迹假设，再由动作条件的 World Predictor 展开短 latent future，反过来继续修正动作；默认重复四轮。其核心不是完整像素 rollout，而是动作和世界假设在推理时递归共演化。
- **主要证据**：NAVSIM v1 的低分辨率消融从无 resampler/predictor/interaction 的 PDMS 82.9，变为仅 resampler 82.8、加 predictor 85.2、再加交互更新 87.9。移除 world-to-action 与 action-to-world 两个方向时，PDMS 分别为 81.6 和 84.9，完整模型为 87.9。0/1/2/3/4 秒 latent rollout 的 PDMS 为 82.8/84.7/87.3/87.5/87.9，时延从 331 ms 增至 1,068 ms。主模型在 NAVSIM v1 报告 PDMS 89.1；nuScenes 离线规划平均 L2 0.33 m、碰撞率 0.11%。但 NAVSIM v2 的 EPDMS 为 83.2，低于表中多个 perception-based baseline。
- **可支撑判断**：在该驾驶模型和 NAVSIM v1 设置内，显式短 latent rollout 与双向世界--动作更新分别提供可测的规划增益；2--3 秒 rollout 已接近 4 秒结果，展示了预测深度与时延的内部权衡。
- **局限 / 待核验**：没有真实车辆闭环或道路部署。NAVSIM 使用真实日志和模拟规则指标，nuScenes 为开环轨迹评价；碰撞率、TTC 或可视化不能改写为部署安全证明。论文未给多 seed 方差、显著性或正式收敛/安全保证。NAVSIM v2 的聚合结果和碰撞相关分项弱于最强基线，说明 v1 结论不能无条件外推。80 张 A100 的完整训练和约 1 秒的 4 秒 rollout 时延也限制实时部署解释。
- **证据位置**：第 2.2--3.4、7、10.1--10.2 节；表 1--10。

## 4. WALL-WM

- **身份**：Shalfun Li 等（X Square Robot Team），*WALL-WM: Carving World Action Modeling at the Event Joints*，arXiv:2606.01955v2，2026-09-06；原文：[arXiv HTML](https://arxiv.org/html/2606.01955v2)。
- **预测与接口**：以语义事件而非固定时长 chunk 作为视频--动作预训练单元。事件模式接收 next-event 描述并输出可变长执行段；统一模式使用 VLM Staircase Decoding 支持固定长动作块。训练还包括多视角交互、事件级 caption、cluster-balanced sampling、恢复/接管数据和大规模视频先验。
- **主要证据**：实体评价覆盖 Diverse Manipulation、Reasoning Manipulation、Dexterous Manipulation 和 Generalization 四组任务，以 0--100 Task Progress 而非二元成功为主指标。控制预训练不变、同时移除 VI-SA 和事件执行格式的联合消融中，Reasoning 平均分从 32.6 增至 71.6，Generalization 从 22.0 增至 53.75。事件模式相对从头训练的统一模式在 Diverse、Reasoning、Dexterous 和 Generalization 的平均分分别为 75.86 vs. 63.00、71.60 vs. 59.50、32.00 vs. 31.25、53.75 vs. 18.50。另在 RoboTwin 50 任务、每任务 10 episode 的 zero-shot 仿真中成功 76/500，即 15.2%。
- **可支撑判断**：该系统把事件粒度明确实现为视频预测、语言条件和动作执行的共同接口，并在内部实体平台上显示事件模式与多视角机制的组合优势；较低的 dexterous 分数也表明高层事件分解不能替代精细接触控制。
- **局限 / 待核验**：实体表没有报告每项 Task Progress 的试验次数、随机种子、方差或置信区间；分段部分分依赖作者定义的 rubric，不能与成功率等同。关键消融同时改变 VI-SA 和执行格式，无法将增益单独归因于事件建模；与从头训练基线的差异还包含大规模预训练。评价使用内部平台及与其对齐的数据，作者明确承认平台和调参资源优势。当前是大规模团队预印本，数据总量和完整复现条件未充分公开。
- **证据位置**：第 3--5、7.1--7.2、8 节；表 2--7；附录 9.5。

## 5. ADriver-I

- **身份**：Fan Jia 等，*ADriver-I: A General World Model for Autonomous Driving*，arXiv:2311.13549v1，2023-11-22；原文：[arXiv HTML](https://arxiv.org/html/2311.13549v1)。
- **预测与接口**：MLLM 根据历史视觉--动作对和当前图像预测速度、转角；独立训练的视频扩散模型再以该动作的文本描述为条件生成后续四帧。推理时可以交替预测控制和生成图像，形成早期的 interleaved action--video 递归循环。
- **主要证据**：模型使用约 1.4M 条私有高速公路视觉--动作对预训练，并在约 23k 个 nuScenes 视频样本上微调视频模型。nuScenes 上 ADriver-I 的速度/转角 L1 为 0.072 m/s 与 0.091 rad，ViT 基线为 0.103 与 0.092；未来四帧的 FID/FVD 为 5.5/97.0。多轮监督相对单轮仅将速度 L1 从 0.078 降到 0.072，转角由 0.094 降到 0.091。论文用一组递归生成序列定性展示动作影响视频、生成视频再影响下一动作。
- **可支撑判断**：ADriver-I 是较早将低层控制预测与动作条件视频生成交替串联的驾驶实例，适合说明后续联合 WAM 之前的模块化递归接口。
- **局限 / 待核验**：没有真实车辆或交互式模拟器闭环结果；所谓持续驾驶只在模型自己生成的图像中定性展示，没有任务完成、碰撞、路线或稳定性指标。控制和视频模块分开训练，量化控制表并未隔离未来视频是否改善后续动作。视频基线的条件、预测长度和输入先验不同，FID/FVD 不宜横向排名。私有数据集中在高速公路且更大、更简单，作者也明确表示尚不适合部署、缺少路线信息且快速动作变化时生成质量下降。
- **证据位置**：第 3.2--4.5、5 节；表 2--6；图 6--7。

## 批次综合

五篇工作把“未来如何进入动作”细化为五个不同设计轴：DriveWAM 的先未来后动作和有界历史、NoiseGate 的 latent 可靠性调度、DAWN 的世界--动作递归修正、WALL-WM 的事件级时间单位，以及 ADriver-I 的模块化视觉--动作交替生成。能够支持的结论主要来自同模型内部的部件消融；无法支持的是跨论文性能排名、真实道路安全、事件机制的单因素归因，或把模型内递归视频当成物理闭环。综述正文据此讨论接口设计，而不是将这些系统合并成一个统一“世界动作模型”强度等级。
