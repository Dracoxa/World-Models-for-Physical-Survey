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
| R15 | 2026-10-02 | Formal-version resolution; ICLR and CVF proceedings, arXiv | Publication status | 4 cited records checked | 2 preprints upgraded; 2 retained as preprints after no official proceedings page was found in this check | [Bibliography](../paper/references.bib) |
| R16 | 2026-10-02 | Formal-version resolution; IEEE/DOI record, arXiv, project pages | Publication status | 4 cited records checked | 1 preprint upgraded; 3 retained as preprints after no formal venue page was found in this check | [Bibliography](../paper/references.bib) |
| R17 | 2026-10-02 | Targeted ICML 2026 PMLR volume scan and primary full text | CQ1--CQ4, CQ6 | 3 absent candidates retained | 2 full-text evidence records; 1 full-text boundary comparator resolved | [Batch 09](EVIDENCE_BATCH_09_INTERACTIVE_IMPROVEMENT.md), [gap tracker](WRITING_GAPS.md) |
| R18 | 2026-10-02 | GitHub update scan; repository pages and web search | CQ1--CQ6 | 5 candidate repositories inspected | 4 retained as discovery neighbors; none added to the frozen candidate count | [Related surveys](../RELATED_SURVEYS.md) |
| R19 | 2026-10-02 | Targeted CVPR 2026 scan; official CVF pages and primary full text | CQ1--CQ4, CQ6 | 11 unique title candidates; 7 absent from catalog | 8 full-text evidence records | [Batch 11](EVIDENCE_BATCH_11_CVPR2026_POLICY_INTEGRATION.md), [Batch 12](EVIDENCE_BATCH_12_CVPR2026_PHYSICAL_REPRESENTATIONS.md) |
| R20 | 2026-10-02 | GitHub survey delta scan; repository and survey pages | CQ1--CQ6 | 7 candidate repositories inspected | 3 retained as discovery sources; no paper-level evidence added | [Related surveys](../RELATED_SURVEYS.md) |
| R21 | 2026-10-02 | Frozen bibliography comparison for R20 sources | CQ1--CQ6 | 633 unique arXiv IDs; 359 absent from catalog and tracked supplements | 14 multi-source candidates prioritized; no paper-level evidence added | [Delta candidates](EXTERNAL_CANDIDATES_DELTA_2026-10-02.md) |
| R22 | 2026-10-02 | Primary arXiv identity and abstract screening | CQ1--CQ6 | 14 multi-source candidates screened | 6 prioritized for full-text review; 5 deferred; 3 retained only as support/boundaries | [Screening table](EXTERNAL_CANDIDATE_SCREENING_2026-10-02.md) |
| R23 | 2026-10-02 | Primary full text for top geometry/tactile candidates | CQ1--CQ4, CQ6 | 2 papers | 2 full-text evidence records and 2 manuscript additions | [Batch 13](EVIDENCE_BATCH_13_GEOMETRY_TACTILE_WAM.md) |
| R24 | 2026-10-02 | Primary full text for remaining R22 priority candidates | CQ1--CQ4, CQ6 | 4 papers | 4 full-text evidence records and 4 manuscript additions | [Batch 14](EVIDENCE_BATCH_14_PREDICTIVE_INTERFACES.md) |
| R25 | 2026-10-02 | GitHub driving-world-model survey scan | CQ1--CQ6 | 4 search queries; 3 repositories retained | Discovery sources only; frozen candidate count unchanged | [Related surveys](../RELATED_SURVEYS.md) |
| R26 | 2026-10-02 | Primary full text for R22 second-queue candidates | CQ1--CQ4, CQ6 | 5 papers | 5 full-text evidence records and 5 manuscript additions | [Batch 15](EVIDENCE_BATCH_15_GENERATION_SCHEDULES_EVENTS.md) |
| R27 | 2026-10-02 | Gap-driven screening of R21 evaluation/reliability candidates; primary full text and CVF record | CQ3--CQ5 | 23 title matches screened; 6 retained | 6 full-text evidence records and 6 manuscript additions | [Batch 16](EVIDENCE_BATCH_16_DIAGNOSTIC_EVALUATION.md) |
| R28 | 2026-10-02 | Gap-driven screening of R21 physical intervention/correction candidates; primary arXiv full text | CQ2--CQ5 | 4 candidates checked; 3 retained | 3 full-text evidence records and 3 manuscript additions; 1 simulation-only boundary | [Batch 17](EVIDENCE_BATCH_17_PHYSICAL_INTERVENTION_CORRECTION.md) |
| R29 | 2026-10-02 | Gap-driven screening of R21 generalization candidates; primary arXiv full text | CQ1--CQ4, CQ6 | 4 candidates checked and retained | 4 full-text evidence records and 4 manuscript additions | [Batch 18](EVIDENCE_BATCH_18_GENERALIZATION_CONTRACTS.md) |
| R30 | 2026-10-02 | Formal-version resolution; arXiv, ECCV accepted-paper list, institutional publication record | Publication status | 4 cited records checked | 2 acceptance statuses resolved; 2 records retained as preprints; no entry upgraded to proceedings | [Formal-version audit](FORMAL_VERSION_AUDIT_2026-10-02.md) |
| R31 | 2026-10-02 | Latest-paper follow-up from V-JEPA formal-version check; arXiv primary full text | CQ1--CQ4, CQ6 | 1 post-freeze candidate found, deduplicated, and retained | 1 full-text evidence record and 1 manuscript addition | [Batch 19](EVIDENCE_BATCH_19_VJEPA_POLICY.md) |
| R32 | 2026-10-02 | Closest-work check around V-JEPA Policy; frozen catalog, external candidates, and arXiv primary full text | CQ1--CQ4, CQ6 | 2 direct JEPA-policy neighbors deduplicated and retained | 2 full-text evidence records and 2 manuscript additions | [Batch 20](EVIDENCE_BATCH_20_JEPA_POLICY_NEIGHBORS.md) |
| R33 | 2026-10-02 | High-priority external-candidate follow-up; frozen catalog and arXiv primary full text | CQ1--CQ4, CQ6 | 1 predictive-representation candidate deduplicated and retained | 1 full-text evidence record and 1 manuscript addition | [Batch 21](EVIDENCE_BATCH_21_JEPA_VLA_REPRESENTATION.md) |

