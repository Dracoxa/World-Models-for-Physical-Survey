# 写作状态 · 2026-10-02

## 本轮进展（v0.2）

- 已建立 ACM `acmart` / `CSUR` 项目和四部分正文文件。
- 四部分已有连贯第一轮内容，保留摘要、引言、概念边界与 Astra 专题。
- 扩写数据、模型、规划、想象学习、联合动作生成、评估和安全；仍需更多技术细节与领域实例。
- 新增 7 张 LaTeX 比较表，连同 Astra 表共 8 表；正文参考文献从 8 条增至 76 条。
- 新增[同类开源调研与差异化定位](RELATED_SURVEYS.md)，并将 2026 年已发表、与 Physical AI 控制视角高度重合的综述纳入正文定位比较。
- 已将 NTUMARS、Li-Zn-H、OpenMOSS 三个高相关开源库与 929 条目录按 arXiv ID 和题名去重，新增候选及优先级见[外部调研库去重结果](literature/EXTERNAL_CANDIDATES.md)。
- 已对最高优先级中的 OmniVTA、Interactive World Simulator、World-VLA-Loop、TesserAct 和 WAV 完成原文级快速核验，并将证据、可支撑判断和局限写入[核验批次 01](literature/EVIDENCE_BATCH_01.md)。
- 已核验 5 篇安全原始来源，将形式保证、仿真中的经验降风险和无实证的架构提案分开记录，详见[核验批次 02](literature/EVIDENCE_BATCH_02_SAFETY.md)。
- 已补 3 篇含实体试验的运行时安全工作和 1 篇 2026 perspective，记录干预接口、实体分母与保证边界，详见[核验批次 03](literature/EVIDENCE_BATCH_03_RUNTIME_SAFETY.md)。
- 已核验 ContactWorld、TouchWorld、DexTouch-WM、ParticleFormer 与 MVISTA-4D，区分触觉感知、未来预测、快速反馈、动作条件前向模型和未来到动作反演，详见[核验批次 04](literature/EVIDENCE_BATCH_04_CONTACT_STRUCTURED.md)。
- 已核验 Drive-WM、OccWorld、Drive-OccWorld、DriveVLA-W0 与 NavForesee，区分推理时候选 rollout、联合场景--轨迹预测和训练时预测监督，详见[核验批次 05](literature/EVIDENCE_BATCH_05_NAVIGATION_DRIVING.md)。
- 已核验 NWM、DreamerNav、NavThinker 与 NavWAM，区分离线显式规划、latent policy、候选动作 look-ahead 与联合世界--动作闭环；实体证据分母与局限见[核验批次 06](literature/EVIDENCE_BATCH_06_NAVIGATION_CLOSED_LOOP.md)。
- 已核验 Mem-World、WorldScape Policy 2.0、FARL、ViFailback 与 LIBERO-Recover，区分记忆保持、进度跟踪、提前避险、失败后纠正和状态恢复；见[核验批次 07](literature/EVIDENCE_BATCH_07_MEMORY_RECOVERY.md)。
- 已核验 Foresight、KnowNo、CoFineLLM 与 ThriftyDAgger，区分动作条件失败检测、校准式求助与人工接管成本；见[核验批次 08](literature/EVIDENCE_BATCH_08_CALIBRATION_INTERVENTION.md)。
- 已核验 WorldSample、Hi-WM、WorldSync 与 FoMo-FD，区分真实在线 RL、模型内人工纠正、off-expert 动作跟随和离线失败监测；见[核验批次 09](literature/EVIDENCE_BATCH_09_INTERACTIVE_IMPROVEMENT.md)。
- 已核验 Dream2Fix、REBOOT、VLA-FixBench 与 AgentChord，区分世界模型合成恢复数据、人工恢复示范、诊断回滚和实体任务续接；见[核验批次 10](literature/EVIDENCE_BATCH_10_RECOVERY_RESUMPTION.md)。
- 已建立[检索、筛选与证据追踪协议](literature/SEARCH_PROTOCOL.md)，固定语料层次、去重顺序、纳入排除规则、45 篇原文核验记录及当前 adequate for bounded claims 保证边界。
- 已汇总[检索与发现日志](literature/SEARCH_LOG.md)，记录 R00--R15 的日期、渠道、覆盖问题、已保存查询、核验产出及未执行检索；未保存的结果数与早期查询显式标为 `NR`。
- 已完成 13 条正式版本解析：R14 升级 10 条预印本记录并补全 1 条 ICRA 记录，R15 将 Cosmos Policy 和 TesserAct 分别升级为 ICLR 2026 与 ICCV 2025 正式版本；其余条目仍按 V01 继续核对。
- 已清除正文中“下一轮检索”“collection priorities”和首页工作稿状态等协作阶段措辞，将其改写为受当前证据图谱边界约束的研究议程与综合判断；ACM 引用条按模板要求恢复显示。
- 已将同类综述定位从主题覆盖比较改为系统论断追踪：统一记录预测对象、动作接口、系统用途与证据环境，并避免以他文未列出的主题推断其缺失。
- 已重写摘要的综合结论，明确区分预测质量、仿真闭环、实体效用、部件归因与不同类型的安全证据，不引入当前语料无法支撑的性能结论。
- 已建立[主张溯源索引](literature/CLAIM_TRACE.md)，把摘要综合结论、边界对照规则和 Astra 接口判断连接到代表性原始来源与本地证据批次。
- 已建立[暂定 publication-family 语料](literature/PUBLICATION_FAMILIES.md)：929 条源记录中排除 15 条非论文占位项，将 914 条论文候选解析为 758 个暂定论文族；修正 4 条身份/链接元数据并记录 11 个人工合并判断。
- 已修正目录中 `2408.14197` 被误写为 Drive-WM、NavForesee 被误标为 CVPR 2026 正式论文，以及 OccWorld 作者名错误；目录统计仍为 929 条分类记录。
- 当前目录未检索到的 28 项补充文献及下一轮缺口见[边写边补清单](literature/WRITING_GAPS.md)。
- 已绘制 2 张论证型框架图：控制接口图与 claim-to-evidence trace，并提供英文图注和可访问性描述。
- 已从最新协作表导出七类文献目录；共 929 条分类记录，保留跨类重复。

