import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(16, 9))
fig.patch.set_facecolor('#0a0e27')
ax.set_facecolor('#0a0e27')
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')

# Color palette
colors = {
    'client': '#4285F4',
    'worker1': '#EA4335',
    'worker2': '#FBBC04',
    'kv': '#34A853',
    'llm': '#8E24AA',
    'edge': '#FF6D00',
    'bg': '#1a1e3a',
    'text': '#FFFFFF',
    'accent': '#00E5FF',
}


def draw_box(ax, x, y, w, h, color, label, sublabel='', icon=''):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                         facecolor=color, edgecolor='white', linewidth=2, alpha=0.9)
    ax.add_patch(box)
    # Glow effect
    glow = FancyBboxPatch((x-0.05, y-0.05), w+0.1, h+0.1, boxstyle="round,pad=0.2",
                          facecolor='none', edgecolor=color, linewidth=3, alpha=0.3)
    ax.add_patch(glow)
    if icon:
        ax.text(x + w/2, y + h/2 + 0.25, icon, fontsize=20, ha='center', va='center',
                color='white', fontweight='bold')
        ax.text(x + w/2, y + h/2 - 0.15, label, fontsize=11, ha='center', va='center',
                color='white', fontweight='bold', fontfamily='monospace')
    else:
        ax.text(x + w/2, y + h/2 + 0.1, label, fontsize=12, ha='center', va='center',
                color='white', fontweight='bold', fontfamily='monospace')
    if sublabel:
        ax.text(x + w/2, y + h/2 - 0.3, sublabel, fontsize=8, ha='center', va='center',
                color='#B0BEC5', style='italic')


def draw_arrow(ax, x1, y1, x2, y2, color='#00E5FF', label='', style='->', lw=2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                                connectionstyle='arc3,rad=0.1'))
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2 + 0.25
        ax.text(mx, my, label, fontsize=8, ha='center', va='center',
                color=color, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#0a0e27', edgecolor=color, alpha=0.8))


# Title
ax.text(8, 8.4, 'SERVERLESS LLM AGENT — SYSTEM ARCHITECTURE', fontsize=18,
        ha='center', va='center', color='white', fontweight='bold', fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.4', facecolor='#1a1e3a', edgecolor='#00E5FF', linewidth=2))
ax.text(8, 7.85, 'Cloudflare Workers · Edge Computing · Async LLM Pipeline', fontsize=10,
        ha='center', va='center', color='#B0BEC5', style='italic')

# Edge Network boundary
edge_box = FancyBboxPatch((2.8, 1.0), 10.5, 5.8, boxstyle="round,pad=0.3",
                          facecolor='none', edgecolor='#FF6D00', linewidth=2, linestyle='--', alpha=0.5)
ax.add_patch(edge_box)
ax.text(8, 6.5, '<<  CLOUDFLARE EDGE NETWORK  >>', fontsize=11, ha='center', va='center',
        color='#FF6D00', fontweight='bold', fontfamily='monospace', alpha=0.8)

# Components
draw_box(ax, 0.3, 3.5, 2.2, 1.5,
         colors['client'], 'CLIENT', 'REST API Consumer', '')
draw_box(ax, 3.5, 3.5, 2.8, 1.5,
         colors['worker1'], 'WORKER 1', 'Job Orchestrator', '')
draw_box(ax, 5.5, 1.3, 2.8, 1.3, colors['kv'], 'KV STORE', 'Cloudflare KV', '')
draw_box(ax, 9.5, 3.5, 2.8, 1.5,
         colors['worker2'], 'WORKER 2', 'LLM Processor', '')
draw_box(ax, 13.2, 3.5, 2.5, 1.5,
         colors['llm'], 'OPENAI', 'GPT-4 / LLM API', '')

# Arrows
draw_arrow(ax, 2.5, 4.25, 3.5, 4.25, '#4285F4', 'POST /request', lw=2.5)
draw_arrow(ax, 6.3, 3.5, 6.9, 2.6, '#34A853', 'PUT job', lw=2)
draw_arrow(ax, 6.9, 2.6, 9.5, 4.0, '#34A853', 'GET job', lw=2)
draw_arrow(ax, 6.3, 4.25, 9.5, 4.25, '#FBBC04', 'ctx.waitUntil()', lw=2.5)
draw_arrow(ax, 12.3, 4.25, 13.2, 4.25, '#8E24AA', 'LLM Prompt', lw=2.5)

# Return arrows
draw_arrow(ax, 3.5, 3.7, 2.5, 3.7, '#00E5FF', 'jobId (202)', '->', lw=1.5)
draw_arrow(ax, 13.2, 3.7, 12.3, 3.7, '#CE93D8', 'Itinerary JSON', '->', lw=1.5)

# Status badges
badges = [
    (1.4, 2.2, 'ASYNC', '#FF6D00'),
    (4.9, 5.7, 'UUID Generation', '#EA4335'),
    (6.9, 5.7, 'Job Queue', '#34A853'),
    (10.9, 5.7, 'Structured Output', '#FBBC04'),
    (14.5, 5.7, 'AI Inference', '#8E24AA'),
]
for x, y, label, color in badges:
    ax.text(x, y, label, fontsize=8, ha='center', va='center', color='white',
            bbox=dict(boxstyle='round,pad=0.3', facecolor=color,
                      edgecolor='none', alpha=0.85),
            fontweight='bold')

# Footer
ax.text(8, 0.35, 'Designed by Mohammad E. Asadolahi  ·  Chief AI Officer @ Google  ·  Edge-Native AI Infrastructure',
        fontsize=9, ha='center', va='center', color='#546E7A', style='italic')

plt.tight_layout()
plt.savefig('docs/architecture_diagram.png', dpi=200, bbox_inches='tight',
            facecolor='#0a0e27', edgecolor='none')
plt.close()
print("Architecture diagram saved.")