The twenty-one paper-level evidence batches contain 83 records in total. They are focused samples selected to answer manuscript questions, not a random or exhaustive sample of the 758 provisional families.

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

### R15: Formal Publication Versions II

Four cited records were checked against official proceedings pages and arXiv. Cosmos Policy was upgraded to its ICLR 2026 proceedings entry, and TesserAct was upgraded to its ICCV 2025 entry under the formal title *Learning 4D Embodied World Models*. V-JEPA 2 and *World Action Models are Zero-shot Policies* were retained as preprints because this check did not find official proceedings pages for them. Citation keys were retained, no DOI was inferred, and publication status was not used to strengthen experimental claims.

### R16: Formal Publication Versions III

Four cited records were checked against an official IEEE/DOI record, arXiv, and author project pages. *Safe Model-Based Reinforcement Learning With an Uncertainty-Aware Reachability Certificate* was upgraded from its 2022 preprint to the IEEE T-ASE 2024 volume version; the formal author list adds Yuming Yin and changes the author order. WorldSample, Dream2Fix, and Hi-WM were retained as preprints because this check did not find formal venue pages for them. The publication upgrade does not alter the paper's simulation-only evidence boundary.

### R17: Targeted ICML 2026 Scan

The newly published PMLR volume 306 was searched for world-model and VLA terms, then candidate titles were checked against the 929-record catalog. VLAW, *Learning Task-Sufficient World Models by Synergizing Agentic Exploration and Structured Modeling*, and *Latent Reasoning VLA* were absent. VLAW and the task-sufficient paper were checked at full-text level, added to Batch 09, and used in the manuscript with their respective physical and simulation evidence boundaries. Full-text inspection resolved *Latent Reasoning VLA* as a boundary comparator: it predicts a future visual latent from observations, instructions, and reasoning states, then decodes actions, but does not expose a candidate-action-conditioned forward model. This targeted pass is not a complete ICML 2026 venue census and does not complete D02.

### R18: GitHub Survey Update Scan

