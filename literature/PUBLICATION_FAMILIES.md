# Provisional Publication-Family Corpus

Snapshot: 2026-10-02. This layer audits all 929 source rows, excludes 15 logged non-publication placeholders, and resolves 914 publication candidates into **758 provisional publication families**.

The count is reproducible but not final: exact normalized titles, verified arXiv identifiers, and logged manual decisions are merged; fuzzy similarity alone never merges records. Formal-version resolution and records without canonical identifiers still require review.

## Accounting

| Item | Count |
|---|---:|
| Frozen category records | 929 |
| Excluded non-publication placeholders | 15 |
| Publication candidate rows | 914 |
| Exact normalized candidate titles before family resolution | 812 |
| Provisional publication families | 758 |
| Families containing multiple source rows | 117 |
| Families touched by a manual merge decision | 11 |
| Identity or metadata corrections applied in this layer | 4 |

## Source Categories

| Category | Source rows |
|---|---:|
| Latent&预测表示 | 75 |
| 世界模型&VLA&规划 | 199 |
| 世界模型基础&控制 | 96 |
| 数据&模拟&跨本体 | 192 |
| 结构化物理&多模态 | 54 |
| 视觉&视频世界模型 | 61 |
| 评估&安全&Benchmark | 252 |

## Excluded Non-Publication Placeholders

- `S01-0020`: 【待补】Physical AI 中 world model 的权威定义
- `S01-0021`: 【待补】world model、simulator 与 digital twin 的正式比较
- `S01-0022`: 【待补】真实机器人世界模型的理论与系统综述
- `S05-0018`: 【待补】human video 与 robot data 的配比规律
- `S05-0019`: 【待补】跨 embodiment 世界模型
- `S05-0020`: 【待补】commanded action 与 realized action 数据记录
- `S05-0021`: 【待补】失败、干预与恢复数据集
- `S06-0037`: 【待补】world model 对 VLA 的独立增益消融
- `S06-0038`: 【待补】长期 memory、progress 与 recovery
- `S06-0039`: 【待补】人形和移动操作中的闭环证据
- `S06-0040`: 【待核对】A1 标题与出版元数据
- `S07-0021`: 【待补】专门面向 world model 的闭环 benchmark
- `S07-0022`: 【待补】action realization 与 interaction grounding 标准
- `S07-0023`: 【待补】world-model-specific runtime safety
- `S07-0024`: 【待补】simulator policy-ranking consistency

## Logged Corrections

- `S05-0107`: The original 2602.18025 link belongs to Cross-Embodiment Offline Reinforcement Learning; 2511.01177 matches this record's title and authors. Sources: [https://arxiv.org/abs/2511.01177](https://arxiv.org/abs/2511.01177), [https://arxiv.org/abs/2602.18025](https://arxiv.org/abs/2602.18025)
- `S05-0159`: The original 2505.07096 link belongs to X-Sim, not Cross-Sim-to-Real; no replacement primary source was verified. Sources: [https://arxiv.org/abs/2505.07096](https://arxiv.org/abs/2505.07096)
- `S06-0014`: Replace a tracking redirect with the canonical arXiv record for RoboCat. Sources: [https://arxiv.org/abs/2306.11706](https://arxiv.org/abs/2306.11706)
- `S06-0065`: The original 2603.07904 link belongs to DyQ-VLA. Crossref and the publisher identify the formal DynaVLA article under this title and DOI. Sources: [https://doi.org/10.1016/j.engappai.2026.115988](https://doi.org/10.1016/j.engappai.2026.115988), [https://arxiv.org/abs/2603.07904](https://arxiv.org/abs/2603.07904)

## Manual Merge Decisions

- `S05-0051`, `S05-0156`: Same CVPR 2026 paper; singular/plural title variation.
- `S02-0059`, `S03-0004`: Same I-JEPA paper; acronym omitted in one title.
- `S02-0019`, `S03-0007`: Same V-JEPA paper; acronym placement differs.
- `S05-0026`, `S05-0058`: Same OpenReview paper and identifier; acronym omitted in one title.
- `S01-0009`, `S02-0060`: Preprint and Nature version of MuZero.
- `S01-0013`, `S01-0060`: Same Diffuser paper; method name prefixed in one title.
- `S04-0005`, `S04-0021`: Same DOI; PDE abbreviation differs.
- `S06-0014`, `S07-0145`: Same RoboCat work; title wording differs between paper and project page.
- `S01-0051`, `S02-0021`: Preprint and CVPR 2024 version of Drive-WM.
- `S03-0009`, `S03-0046`: Preprint and ICML 2025 version of SOLD.
- `S05-0055`, `S05-0110`: Same ICLR 2026 paper identifier; one title contains a transcription error.

## Explicit Non-Merges

- `S01-0079`, `S07-0213`: Similar titles but distinct arXiv identifiers 1806.01242 and 1806.01261.
- `S06-0117`, `S06-0118`: Related tactile world-action models with distinct titles and arXiv identifiers.
- `S07-0095`, `S07-0125`: Related BEHAVIOR-1K releases with distinct preprint identifiers; retained separately pending formal version resolution.

## Assurance Boundary

This artifact supports record-level navigation and bounded manuscript claims. It does not establish comprehensive recall, independent dual screening, or a final PRISMA count. Singleton families without canonical identifiers remain candidates rather than verified unique publications.

Rebuild with `python literature/build_publication_families.py`; verify freshness with `python literature/build_publication_families.py --check`.
