# World Models for Physical AI · Literature Catalog

按七类研究主题整理的候选文献检索目录。快照日期：2026-10-01。

当前收录 **929 条分类记录**。跨主题记录保留，因此该数字不是全局唯一论文数，也不是已核验论文数。这里同步标题、作者、年份、来源和链接；实验结论继续在内部协作表中核查。

| 主题 | 分类记录数 |
|---|---:|
| [世界模型基础&控制](categories/01-foundations-control.md) | 96 |
| [视觉&视频世界模型](categories/02-visual-video.md) | 61 |
| [Latent&预测表示](categories/03-latent-representations.md) | 75 |
| [结构化物理&多模态](categories/04-physics-multimodal.md) | 54 |
| [数据&模拟&跨本体](categories/05-data-simulation-embodiment.md) | 192 |
| [世界模型&VLA&规划](categories/06-policy-planning.md) | 199 |
| [评估&安全&Benchmark](categories/07-evaluation-safety.md) | 252 |

## 检索和维护

- 在分类页按标题或作者查找；下载 [catalog.csv](catalog.csv) 可按年份、类别、来源筛选。
- `publication_status` 为原表填写，不代表本目录确认接受或发表状态。
- 原始论文核验后确认的 7 条元数据修正由 `export_catalog.py` 中的 `VERIFIED_OVERRIDES` 保留，重新导出不会退回旧值。
- 32 条记录暂未导出可用的公开链接；校园代理、临时签名下载链接和不完整链接不进入公开目录。链接能打开也不等于标题与原文已经核验。
- 记录编号用于定位当前快照，不作为论文永久标识。后续核验优先记录 DOI、arXiv ID 和正式出版版本。
- 更新分类与元数据后重新导出：`python export_catalog.py path/to/workbook.xlsx`。依赖：`openpyxl`。

## 本轮新增讨论入口

2026-10-01 v0.2 写作补充另见[文献与内容缺口清单](WRITING_GAPS.md)；补充来源单列，不计入 929 条原快照。

2026-10-02 已完成第一批 5 篇新增候选的原文核验，详见[接触、4D、模拟器与策略闭环证据表](EVIDENCE_BATCH_01.md)。这些条目仍与 929 条原快照分开统计。

2026-10-02 已完成第二批 5 篇安全原始来源核验，详见[安全保证、经验降风险与运行时护栏证据表](EVIDENCE_BATCH_02_SAFETY.md)。其中 4 篇已在原目录中，SafeDreamer 仍作为正文补充来源单列。

2026-10-02 已完成第三批运行时安全核验，详见[实体运行时监测、语义护栏与可验证安全模块证据表](EVIDENCE_BATCH_03_RUNTIME_SAFETY.md)。Model-Based Runtime Monitoring 已在原目录中并修正正式发表元数据，其余 3 篇作为正文补充来源单列。

2026-10-02 已完成第四批接触与结构化三维核验，详见[接触、触觉与结构化三维世界模型证据表](EVIDENCE_BATCH_04_CONTACT_STRUCTURED.md)。ContactWorld 已在原目录中并更新到 v3；TouchWorld、DexTouch-WM、ParticleFormer 与 MVISTA-4D 作为正文补充来源单列。

2026-10-02 已完成第五批导航与驾驶核验，详见[导航与自动驾驶中的预测--决策接口证据表](EVIDENCE_BATCH_05_NAVIGATION_DRIVING.md)。5 篇均在原目录中；本轮修正了 NavForesee 的预印本状态、OccWorld 作者与正式版本，以及被错配到 `2408.14197` 的 Drive-OccWorld 记录。

2026-10-02 已完成第六批闭环导航核验，详见[导航世界模型的闭环、实体部署与重规划证据表](EVIDENCE_BATCH_06_NAVIGATION_CLOSED_LOOP.md)。DreamerNav 与 NavThinker 已在原目录；NWM 与 NavWAM 作为正文补充来源单列。现有实体证据仍以受控演示和单平台小样本为主。

2026-10-02 已完成第七批记忆与恢复核验，详见[长期记忆、失败检测与恢复证据表](EVIDENCE_BATCH_07_MEMORY_RECOVERY.md)。Mem-World、WorldScape Policy 2.0、ViFailback 与 LIBERO-Recover 已在原目录；Failure-Aware RL 作为正文补充来源单列。恢复证据按失败前预防、失败检测、动作纠正、状态修复和任务恢复区分。

2026-10-02 已完成第八批风险校准与干预代价核验，详见[分布偏移校准、选择性求助与干预代价证据表](EVIDENCE_BATCH_08_CALIBRATION_INTERVENTION.md)。Foresight、KnowNo、CoFineLLM 与 ThriftyDAgger 均作为补充来源单列；只有 Foresight 是直接世界模型证据，其余用于界定求助和人工接管的评估接口。

以下为 2026-10-01 核对的 Astra 相关来源，另列于现有表格快照之外，未计入上述数量：

- GPT 6 Astra as an Embodied Policy [技术报告与代码](https://github.com/anonymous-report-421/GPT-as-Policy)
- An Unexpected Robot Policy [https://arxiv.org/abs/2609.24170](https://arxiv.org/abs/2609.24170)
- Systematically Exploring the Capabilities of GPT-6 Astra as Embodied Policies [https://arxiv.org/abs/2609.38537](https://arxiv.org/abs/2609.38537)
- FLUX 3 Action [技术报告](https://bfl.ai/models/flux-3-action)

前述项目报告与 Galbot 扩展稿中的重合实验应按证据系列处理，不能计作独立重复验证。

## 快照来源

工作簿名：`world_model_survey_七页统一去重版.xlsx`。

SHA-256：`bcc92b5e56260e2938e6ecf769e7fb0bad2928628800cde26873940e7c17c384`。

本目录提供文献索引，不分发论文 PDF、实验截图或模型权重。