GitHub repository and web searches inspected five previously unlisted collections: JiahuaDong/Awesome-World-Models, NeuraLiying/Awesome-World-Models, autonomousdrivingkr/Awesome-Physical-AI, w-xb/awesome-agentic-robotics, and operator22th/awesome-world-models-for-robots. The first four were retained as discovery neighbors because they respectively add a 2026 survey update stream, a broad categorized bibliography, a Physical AI systems view, and an agentic safety/recovery neighborhood. The operator22th list was not retained for ongoing tracking because its metadata and update structure are comparatively sparse. No paper-level evidence or candidate count was changed: these repositories must first be deduplicated against the frozen corpus, and their entries remain discovery leads rather than evidence.

### R19: Targeted CVPR 2026 Policy-Integration Scan

Four recorded queries targeted official CVF pages: `site:openaccess.thecvf.com/content/CVPR2026/html "world model" robot`, `"world models" embodied`, `"action-conditioned" robot`, and `predictive planning robot`. Eleven unique title candidates were retained from the returned official pages. Motus, Chain of World, 4DWorldBench, and RoboWM-Bench were already in the 929-record catalog. Dexterous World Models, DynBridge, ModularAgent, Physical Object Understanding with a Physically Controllable World Model, GeoWorld, MM-ACT, and PhysInOne were absent by full title. All seven absent candidates and the cataloged Motus paper were inspected at full-text level. Batch 11 records Motus, DynBridge, and MM-ACT as policy-integration cases; Batch 12 records DWM, PhyWM, PhysInOne, GeoWorld, and ModularAgent as distinct visual-consequence, structure-discovery, synthetic-data, procedural-planning, and simulation-control cases. The official Motus page also exposed a hard metadata error in `S05-0063`: its authors and venue belonged to a different work despite the correct title and link. The public catalog now applies a verified export override with the CVPR 2026 author list and publication status. The run remains a targeted query pass rather than a complete CVPR 2026 title census, so it advances but does not complete D02.

### R20: GitHub Survey Delta Scan II

Four exact web queries were used: `site:github.com world models physical AI survey robotics 2026 awesome`, `site:github.com world model robotics survey VLA world action model awesome 2026`, `site:github.com embodied world models survey benchmark robotics`, and `site:github.com physical AI survey world model robot literature`. Seven previously unlisted candidate repositories were inspected. Three were retained: RCL-Robotics/Awesome-World-Action-Models provides the machine-readable companion catalog and classification audit for Lu et al.; world-action-models/awesome-world-action-models gives a narrow action-path inclusion rule and three WAM families; NJU3DV-LoongGroup/Embodied-World-Models-Survey links physical simulator properties with world-model resources. Four personal or derivative WAM/VLA lists were not retained because their coverage substantially overlaps these sources without adding a distinct audit or taxonomy interface. No repository entry was treated as paper-level evidence, and no frozen candidate count changed.

### R21: Frozen Comparison of R20 Sources

The three retained sources were frozen at RCL-Robotics/Awesome-World-Action-Models `7985fa2`, world-action-models/awesome-world-action-models `9be4441`, and NJU3DV-LoongGroup/Embodied-World-Models-Survey `185871d`. Their Markdown bibliographies yielded 633 unique arXiv IDs. Matching by arXiv ID, normalized title, and near-title against the 929-row catalog, the previous external-candidate CSV, the writing-gap tracker, and the manuscript bibliography left 359 raw discovery candidates; one unresolved title per source was excluded from that count. Fourteen candidates occurred in at least two sources and form the first screening queue. These are source-specific discovery counts, not a claim that 359 papers satisfy the review's inclusion criteria or have verified metadata, methods, or results.

### R22: Multi-Source Candidate Screening

The current arXiv identity, version, and abstract were checked for all 14 candidates occurring in at least two R21 sources. Six direct world-model papers were assigned to the first full-text queue: DriveDreamer-Policy, VTAM, JOPAT, VAMPO, Audio-WM, and DexWM. Five direct but less urgent driving, inference-scheduling, or system-design papers were deferred to a second queue. Cosmos-Transfer1, FAST, and DexGraspNet were retained only as data, component, or boundary sources. Abstract screening establishes neither experimental validity nor publication status beyond the arXiv record.

### R23: Geometry and Tactile World--Action Full-Text Check

DriveDreamer-Policy and VTAM were checked in full text. DriveDreamer-Policy contributes matched NAVSIM ablations for joint depth/video/action supervision, but its evaluation is predictive-driver-model based and its depth target is DA3 pseudo-depth. VTAM contributes 80 physical trials per model across contact-rich tasks, plus a ten-trial chip-task ablation, but reports only qualitative future-prediction assessment. Both entered the manuscript with these limits preserved; neither supports a general causal claim that lower prediction error produces physical closed-loop gains.

