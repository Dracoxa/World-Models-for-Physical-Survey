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
print(OUT / "fig01_prediction_policy_interfaces.png")
