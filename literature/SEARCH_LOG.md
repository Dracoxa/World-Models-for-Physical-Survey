# Search and Discovery Log

Version: 2026-10-02. This log consolidates the searches and corpus operations that can be reconstructed from contemporaneous project records. Run IDs were assigned during this consolidation and were not preregistered. `NR` means not recorded at search time; missing counts or query strings are not reconstructed after the fact.

The review profile remains a **structured narrative review with a critical evidence map**. This log supports bounded, source-specific claims and does not establish database-complete recall or PRISMA completion.

## Coverage Questions

| ID | Coverage question |
|---|---|
| CQ1 | What quantity is predicted: observations, latent states, geometry, physical variables, rewards, constraints, or task outcomes? |
| CQ2 | How do actions or interventions enter the model? |
| CQ3 | Where is prediction used: representation learning, planning, control, simulation, monitoring, or recovery? |
| CQ4 | What evaluation environment and denominator support the claim? |
| CQ5 | What uncertainty, safety, intervention, or recovery boundary is tested? |
| CQ6 | What data, embodiment, sensor, or domain transfer is demonstrated? |

## Run Summary

| Run | Date | Channel | Coverage | Retrieved / candidates | Deep-checked yield | Record |
|---|---|---|---|---:|---:|---|
| R00 | 2026-10-01 | User-provided seven-sheet catalog | CQ1--CQ6 | 929 category rows | Not a screening run | [Catalog](catalog.csv) |
| R01 | 2026-10-01 | Web, arXiv, PMLR, NeurIPS/ICLR pages, project pages | CQ1--CQ6 | NR | NR; anchors entered the manuscript and gap tracker | [Gap tracker](WRITING_GAPS.md) |
| R02 | 2026-10-02 | Three frozen GitHub bibliographies | CQ1--CQ6 | 341 unique arXiv IDs; 253 absent from the local catalog | 5 prioritized for R03 | [External candidates](EXTERNAL_CANDIDATES.md) |
| R03 | 2026-10-02 | Priority candidates from R02, then arXiv full text | CQ1--CQ4, CQ6 | Search-result count NR | 5 | [Batch 01](EVIDENCE_BATCH_01.md) |
| R04 | 2026-10-02 | Targeted safety search; NeurIPS, ICLR, arXiv | CQ3--CQ5 | Search-result count NR | 5 | [Batch 02](EVIDENCE_BATCH_02_SAFETY.md) |
| R05 | 2026-10-02 | Targeted runtime-safety search; arXiv | CQ3--CQ5 | Search-result count NR | 4 | [Batch 03](EVIDENCE_BATCH_03_RUNTIME_SAFETY.md) |
| R06 | 2026-10-02 | Targeted contact/structured-physics search; arXiv, PMLR | CQ1--CQ4, CQ6 | Search-result count NR | 5 | [Batch 04](EVIDENCE_BATCH_04_CONTACT_STRUCTURED.md) |
| R07 | 2026-10-02 | Catalog seeds and targeted navigation/driving search; publisher and arXiv pages | CQ1--CQ5 | Search-result count NR | 5 | [Batch 05](EVIDENCE_BATCH_05_NAVIGATION_DRIVING.md) |
| R08 | 2026-10-02 | Targeted closed-loop navigation search; CVF, Frontiers, arXiv | CQ1--CQ4 | Search-result count NR | 4 | [Batch 06](EVIDENCE_BATCH_06_NAVIGATION_CLOSED_LOOP.md) |
| R09 | 2026-10-02 | Targeted memory and recovery search; arXiv, CVF | CQ3--CQ5 | Search-result count NR | 5 | [Batch 07](EVIDENCE_BATCH_07_MEMORY_RECOVERY.md) |
| R10 | 2026-10-02 | Targeted calibration/intervention search; arXiv, PMLR | CQ4--CQ5 | Search-result count NR | 4 | [Batch 08](EVIDENCE_BATCH_08_CALIBRATION_INTERVENTION.md) |
| R11 | 2026-10-02 | Targeted interactive-improvement search; project pages, arXiv | CQ2--CQ6 | Search-result count NR | 4 | [Batch 09](EVIDENCE_BATCH_09_INTERACTIVE_IMPROVEMENT.md) |
| R12 | 2026-10-02 | Targeted recovery/resumption search; arXiv, PMLR | CQ2--CQ5 | Search-result count NR | 4 | [Batch 10](EVIDENCE_BATCH_10_RECOVERY_RESUMPTION.md) |
| R13 | 2026-10-02 | Identity normalization and publication-family resolution | Corpus integrity | 929 source rows | 15 placeholders excluded; 914 candidates resolved to 758 provisional families | [Family audit](PUBLICATION_FAMILIES.md) |
| R14 | 2026-10-02 | Formal-version resolution; PMLR, ICLR Proceedings, RSS, IEEE/DOI records | Publication status | 11 cited records checked | 10 preprint citations upgraded; 1 conference record completed with its DOI | [Bibliography](../paper/references.bib) |

The ten paper-level evidence batches contain 45 records in total. They are focused samples selected to answer manuscript questions, not a random or exhaustive sample of the 758 provisional families.

## Recorded Queries and Seeds

### R01: Initial Scope, Survey Positioning, and Missing Anchors

The following exact queries were retained:

1. `world models physical AI survey 2026 arxiv robot world action survey`
2. `world models survey 2026 embodied intelligence taxonomy evaluation survey latex`
3. `DreamZero World Action Models are Zero shot Policies 2026 arxiv`
4. `Cosmos Policy fine tuning video models visuomotor control 2026 arxiv`
5. `WorldArena 2026 benchmark embodied world models arxiv`
6. `SafeDreamer world models safety constraints ICLR 2024 paper`
7. `site.proceedings.mlr.press Recovery RL Safe Reinforcement Learning Learned Recovery Zones`
8. `site.arxiv.org control barrier functions theory applications Ames 2019`

The search-result count and title/abstract exclusion count were not recorded. Sources used in prose were subsequently checked against primary paper or proceedings pages; the resulting supplemental-source list is maintained in [WRITING_GAPS.md](WRITING_GAPS.md).

### R02: Frozen External Bibliographies

Discovery sources were frozen by repository commit:

- NTUMARS/Awesome-World-Model-for-Robotics-Policy @ `5f69b4e`
- Li-Zn-H/AwesomeWorldModels @ `9de513c`
- OpenMOSS/Awesome-WAM @ `aa6cd05`

Entries were compared by arXiv ID, normalized title, and manually reviewed near-title candidates. Repository inclusion was used only for discovery priority, never as evidence of quality or correctness.

### R03--R07: Early Focused Batches

The exact query strings and search-result counts were not preserved for these five runs. The following contemporaneous information remains auditable:

- R03 started from the highest-priority R02 candidates and verified OmniVTA, Interactive World Simulator, World-VLA-Loop, TesserAct, and World-Value-Action Model.
- R04 used the R01 safety anchors plus targeted searches to separate formal guarantees, empirical constraint reduction, recovery mechanisms, and architecture proposals.
- R05 selected runtime safety papers with physical trials or explicit module-level guarantees.
- R06 selected contact, tactile, structured 3D, and 4D prediction papers with identifiable action interfaces.
- R07 started from cataloged navigation and driving papers and checked formal publisher or current arXiv records.

Because the original query text is missing, these runs cannot support reproducible recall claims. Their batch files support only paper-level evidence traceability.

### R08: Closed-Loop Navigation

Seeds: DreamerNav, NavThinker, and NavForesee. Recorded queries:

1. `Navigation World Models`
2. `navigation world model real robot closed loop`
3. `world action model navigation real robot`

### R09: Memory, Failure Detection, and Recovery

Seeds: Mem-World, WorldScape Policy 2.0, ViFailback, and LIBERO-Recover. Recorded queries:

1. `world model failure recovery real robot`
2. `long-term memory world action model`
3. `robot failure recovery benchmark`

### R10: Calibration and Intervention Cost

1. `world model uncertainty calibration robot safety 2026`
2. `robot failure detector conformal real world`
3. `robot ask for help conformal planning`
4. `robot intervention cost physical evaluation`

### R11: Interactive Improvement

1. `world model online intervention failure detection real robot`
2. `action-conditioned world model safety monitor online intervention physical robot`
3. `robot world model failure alarm intervention real-world manipulation recovery`
4. `robot failure prediction intervention real robot world model`

### R12: Recovery and Task Resumption

1. `real robot failure recovery state restoration resume task manipulation 2026`
2. `robot manipulation recover from execution failure real-world benchmark state restoration`
3. `world model failure correction closed-loop real robot`
4. `VLA rollback correction real-world failure benchmark`

### R14: Formal Publication Versions

Eleven cited records with unambiguous official publication entries were resolved: PlaNet (ICML 2019), Dreamer (ICLR 2020), Recovery RL (RA-L 2021), CALVIN (RA-L 2022), UniSim and TD-MPC2 (ICLR 2024), DROID (RSS 2024), Open X-Embodiment and Model-Based Runtime Monitoring (ICRA 2024), OpenVLA (CoRL proceedings published in PMLR 2025), and Control Barrier Functions (ECC 2019). Ten preprint entries were upgraded; the existing ICRA runtime-monitoring entry received its formal DOI and publisher. Citation keys were retained so that manuscript anchors did not change. This run did not infer missing DOIs and does not close version checking for the remaining bibliography.

## Screening and Evidence Handling

- Candidate discovery and evidence inclusion are separate decisions. Repository lists, project pages, and surveys locate papers but do not validate experimental claims.
- Direct world-model evidence is separated from supporting resources and boundary comparators.
- Formal publications are preferred when available; preprints retain explicit version and status.
- Numbers are extracted with task, environment, denominator, comparator, and source location. Incompatible protocols are not combined into rankings.
- Each batch records what the evidence can support and what it cannot establish.

## Unfinished Retrieval Work

The following required runs have not been executed and therefore have no fabricated counts:

| Planned run | Missing evidence | Consequence |
|---|---|---|
| D01 | Unified searches across selected scholarly databases with exact dates, fields, and filters | No database-complete recall claim |
| D02 | Venue census for major robotics, ML, vision, and control venues | Possible venue-specific omissions |
| C01 | Backward citation decisions for foundational and closest survey seeds | Historical lineage may remain incomplete |
| C02 | Forward citation decisions for foundational and recent anchor papers | Recent follow-on work may remain incomplete |
| V01 | Formal publication-version resolution for remaining preprints; 11 cited records resolved in R14 | Partially complete; some canonical citations may still change |
| S01 | Title/abstract and full-text exclusion log with reasons | No final PRISMA flow count |
| P01 | Independent PRESS-style review of the search strategy | Search design has only internal review |

## Assurance Statement

Current discovery assurance is **adequate for bounded claims**. The log makes completed rapid-scan work traceable where records exist and reproducible only where exact query provenance was retained; it also exposes where provenance is missing. It is insufficient for claims that the corpus is exhaustive, that 758 is a final unique-paper count, or that omitted work is absent from the field.
