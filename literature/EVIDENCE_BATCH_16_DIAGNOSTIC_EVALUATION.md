# 原文核验批次 16：诊断评估、鲁棒性与预测完整性

更新：2026-10-02。范围：第二轮增量候选中直接补充评估、安全与 Benchmark 论证的 6 篇论文。本批次区分真实机器人评测、仿真闭环、离线诊断和白盒攻击；不同任务、训练配方和指标不做横向排名。

## 1. WorldLens

- **身份**：Ao Liang 等，*WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World*，CVPR 2026 Oral；正式入口：[CVF Open Access](https://openaccess.thecvf.com/content/CVPR2026/papers/Liang_WorldLens_Full-Spectrum_Evaluations_of_Driving_World_Models_in_Real_World_CVPR_2026_paper.pdf)，开放扩展稿为 arXiv:2512.10958v2。
- **评价对象与接口**：把驾驶世界生成拆成 Generation、Reconstruction、Action-Following、Downstream Task 和 Human Preference 五个方面、24 个维度。Action-Following 既比较生成视频与真实视频诱导的轨迹，也把生成视频送入预训练驾驶策略，在非反应式和反应式生成模拟器中评价。
- **主要证据**：位移误差在 nuScenes 验证集 150 个场景上计算。生成模拟器覆盖两个地图环境和 5 条验证序列，交通引擎为 10 Hz、控制信号为 2 Hz；闭环时策略输出更新 ego 状态，世界模型再生成下一帧。被测模型中最高 Route Completion 仅为 13.51%，相应 Arena Driving Score 为 0.106，说明视觉可用性与长时闭环仍有明显差距。WorldLens-26K 另收集人类数值评分与文本理由，用于训练评价代理。
- **可支撑判断**：正式 benchmark 将视觉质量、几何重建、动作跟随、下游感知和人类判断分开，并提供了生成内容进入闭环驾驶模拟器的功能性终点；它支持“世界模型评价不能只看视频外观”。
- **局限 / 待核验**：所谓闭环发生在生成式驾驶模拟器，不是道路车辆试验。位移、PDMS、Route Completion 和 ADS 依赖固定的预训练策略、地图、交通引擎和 5 条序列；不能据此认证真实驾驶安全。评价代理继承基础模型与标注偏差，WorldLens-26K 的视觉偏好也可能受地区与风格影响。当前范围只覆盖驾驶。
- **证据位置**：正式论文第 3、9--13 节；图 2；表 16--19、24--29；arXiv 扩展稿第 13.3 节。

## 2. ManipArena

- **身份**：Yu Sun 等，arXiv:2603.28545v2，当前摘要页题名为 *ManipArena: Comprehensive Real-world Evaluation of Reasoning-Oriented Generalist Robot Manipulation*；v2 HTML/PDF 内仍显示早期题名 *A Controlled Benchmark for Diagnosing Generalization in Real-Robot Manipulation*，因此以标识符和版本锁定该 publication family。原文：[arXiv](https://arxiv.org/abs/2603.28545v2)。
- **评价对象与接口**：20 个实体任务包含 15 个桌面任务和 5 个移动操作任务，数据集有 10,812 条专家轨迹、13.5M 帧和约 188 小时。桌面任务采用固定 10 次试验：4 次 ID、4 次受控 shift、2 次最强 held-out 条件，并按子目标给部分分。
- **主要证据**：七种桌面配置在 15 个任务上至少形成 1,050 次实体试验。最佳汇总配置为 task-specific WALL-OSS-0.5，得分 950.8/1500、成功率 38%；统一训练的 WALL-WM 为 868/1500、31.33%。相同架构内，$\pi_{0.5}$ 的 200 条/任务子集优于更大数据配方；语言粒度和单任务/多任务微调也显著改变排序。作者据此将结果解释为架构、预训练来源、数据采样、微调和标注共同作用，而不是 WAM 类别本身的优势。
- **可支撑判断**：ManipArena 提供了当前较完整的实体机器人、分层 shift 与部分完成度协议，并直接显示训练配方足以改变模型族排序；它适合支撑“benchmark 必须固定数据、任务共享和语言条件后再做归因”。
- **局限 / 待核验**：每任务只有 10 次实体试验，held-out 仅 2 次，作者也承认需要更多重复。移动操作只评价一个 scoped $\pi_{0.5}$ 配置，Real2Sim 只覆盖 3 个任务；平台、受控环境和 L1 指令接口限制外推。跨架构表仍包含不同预训练来源，不能用于证明 WAM 普遍优于 VLA。
- **证据位置**：第 3.1--3.5、4.1--4.5、5 节；表 2--4、8--11；附录 M--N。

## 3. Beyond Task Success

- **身份**：Geonmyeong Lee、Byoung-Tak Zhang，*Beyond Task Success: Stage-Wise Reliability of World Model Planning under Sensing Degradation*，arXiv:2609.07126v1，2026-09-07；论文标注 RLWM workshop，按预印本处理。原文：[arXiv HTML](https://arxiv.org/html/2609.07126v1)。
- **评价对象与接口**：在 DINO-WM 的 OGBScene Drawer 任务上，对同一组 50 个可重规划 start--goal 任务施加 10 种视觉或时间退化，依次追踪表示变化、未来预测残差、共享 300 个候选上的 planner preference，以及最终仿真任务结果。次级实验在 OGB-Cube 上比较 DINO-WM 与 LeWM。
- **主要证据**：干净条件成功率为 60%；低照、过曝和运动模糊分别为 52%、50% 和 52%，Delay-5/10 的点估计为 66%。这些条件在表示、预测和候选排序上的相对顺序没有保持到结果层；所有主条件的配对 95% 置信区间均包含 0，论文明确不把点差解释为优劣或等价。恢复最新观测的开发集反事实使 10 对中 7 对的 planner decision 更接近干净条件，但没有继续执行以验证任务恢复。
- **可支撑判断**：该工作支持“单一内部预测指标或最终成功率都不足以定位 sensing degradation 在多阶段 planner 中的传播位置”，并提供了配对任务和共享候选池的诊断范式。
- **局限 / 待核验**：全部是 OGBench 中的合成退化和仿真任务，不是实体传感故障。主结果只有 50 个固定任务，次级任务只保留干净条件可解样本；恢复分析是同一物理状态下替换历史的反事实，不证明后续轨迹或任务恢复。工作没有实现缓解方法。
- **证据位置**：第 3--5 节；图 1--3；表 1--2。

## 4. Test-Time Scaling with Geometric Verification

- **身份**：Zesen Zhao 等，arXiv:2607.17454v1，2026-07-20。arXiv 摘要页题名使用 *Zero-Shot Geometric Evaluation*，HTML/PDF 使用 *Zero-Shot Geometric Verification*；本批次保留标识符并记录该元数据差异。原文：[arXiv](https://arxiv.org/abs/2607.17454v1)。
- **预测与决策接口**：固定预算 GeoBoN 从同一 WAM 采样多个未来--动作 rollout，用冻结几何模型的跨视角深度重投影误差选出一个动作块；动作--未来一致性 gate 仅在初始 rollout 可疑时触发额外采样。
- **主要证据**：RoboCasa、LIBERO Long 和 RoboTwin 2.0 共 5 个 benchmark--backbone 设置，每个设置用 4 个 seed；LIBERO 每任务每 seed 50 次 rollout，另两个 benchmark 为 10 次。$N=8$ GeoBoN 在 5 个设置均提高汇总成功率，例如 Cosmos Policy 在 RoboCasa 从 66.3% 到 68.4%，X-WAM 从 80.8% 到 82.5%。gate 平均只在 26.2% 决策点触发并保留 74.8% 的 always-on 增益；但 Cosmos Policy 的平均延迟由 0.90 s 增到 1.29 s，always-on 为 3.65 s。部分任务类别下降，且 $N$ 增大可能选中虚假的低重投影异常值。
- **可支撑判断**：在这些仿真策略与公开 checkpoint 上，预测未来可被外部几何一致性用于候选动作重排，选择性 gate 能在成功率与额外计算之间形成可测权衡。
- **局限 / 待核验**：没有实体机器人。外部几何模型、相机标定和多视角预测是必要条件；不同 WAM 使用各自公开 checkpoint，绝对结果不用于模型排名。改善通常为 1--2 个百分点，个别任务和更大候选池会退化；门控仍增加延迟，不能自动满足实时控制预算。
- **证据位置**：第 3、4.1--4.5 节；表 1--5；图 2--3。

## 5. Trusted Imagination Attack

- **身份**：Linghan Chen、Kaiyan Ji、Minyu Guo，*Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models*，arXiv:2606.22966v1，2026-06-22；预印本。原文：[arXiv HTML](https://arxiv.org/html/2606.22966v1)。
- **威胁模型与接口**：白盒攻击者只扰动当前相机观测，通过可微 observation--imagination 映射修改未来 latent；下游 safety gate、MPC 或 verifier 将该 latent 当作可信预测。论文同时报告 reactive policy 作为负对照。
- **主要证据**：在 LIBERO-10 上，untargeted latent corruption 在 5 个任务中最高约为同幅随机扰动的 60 倍；但 targeted cross-scene steering 在 8 个任务上没有改变解码场景或 verifier。Reactive policy 聚合 143--190 个 episode 后几乎不受 oracle-level imagination 攻击影响。唯一端到端闭环失败来自 LaDi-WM sampling MPC 的单个任务：每个扰动强度 20 次，$\epsilon=0.01$ 时随机扰动成功率为 14/20，而 adversarial 为 1/20，Fisher $p<10^{-4}$。
- **可支撑判断**：预测分支被下游 verifier 或 planner 信任时形成独立完整性攻击面；同时，latent 偏移并不必然改变 reactive policy，安全评价必须测到具体 downstream consumer。
- **局限 / 待核验**：闭环失败只覆盖一个仿真任务、每条件 20 次，不能外推到实体机器人或黑盒攻击。攻击假设知道模型与编码器；观测攻击共享直接视觉与 imagination-refinement 编码路径，不能完全把失败归因于 imagination。作者早期小样本的灾难性 availability 结论在 179 样本复核后降为轻微但显著的损失，说明小样本攻击结果尤其需要谨慎。
- **证据位置**：第 3、5.1--5.9、6--8 节；表 1、3--10；图 3--5。

## 6. WAM--VLA Robustness Study

- **身份**：Zhanguang Zhang 等，*Do World Action Models Generalize Better than VLAs? A Robustness Study*，arXiv:2603.22078v5，2026-07-30；预印本。原文：[arXiv](https://arxiv.org/abs/2603.22078v5)。
- **评价对象与接口**：RoboTwin 2.0-Plus 在 50 个双臂任务上设置 camera、robot initial state、language、light、background、noise 和 layout 七类扰动，每类每任务 50 个 episode；另汇总 LIBERO-Plus 单臂结果。比较 VLA、辅助预测、混合架构与 WAM checkpoint，并记录推理时延。
- **主要证据**：RoboTwin 2.0-Plus 中 LingBot-VA 汇总 74.2%、Fast-WAM 72.7%、MOTUS 71.5%、$\pi_{0.5}$ 58.6%，但 camera 和 robot-initial-state 对 WAM 仍困难。LIBERO-Plus 中 $\pi_{0.5}$ 为 85.7%，高于 Cosmos Policy 的 82.2%。同一设备的部分时延比较中，$\pi_{0.5}$ 为 63 ms，GE-Act 300 ms、Cosmos Policy 390 ms、MOTUS 1175 ms、LingBot-VA 的 RoboTwin 配置 5230 ms；Fast-WAM 的 190 ms 来自原论文硬件而非重测。
- **可支撑判断**：该研究显示 WAM 的鲁棒性并非跨扰动和跨 benchmark 一致，camera/robot geometry 与生成式去噪时延仍是独立问题；“是否使用世界模型”不足以解释全部排序。
- **局限 / 待核验**：所有评价为仿真。模型训练数据、预训练来源、微调实现和 denoising steps 不匹配；LIBERO 表还混合本轮重测、既有 benchmark 数字和论文自报结果。Fast-WAM 两个 benchmark checkpoint 的训练数据多样性不同。因而表格适合描述协议内的鲁棒性轮廓，不能因模型类别差异推出 WAM 的因果泛化优势。
- **证据位置**：第 3.1--4 节；表 2--5；附录 A--C。

## 批次综合

六篇工作把评估拆成四类互补终点：WorldLens 与 ManipArena 分别覆盖生成世界的功能用途和实体策略的受控比较；stage-wise reliability 与 WAM--VLA robustness study 诊断退化传播和扰动轮廓；GeoBoN 直接测试预测候选能否改善动作选择；trusted-imagination attack 检查预测被下游消费者信任后的完整性风险。可支持的共同结论是评估必须绑定预测的实际消费者、任务环境和控制预算。不能支持的是把模拟闭环等同于道路或实体安全、从异配模型排行榜推断 WAM 类别优势，或由单任务白盒攻击声称普遍脆弱。