### R24: Predictive-Interface Full-Text Check

The remaining four R22 priority papers were checked in full text. JOPAT contributes matched pixel/track/action ablations and ten physical rollouts per task; VAMPO separates predictor-only post-training from subsequent action-module adaptation on CALVIN but omits physical evaluation denominators; Audio-WM contributes a 30-trial closed-loop audio-anticipation case without a matched physical no-lookahead ablation; DexWM contributes simulation and 12-trial physical transfer evidence while relying on four hours of simulated robot adaptation. Batch 14 records these distinctions. All four entered the manuscript as interface-specific examples, not as evidence for a cross-paper performance ranking or a general causal relationship between prediction accuracy and physical control.

### R25: GitHub Driving-World-Model Survey Scan

Four exact web queries were used: `site:github.com world action models survey awesome 2026 robotics`, `site:github.com embodied world models survey 2026`, `site:github.com "World Models for Physical AI" survey`, and `site:github.com autonomous driving world model survey awesome`. AwesomeWMAD, NYU-ECE-AV-Group/World-Models-Autonomous-Driving-Latest-Survey, and Foundation-Models-Meet-Driving-World-Models were retained because they add, respectively, a prediction--planning interaction taxonomy, a venue-organized update stream, and a foundation-model-role view of driving world models. A repository with a placeholder arXiv identifier was not retained. The three sources remain discovery aids; no paper-level claim, frozen candidate count, or evidence grade changed.

### R26: Generation-Schedule and Event-Interface Full-Text Check

The five R22 second-queue papers were checked in full text. DriveWAM exposes generated-future-conditioned action decoding and bounded history but evaluates only logged driving; NoiseGate optimizes per-latent denoising schedules with simulator reward and reports one seed; DAWN provides matched reciprocal world--action and rollout-horizon ablations without real-vehicle evidence; WALL-WM provides internal real-robot Task Progress but combines event execution with cross-view changes and omits physical trial denominators; ADriver-I provides an early modular interleaved loop whose recurrent-driving evidence is qualitative and model-internal. Batch 15 records these boundaries. All five entered the manuscript as interface examples, not as evidence of deployment safety or a common performance scale.

### R27: Diagnostic Evaluation and Prediction-Integrity Full-Text Check

The 359-candidate R21 delta was filtered by title for benchmark, evaluation, reliability, safety, risk, uncertainty, failure, robustness, degradation, attack, guard, monitor, and causal terms. Twenty-three records matched; this is a gap-driven title screen, not a complete title/abstract review of the remaining delta. Six papers were retained because they add distinct evaluation endpoints already required by the manuscript: WorldLens for driving generation-to-control evaluation, ManipArena for controlled physical policy comparison, stage-wise sensing degradation for pipeline diagnosis, GeoBoN for prediction-based candidate selection and compute gating, the trusted-imagination attack for downstream prediction integrity, and the WAM--VLA robustness study for perturbation profiles. Primary arXiv or CVF full text was checked for all six. Two arXiv records have title differences between their abstract metadata and HTML/PDF; the evidence batch records those version-level inconsistencies instead of silently choosing a title. None of the simulation-only results is interpreted as physical safety, and the mixed-training robustness table is not used for a causal model-family ranking.

### R28: Physical Intervention and Execution-Time Correction Check

The R21 delta was queried for intervention, correction, avoidance, failure, and real-time tactile terms. Four direct candidates were checked in primary arXiv full text. TacPAC was retained for within-chunk tactile correction with 20 physical trials per method and task; DreamAvoid for trigger--future--rerank physical execution with 40 trials per task and method; and WHIRL for turning physical HIL takeover labels into actor-side predictive risk shaping. CoWAM was not added to the manuscript because all eight tasks are simulated, although its matched candidate-pool design is retained in Batch 17 as a methodological boundary. The three retained studies use one physical platform each. None supports cross-platform, cross-operator, calibrated abstention, or open-distribution recovery claims.

### R29: Generalization-Contract Check

