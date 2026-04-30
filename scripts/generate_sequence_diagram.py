import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(figsize=(16, 10))
fig.patch.set_facecolor('#0a0e27')
ax.set_facecolor('#0a0e27')
ax.set_xlim(0, 16)
ax.set_ylim(0, 10)
ax.axis('off')

# Title
ax.text(8, 9.5, 'ASYNC JOB LIFECYCLE — SEQUENCE DIAGRAM', fontsize=17,
        ha='center', va='center', color='white', fontweight='bold', fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1e3a', edgecolor='#00E5FF', linewidth=2))

# Actor columns
actors = [
    (2, 'CLIENT', '#4285F4', ''),
    (5.5, 'WORKER 1', '#EA4335', ''),
    (9, 'KV STORE', '#34A853', ''),
    (12.5, 'WORKER 2', '#FBBC04', ''),
    (15, 'OPENAI', '#8E24AA', ''),
]

for x, label, color, icon in actors:
    box = FancyBboxPatch((x-0.7, 8.5), 1.4, 0.7, boxstyle="round,pad=0.1",
                         facecolor=color, edgecolor='white', linewidth=2, alpha=0.9)
    ax.add_patch(box)
    ax.text(x, 8.85, label, fontsize=9, ha='center', va='center',
            color='white', fontweight='bold', fontfamily='monospace')
    # Lifeline
    ax.plot([x, x], [0.3, 8.5], color=color,
            linewidth=1.5, linestyle=':', alpha=0.4)

# Sequence steps
steps = [
    (2, 5.5, 8.0, 'POST {destination, days}', '#4285F4', 'solid'),
    (5.5, 9, 7.3, 'PUT job_{uuid}', '#EA4335', 'solid'),
    (5.5, 12.5, 6.6, 'ctx.waitUntil(fetch)', '#FF6D00', 'dashed'),
    (5.5, 2, 5.9, 'Response 202 {jobId}', '#00E5FF', 'solid'),
    (12.5, 9, 5.2, 'GET job_{uuid}', '#FBBC04', 'solid'),
    (12.5, 15, 4.5, 'LLM Completion Request', '#8E24AA', 'solid'),
    (15, 12.5, 3.8, 'Generated Itinerary JSON', '#CE93D8', 'solid'),
    (12.5, 9, 3.1, 'PUT job_{uuid} [completed]', '#34A853', 'solid'),
    (2, 5.5, 2.3, 'POST {jobId} (poll)', '#4285F4', 'dashed'),
    (5.5, 9, 1.7, 'GET job_{uuid}', '#EA4335', 'solid'),
    (9, 5.5, 1.2, 'Return completed itinerary', '#34A853', 'solid'),
    (5.5, 2, 0.7, 'Response 202 {itinerary}', '#00E5FF', 'solid'),
]

for x1, x2, y, label, color, style in steps:
    ls = '--' if style == 'dashed' else '-'
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='->', color=color, lw=2, linestyle=ls))
    mid_x = (x1 + x2) / 2
    offset = 0.15
    ax.text(mid_x, y + offset, label, fontsize=7.5, ha='center', va='bottom',
            color=color, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.15', facecolor='#0a0e27', edgecolor=color, alpha=0.7, linewidth=0.8))

# Phase separators
ax.axhline(y=5.5, color='#546E7A', linewidth=1,
           linestyle='--', alpha=0.3, xmin=0.05, xmax=0.95)
ax.text(0.5, 5.55, 'ASYNC BOUNDARY', fontsize=8, color='#FF6D00', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#0a0e27', edgecolor='#FF6D00', alpha=0.8))

ax.axhline(y=2.7, color='#546E7A', linewidth=1,
           linestyle='--', alpha=0.3, xmin=0.05, xmax=0.95)
ax.text(0.5, 2.75, 'CLIENT POLL', fontsize=8, color='#4285F4', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#0a0e27', edgecolor='#4285F4', alpha=0.8))

# Footer
ax.text(8, 0.1, 'Designed by Mohammad E. Asadolahi  ·  Chief AI Officer @ Google  ·  Async Edge-Native Pipeline',
        fontsize=9, ha='center', va='center', color='#546E7A', style='italic')

plt.tight_layout()
plt.savefig('docs/sequence_diagram.png', dpi=200, bbox_inches='tight',
            facecolor='#0a0e27', edgecolor='none')
plt.close()
print("Sequence diagram saved.")
