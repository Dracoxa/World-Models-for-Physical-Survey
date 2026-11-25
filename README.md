<div align="center">

# World Models for Physical AI

### Interfaces, Experimental Evidence, and Downstream Utility

[![Website](https://img.shields.io/badge/Website-GitHub_Pages-1d4ed8?style=flat-square)](https://dracoxa.github.io/World-Models-for-Physical-Survey/)
[![Journal Preview](https://img.shields.io/badge/PDF-ACM_Preview_(33p)-0f766e?style=flat-square)](docs/assets/survey.pdf)
[![Review Manuscript](https://img.shields.io/badge/PDF-Review_Draft_(31p)-334155?style=flat-square)](docs/assets/survey-review.pdf)
[![Evidence Companion](https://img.shields.io/badge/Data-Evidence_Companion_(75%20%2F%2093)-b45309?style=flat-square)](docs/assets/Evidence-companion.zip)
[![Candidate Pool](https://img.shields.io/badge/Index-Literature_Catalog_(781)-64748b?style=flat-square)](literature/current/README.md)

*An ACM Computing Surveys (CSUR) anonymous review manuscript & reproducible evidence companion auditing when learned environmental predictions improve physical learning, planning, action generation, evaluation, and runtime control.*

</div>

---

## Core Takeaway

Learned world models predict how physical environments evolve, yet higher forecast accuracy does not automatically improve physical behavior. Forecasts enter Physical AI systems through distinct interfaces—**training supervision**, **candidate-plan scoring**, **action-generation context**, **offline policy evaluation**, or **runtime correction**—and each interface requires its own experimental control.

Across **93 source-linked comparisons** drawn from **75 purposively selected Physical AI studies** (**56** with simulated or physical execution outcomes; **29** with qualifying component tests, or **26** after removing four bundled branch/scoring records across three studies), anchored quantitatively in robotic manipulation with autonomous driving and navigation as cross-domain interface contrasts:

- **Training supervision vs. deployment readout**: Objective ablations consistently show training-time future supervision aiding policy learning even when deployment omits future generation (*Fast-WAM Base*, *DyPES-VLA*, *Cosmos Policy*). Matched execution component controls remain sparse for deployment-time action generation (**2** after unbundling) and runtime intervention (**1**).
- **Candidate pool & closed-loop reversal**: Test-time selection depends first on mixed-outcome headroom (*Yuan et al.*: only 6 of 48 restored states offer reranking gain) and second on closed-loop alignment (*GeoBoN*: offline trajectory fit reverses online, `77.4%` vs. `82.5%`).
- **Evaluator agreement ≠ training utility**: In *DexTouch-WM*, the simulator with higher evaluator correlation (`WM-Mix`, `r = 0.844` vs. `0.646`) trains lower-scoring policies for two of three new learners.
- **Task-level benchmark forensics** (10 Nov 2026 frozen snapshots):
  - **RoboTwin 2.0** (33 configs · 1,650 clean/randomized task pairs): **32 / 33** configs (**27 / 28** co-trained) drop in mean success under scene randomization; **12 / 33** (**11 / 28** co-trained) decline on **all 50 tasks**; even *GigaBrain-0.7* still declines on 18 tasks.
  - **RoboDojo** (66 configs · 3,536 visible cells): **858 / 3,536 cells (`24.3%`)** receive partial-progress `Score` credit despite `0%` binary completion (every config affected; median **13**, range **3–26**).

---

## Quick Access

| Artifact | Description | Link |
| :--- | :--- | :--- |
| **Interactive Companion Website** | Search all 93 source-linked comparisons, toggle the `29 → 26` sensitivity check, explore RoboTwin/RoboDojo task profiles, and inspect all 7 survey figures | [dracoxa.github.io/World-Models-for-Physical-Survey](https://dracoxa.github.io/World-Models-for-Physical-Survey/) |
| **ACM Journal Preview PDF** | Formatted `acmsmall` preview (33 pages, anonymous, 110 references) | [`docs/assets/survey.pdf`](docs/assets/survey.pdf) |
| **Review Draft PDF** | Line-numbered `manuscript,review` submission draft (31 pages, anonymous) | [`docs/assets/survey-review.pdf`](docs/assets/survey-review.pdf) |
| **Evidence Companion Archive** | `papers.csv`, `comparisons.csv`, `coding_decisions.csv`, `summarize.py`, `benchmark_tasks.zip`, and 18-sheet `Quantitative_Analysis.xlsx` | [`docs/assets/Evidence-companion.zip`](docs/assets/Evidence-companion.zip) |
| **Broader Discovery Catalog** | 781 deduplicated candidate records (2026-10-10 discovery snapshot; distinct from the 75-study audited evidence core) | [`literature/current/README.md`](literature/current/README.md) · [`catalog.csv`](literature/current/catalog.csv) |

---

## Survey Structure (4 Parts · 17 Subsections)

1. **Part 1 — From Prediction to Physical Action** (`§1.1–§1.4`): Predictive target, action query ($p_\theta(y_{t+1:t+H}\mid h_t, a_{t:t+H-1})$ vs. goal-conditioned/joint/policy interfaces), six evaluation dimensions (`L1–L6`), corpus scope (`75 / 93`), and comparison with 7 recent 2026 surveys (`Table 1`).
2. **Part 2 — Information Requirements for Downstream Use** (`§2.1–§2.3`): Command-consequence grounding (`V-JEPA 2`, `DreamDojo`, `DROID`, `DexTouch-WM`, `REBOOT`), state initialization and recursive rollout (`GNS`, `ContactWorld`, `AVID`, `OmniVTA`), and history/viewpoint/embodiment transfer (`UniSim`, `SCVC`, `DyPES-VLA`).
3. **Part 3 — How Predictions Enter Learning and Action** (`§3.1–§3.5`): Training supervision (`Fast-WAM`, `MBPO`, `PWM`, `VLAW`, `WMPO`), candidate selection (`PETS`, `TD-MPC2`, `GeoBoN`, `Yuan et al.`, `Drive-WM`, `ContactWorld`), action generation (`V-JEPA Policy`, `DreamZero`, `JOPAT`, `Cosmos Policy`, `DAWN`, `NavForesee`), policy evaluators (`IWS`, `DexTouch-WM`, `Mem-World`), and runtime timing/safety (`FutureRTC`, `TacPAC`, `VLA-FixBench`, `DreamAvoid`, `SMBPO`).
4. **Part 4 — Evaluating Downstream Utility and Reliability** (`§4.1–§4.5`): RoboTwin 2.0 & RoboDojo task-level forensics, `Table 9` attribution summary (`75 / 56 / 29 (26)`), synthesis, and three falsifiable controlled follow-up tests (`Table 10`).

---

## Local Website Preview & Validation

The GitHub Pages site (`docs/`) requires no Node/bundler build step:

```bash
# Validate HTML anchors, local assets, 7 figures, and JSON counts (75/93, 33/66/858)
python3 docs/check_site.py

# Preview locally
python3 -m http.server 8000 --directory docs
```

Pushing changes in `docs/` to `main` automatically deploys via [`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml).

---

## Citation (Anonymous Preprint)

```bibtex
@article{anonymous2026worldmodelsphysical,
  title   = {World Models for Physical AI: Interfaces, Experimental Evidence, and Downstream Utility},
  author  = {Anonymous Author(s)},
  journal = {ACM Computing Surveys (manuscript under review)},
  year    = {2026},
  note    = {Evidence companion snapshot: 2026-11-22; benchmark snapshot: 2026-11-10}
}
```
