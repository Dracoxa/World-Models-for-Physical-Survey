# 主张溯源索引

本页把正文的关键综合判断连接到代表性原始来源和本地证据提取记录。它用于核查论证边界，不按论文数量投票，也不表示已经穷尽相关研究。正文中的方法描述和数字仍以所引原始论文为准。

| 正文关键判断 | 代表性原始证据 | 当前可支撑范围 | 本地核验 |
|---|---|---|---|
| 离线预测质量、仿真闭环表现和实体闭环效用相关但不可互换。 | [Interactive World Simulator](https://arxiv.org/abs/2603.08546v1)分别测试视频指标、合成数据训练和策略排序；[Navigation World Models](https://openaccess.thecvf.com/content/CVPR2025/html/Bar_Navigation_World_Models_CVPR_2025_paper.html)在记录轨迹上用预测做规划；[NavWAM](https://arxiv.org/abs/2606.13494v1)报告小规模实体反馈闭环。 | 三项研究展示不同评价对象和协议，支持把预测、决策和实体执行分开报告；不能据此形成跨论文性能排名。 | [批次 01](EVIDENCE_BATCH_01.md#2-interactive-world-simulator)；[批次 06](EVIDENCE_BATCH_06_NAVIGATION_CLOSED_LOOP.md) |
| 系统收益常同时包含数据、表示、策略、规划和推理变化；归因于世界模型部件需要匹配控制。 | [WAV](https://arxiv.org/abs/2604.14732v2)提供同模型 latent planning 消融；[WorldSample](https://arxiv.org/abs/2607.02431v1)同时改变模型适配、奖励标注、样本选择和调度；[WorldSync](https://arxiv.org/abs/2608.24885v1)比较动作覆盖不同的模拟器，但实体分母未报告。 | 同系统消融可以支持局部增量判断；多组件系统的总收益不能自动归因给预测器或单一训练目标。 | [批次 01](EVIDENCE_BATCH_01.md#5-world-value-action-model)；[批次 09](EVIDENCE_BATCH_09_INTERACTIVE_IMPROVEMENT.md) |
| 安全证据包含条件性保证、经验降风险、离线监测、在线干预和恢复，不能压成单一强度等级。 | [Berkenkamp et al.](https://proceedings.neurips.cc/paper/2017/hash/766ebcd59621e305170616ba3d3dac32-Abstract.html)在假设下给出稳定性保证；[Foresight](https://arxiv.org/abs/2606.23085v1)离线评估失败检测；[FEARL](https://arxiv.org/abs/2606.23754v1)在 18 个实体导航回合中测试护盾；[Dream2Fix](https://arxiv.org/abs/2603.13528v1)用世界模型生成恢复数据并评估实体纠正。 | 每项证据只支持其假设、风险定义、响应接口和试验分母；离线报警不等于事故减少，小样本零碰撞不等于开放世界保证。 | [批次 02](EVIDENCE_BATCH_02_SAFETY.md)；[批次 03](EVIDENCE_BATCH_03_RUNTIME_SAFETY.md)；[批次 08](EVIDENCE_BATCH_08_CALIBRATION_INTERVENTION.md)；[批次 10](EVIDENCE_BATCH_10_RECOVERY_RESUMPTION.md) |
| 数据集、策略、安全层和恢复系统可作为支撑资源或边界对照，但不因进入同一机器人流程就成为世界模型。 | [DROID](https://www.roboticsproceedings.org/rss20/p120.html)提供实体示范数据；[KnowNo](https://proceedings.mlr.press/v229/ren23a.html)把不确定性连接到求助；[AgentChord](https://arxiv.org/abs/2605.11951v1)用预编译任务图完成故障后续接。 | 这些工作可界定训练条件、求助代价和恢复终点；它们不作为世界模型方法数量或世界模型效果证据。 | [检索协议第 4 节](SEARCH_PROTOCOL.md#4-纳入与排除口径)；[批次 08](EVIDENCE_BATCH_08_CALIBRATION_INTERVENTION.md)；[批次 10](EVIDENCE_BATCH_10_RECOVERY_RESUMPTION.md) |
| 推理器审查或修改策略动作，不等于系统已经暴露可查询的未来状态预测。 | [GPT 6 Astra as an Embodied Policy](https://github.com/anonymous-report-421/GPT-as-Policy)比较直接控制与策略提案纠正；[Unexpected Robot Policy](https://arxiv.org/abs/2609.24170v1)扩大任务覆盖；[Galbot 扩展稿](https://arxiv.org/abs/2609.38537v1)复用部分混合实验；[FLUX 3 Action](https://bfl.ai/models/flux-3-action)报告提案审查接口。 | 现有材料支持讨论动作生成、审查、编辑和推理时延；没有隔离显式后果预测，因此不能把混合收益直接归因于 world-model rollout。 | [Astra 来源与重合说明](README.md#本轮新增讨论入口)；正文第 3 部分 Astra 专题 |

## 使用规则

1. 表中来源是代表性支点，不是完整纳入列表；完整检索边界见[检索协议](SEARCH_PROTOCOL.md)和[检索日志](SEARCH_LOG.md)。
2. 定量陈述必须同时保留任务、平台、试验分母、比较对象和来源位置；缺失项不得自行补齐。
3. 新证据若改变上述判断，应先更新对应证据批次，再修改本页和正文，避免只改结论不改证据链。
