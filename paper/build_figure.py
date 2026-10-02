"""Render the survey's interface diagram as publication-editable vector files."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "pdf.fonttype": 42, "svg.fonttype": "none"})
fig, ax = plt.subplots(figsize=(7, 4.6))
fig.subplots_adjust(left=0.025, right=0.985, top=0.97, bottom=0.035)
ax.set(xlim=(0, 14), ylim=(0, 8))
ax.axis("off")
INK, MUTED, GRAY = "#21333B", "#64747A", "#D5DFE2"
TEAL, BLUE, RUST = "#267D76", "#426FA3", "#A26839"


def block(x, y, label, width=2.05, color=TEAL):
    patch = FancyBboxPatch((x, y), width, .74, boxstyle="round,pad=0.035,rounding_size=0.045", linewidth=1.05, edgecolor=color, facecolor="white")
    ax.add_patch(patch)
    ax.text(x + width / 2, y + .37, label, ha="center", va="center", color=INK, fontsize=8, linespacing=1.25)
    return (x, y, width)


def arrow(start, end, color=MUTED):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=10, linewidth=1.1, color=color))


def feedback(y, right=12.7):
    ax.plot([right, right, 1.38, 1.38], [y, y-.34, y-.34, y-.10], color=MUTED, linewidth=.95)
    arrow((1.38, y-.10), (1.38, y+.02))
    ax.text(7.15, y-.51, "new observation / proprioception", ha="center", color=MUTED, fontsize=7)


ax.text(.3, 7.73, "Where does prediction enter the control loop?", fontsize=13, weight="bold", color=INK)
ax.text(.3, 7.36, "Three functional interfaces for organizing the survey", fontsize=8, color=MUTED)

rows = [
    (6.05, "A", "Direct action generation", TEAL, ["Observation\nand goal", "Action policy", "Selected\ncommand", "Robot\ncontroller", "Environment"]),
    (3.80, "B", "Policy proposals reviewed by a reasoner", BLUE, ["Observation\nand goal", "Policy\nproposal", "Reasoner\nreview / edit", "Robot\ncontroller", "Environment"]),
    (1.55, "C", "Action selection through explicit consequence prediction", RUST, ["History +\naction candidates", "Consequence\npredictor", "Evaluate\nand select", "Robot\ncontroller", "Environment"]),
]
xs = [.35, 3.0, 5.65, 8.3, 10.95]
for y, letter, title, color, labels in rows:
    ax.text(.35, y+1.12, letter, fontsize=9, weight="bold", color=color)
    ax.text(.72, y+1.12, title, fontsize=9, weight="bold", color=INK)
    for x, label in zip(xs, labels):
        block(x, y, label, color=color)
    for left, right in zip(xs, xs[1:]):
        arrow((left+2.08, y+.37), (right-.06, y+.37), color)
    feedback(y)
    if letter == "B":
        ax.plot([1.38, 1.38, 6.675], [y+.77, y+.97, y+.97], color=color, linewidth=.95)
        arrow((6.675, y+.97), (6.675, y+.77), color)
    if letter != "C":
        ax.axhline(y-.83, xmin=.025, xmax=.97, linewidth=.6, color=GRAY)

ax.text(.35, .47, "Comparison axes", fontsize=7.5, weight="bold", color=INK)
ax.text(3.0, .47, "Predicted variable", fontsize=7.5, color=RUST)
ax.text(6.2, .47, "Action interface", fontsize=7.5, color=BLUE)
ax.text(9.4, .47, "Operational use", fontsize=7.5, color=TEAL)
ax.text(.35, .08, "Conceptual interfaces. Reasoning alone does not establish an explicit future-state model.", fontsize=7, color=MUTED)

for extension in ("png", "pdf", "svg"):
    fig.savefig(OUT / f"fig01_prediction_policy_interfaces.{extension}", dpi=220, facecolor="white")
plt.close(fig)


fig, ax = plt.subplots(figsize=(7, 4.15))
fig.subplots_adjust(left=0.025, right=0.985, top=0.97, bottom=0.04)
ax.set(xlim=(0, 15), ylim=(0, 8))
ax.axis("off")
OLIVE = "#6D7935"
columns = [
    ("1", "Predicted quantity", ["pixels / latents", "geometry /\ncontact", "reward / value /\nrisk"], TEAL),
    ("2", "Action relation", ["passive context", "action-\nconditioned", "generated /\nrevised"], BLUE),
    ("3", "Operational use", ["representation /\ndata", "planning /\nselection", "policy /\nmonitoring"], RUST),
    ("4", "Evidence setting", ["held-out offline", "simulated\nclosed loop", "physical\nclosed loop"], OLIVE),
    ("5", "Supported claim", ["predictive\ncontent", "decision utility", "operational\nreliability"], "#7B5268"),
]

ax.text(.3, 7.63, "From model design to a supportable Physical AI claim", fontsize=13, weight="bold", color=INK)
ax.text(.3, 7.25, "Read left to right; retain the interface, setting, and denominator", fontsize=8, color=MUTED)

x_positions = [.25, 3.25, 6.25, 9.25, 12.25]
for (number, title, items, color), x in zip(columns, x_positions):
    ax.text(x, 6.61, number, fontsize=8, weight="bold", color="white", ha="center", va="center",
            bbox={"boxstyle": "circle,pad=.28", "facecolor": color, "edgecolor": color})
    ax.text(x + .35, 6.61, title, fontsize=8.3, weight="bold", color=INK, va="center")
    patch = FancyBboxPatch((x, 3.65), 2.48, 2.45, boxstyle="round,pad=0.04,rounding_size=0.04",
                           linewidth=1.05, edgecolor=color, facecolor="white")
    ax.add_patch(patch)
    for index, item in enumerate(items):
        y = 5.48 - index * .73
        ax.plot([x + .18, x + .35], [y, y], linewidth=2.1, color=color)
        ax.text(x + .48, y, item, fontsize=6.9, color=INK, va="center", linespacing=1.05)

for left in x_positions[:-1]:
    arrow((left + 2.54, 4.88), (left + 2.91, 4.88), MUTED)

ax.text(.3, 3.08, "Attribution controls", fontsize=8.8, weight="bold", color=INK)
controls = [
    "matched data\nand compute",
    "fixed candidates\nand controller",
    "ablate predictor\nor use interface",
    "report tasks, trials,\ninterventions, latency",
]
for index, label in enumerate(controls):
    x = .3 + index * 3.65
    patch = FancyBboxPatch((x, 1.15), 3.05, 1.38, boxstyle="round,pad=0.035,rounding_size=0.04",
                           linewidth=.9, edgecolor=GRAY, facecolor="#F7F9F9")
    ax.add_patch(patch)
    ax.text(x + .22, 2.22, f"{index + 1:02d}", fontsize=7, weight="bold", color=MUTED)
    ax.text(x + 1.53, 1.76, label, fontsize=7.8, color=INK, ha="center", va="center", linespacing=1.25)

ax.plot([.3, 14.7], [.75, .75], color=GRAY, linewidth=.7)
ax.text(.3, .35, "Trace, not hierarchy: a farther-right setting changes the supported claim but does not rank every paper.",
        fontsize=7, color=MUTED)

for extension in ("png", "pdf", "svg"):
    fig.savefig(OUT / f"fig02_claim_evidence_trace.{extension}", dpi=220, facecolor="white")
plt.close(fig)

outputs = [OUT / f"fig{number:02d}_{name}.{extension}" for number, name in (
    (1, "prediction_policy_interfaces"), (2, "claim_evidence_trace")) for extension in ("png", "pdf", "svg")]
assert all(path.exists() and path.stat().st_size > 0 for path in outputs)
print("\n".join(str(path) for path in outputs))