## Astra 专题的证据边界

正文引用两篇近期预印本、一份项目报告和一份厂商报告，来源均直接链接或以 BibTeX 记录。Su 等人的早期项目报告与 Galbot 扩展稿有重合实验，不计作两个独立验证。不同任务子集和不同分母的成功率不拼成排名；混合策略收益也不直接归因于未被隔离检验的世界模型机制。

查询日期：2026-10-01。`2609.24170` 与 `2609.38537` 均按 v1 记录。动态报告使用查询当日页面。

## 下一批写作

| 内容 | 需要交付 |
|---|---|
| 数据与模型 | 已补 4D、触觉、点云多材料动力学和长时交互模拟器案例；继续补长时组合接触、跨传感器校准、人类视频和失败数据 |
| 策略融合 | 已补隐式规划、模型--策略共进化、导航/驾驶接口、长期记忆、预测式风险门控及受控失败后的实体纠正；继续补跨平台复现和统一实体消融 |
| 评估与安全 | 已补条件性保证、短视规避、可达性护盾、成本规划、校准式失败检测、求助率、人工恢复数据及任务续接；继续补真实分布偏移下的在线干预效果与跨平台复现 |
| 综述方法与定位 | 已固化基础语料、外部库 commit、R00--R13 检索日志、去重协议及 758 个暂定 publication family；继续执行统一数据库检索、正式版本解析、逐条排除理由、引文追踪和最终流程统计 |

## 尚待作者完成

作者与机构信息、CSUR 当期投稿要求、检索截止日期、文献正式发表版本与完整作者列表，以及按 ACM 当前政策填写的生成式 AI 使用说明。现有参考文献使用本轮实际检查过的版本，并未完成所有正式发表元数据的替换。

此仓库中的文字由 AI 辅助起草，需作者逐段核查、修订并承担最终责任；没有据此声称实验已复现或全文文献已核验。
