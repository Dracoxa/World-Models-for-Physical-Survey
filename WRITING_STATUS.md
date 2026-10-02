# 写作状态 · 2026-10-02

## 本轮进展（v0.2）

- 已建立 ACM `acmart` / `CSUR` 项目和四部分正文文件。
- 四部分已有连贯第一轮内容，保留摘要、引言、概念边界与 Astra 专题。
- 扩写数据、模型、规划、想象学习、联合动作生成、评估和安全；仍需更多技术细节与领域实例。
- 新增 7 张 LaTeX 比较表，连同 Astra 表共 8 表；正文参考文献从 8 条增至 64 条。
- 新增[同类开源调研与差异化定位](RELATED_SURVEYS.md)，并将 2026 年已发表、与 Physical AI 控制视角高度重合的综述纳入正文定位比较。
- 已将 NTUMARS、Li-Zn-H、OpenMOSS 三个高相关开源库与 929 条目录按 arXiv ID 和题名去重，新增候选及优先级见[外部调研库去重结果](literature/EXTERNAL_CANDIDATES.md)。
- 已对最高优先级中的 OmniVTA、Interactive World Simulator、World-VLA-Loop、TesserAct 和 WAV 完成原文级快速核验，并将证据、可支撑判断和局限写入[核验批次 01](literature/EVIDENCE_BATCH_01.md)。
- 已核验 5 篇安全原始来源，将形式保证、仿真中的经验降风险和无实证的架构提案分开记录，详见[核验批次 02](literature/EVIDENCE_BATCH_02_SAFETY.md)。
- 已补 3 篇含实体试验的运行时安全工作和 1 篇 2026 perspective，记录干预接口、实体分母与保证边界，详见[核验批次 03](literature/EVIDENCE_BATCH_03_RUNTIME_SAFETY.md)。
- 已核验 ContactWorld、TouchWorld、DexTouch-WM、ParticleFormer 与 MVISTA-4D，区分触觉感知、未来预测、快速反馈、动作条件前向模型和未来到动作反演，详见[核验批次 04](literature/EVIDENCE_BATCH_04_CONTACT_STRUCTURED.md)。
- 已核验 Drive-WM、OccWorld、Drive-OccWorld、DriveVLA-W0 与 NavForesee，区分推理时候选 rollout、联合场景--轨迹预测和训练时预测监督，详见[核验批次 05](literature/EVIDENCE_BATCH_05_NAVIGATION_DRIVING.md)。
- 已核验 NWM、DreamerNav、NavThinker 与 NavWAM，区分离线显式规划、latent policy、候选动作 look-ahead 与联合世界--动作闭环；实体证据分母与局限见[核验批次 06](literature/EVIDENCE_BATCH_06_NAVIGATION_CLOSED_LOOP.md)。
- 已核验 Mem-World、WorldScape Policy 2.0、FARL、ViFailback 与 LIBERO-Recover，区分记忆保持、进度跟踪、提前避险、失败后纠正和状态恢复；见[核验批次 07](literature/EVIDENCE_BATCH_07_MEMORY_RECOVERY.md)。
- 已修正目录中 `2408.14197` 被误写为 Drive-WM、NavForesee 被误标为 CVPR 2026 正式论文，以及 OccWorld 作者名错误；目录统计仍为 929 条分类记录。
- 当前目录未检索到的 17 项补充文献及下一轮缺口见[边写边补清单](literature/WRITING_GAPS.md)。
- 已绘制图 1，并提供英文图注和可访问性描述。
- 已从最新协作表导出七类文献目录；共 929 条分类记录，保留跨类重复。

## Astra 专题的证据边界

正文引用两篇近期预印本、一份项目报告和一份厂商报告，来源均直接链接或以 BibTeX 记录。Su 等人的早期项目报告与 Galbot 扩展稿有重合实验，不计作两个独立验证。不同任务子集和不同分母的成功率不拼成排名；混合策略收益也不直接归因于未被隔离检验的世界模型机制。

查询日期：2026-10-01。`2609.24170` 与 `2609.38537` 均按 v1 记录。动态报告使用查询当日页面。

## 下一批写作

| 内容 | 需要交付 |
|---|---|
| 数据与模型 | 已补 4D、触觉、点云多材料动力学和长时交互模拟器案例；继续补长时组合接触、跨传感器校准、人类视频和失败数据 |
| 策略融合 | 已补隐式规划、模型--策略共进化、导航/驾驶接口、长期记忆及预测式风险门控；继续补跨平台复现、失败后状态恢复和统一实体消融 |
| 评估与安全 | 已补条件性保证、短视规避、可达性护盾、成本规划、实体纠正及恢复层级；继续补分布外校准、跨平台复现与干预成本 |
| 综述方法与定位 | 真实检索日志、筛选理由、已有综述差异和最终统计 |

## 尚待作者完成

作者与机构信息、CSUR 当期投稿要求、检索截止日期、文献正式发表版本与完整作者列表，以及按 ACM 当前政策填写的生成式 AI 使用说明。现有参考文献使用本轮实际检查过的版本，并未完成所有正式发表元数据的替换。

此仓库中的文字由 AI 辅助起草，需作者逐段核查、修订并承担最终责任；没有据此声称实验已复现或全文文献已核验。