The R21 delta was screened for sim-to-real, viewpoint, compositional, transfer, and cross-task terms. Four primary arXiv full texts were retained because they test distinct changes rather than repeating a generic generalization claim: synthetic-only training to one real Franka, held-out simulated camera regions, unseen object--receptacle compositions on one YAM platform, and human-video-specified unseen task configurations on one bimanual Franka. The evidence is recorded by changed variable, adaptation budget, endpoint, and denominator. No retained study evaluates the same WAM across multiple physical robot platforms or operators under a common protocol.

### R30: Formal Publication Versions IV

Four cited records were checked against arXiv, the official ECCV 2026 accepted-paper list, and an institutional publication record. DexWM was confirmed on the ECCV 2026 accepted list, which remains preliminary pending publisher checks, and Audio-WM was confirmed as an ICRA 2026 workshop paper whose author-hosted accepted manuscript lists no DOI. Both remain `@misc` entries because this check found no formal per-paper proceedings record. V-JEPA 2 and ADriver-I remain preprints after no official venue page was found in this check. The audit records status rather than changing any experimental interpretation, and it does not treat search failure as proof that no later formal version exists.

### R31: V-JEPA Policy Full-Text Check

The V-JEPA 2 formal-version check surfaced the new arXiv record *V-JEPA Policy: Building Effective World-Action Models on Predictive Visual Latents*. Exact arXiv-ID and title checks found no match in the 929-row catalog, either external-candidate set, the gap tracker, or the manuscript bibliography. Primary arXiv full text was inspected. The paper was retained because it adds a matched future-loss control, predictor-only pretraining transfer, and two physical tasks with 20 trials each. Batch 19 records that the predictor is not candidate-action-conditioned, the ablation uses one training seed, upstream pretraining adds data and computation, and physical evidence remains limited to one platform. This is a post-freeze corpus amendment, not evidence that the latest-paper search is exhaustive.

### R32: JEPA Policy Closest-Work Check

VLA-JEPA and JEPA-WAM were selected as direct methodological neighbors of V-JEPA Policy rather than as a broad new-paper sweep. Exact title and arXiv-ID checks found VLA-JEPA in the first external-candidate set but not the 929-row catalog; JEPA-WAM was already represented by three catalog rows and one publication family. Primary arXiv full text was inspected for both. VLA-JEPA was retained because its human-video ablation is positive on LIBERO-Plus but small or negative on other benchmarks, providing an adversarial check against a universal pretraining claim. JEPA-WAM was retained for matched representation, target, and interface ablations and for a five-task physical protocol with rollout-level records. Batch 20 records that JEPA-WAM removes transition prediction at deployment, both studies use one physical platform with ten rollouts per task and setting, and neither provides candidate-action-conditioned online rollout. This focused neighbor check does not establish coverage of all 2026 JEPA--VLA work.

### R33: JEPA-VLA Predictive-Representation Check

The first external-candidate list's high-priority record *JEPA-VLA: Video Predictive Embedding is Needed for VLA Models* was checked against the catalog, delta candidates, supplement tracker, and manuscript by exact title and arXiv ID. It was absent from the 929-row catalog and tracked supplements, so it was retained as one additional post-freeze amendment. Primary arXiv full text was inspected. The paper contributes matched within-implementation comparisons for adding frozen V-JEPA 2 history embeddings to basic and OpenVLA-OFT policies, but the intervention also adds encoder capacity and fusion modules. Batch 21 records that no downstream future target or transition model is trained, the physical study is one task with an ambiguous per-condition denominator, Table 7 duplicates a DINOv2 label, and no multi-seed or systems-cost results are reported. It is used as a predictive-pretraining representation boundary, not as online world-model evidence.

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
| V01 | Formal publication-version resolution for remaining preprints; 23 cited records checked in R14--R16 and R30 | Partially complete; 14 records were upgraded or completed, two acceptance statuses were resolved without inventing proceedings metadata, and some canonical citations may still change |
| S01 | Title/abstract and full-text exclusion log with reasons | No final PRISMA flow count |
| P01 | Independent PRESS-style review of the search strategy | Search design has only internal review |

## Assurance Statement

Current discovery assurance is **adequate for bounded claims**. The log makes completed rapid-scan work traceable where records exist and reproducible only where exact query provenance was retained; it also exposes where provenance is missing. It is insufficient for claims that the corpus is exhaustive, that 758 is a final unique-paper count, or that omitted work is absent from the field.
