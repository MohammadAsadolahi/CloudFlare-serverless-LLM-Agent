import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.patch.set_facecolor('#0a0e27')
fig.suptitle('SERVERLESS LLM AGENT — PERFORMANCE ANALYTICS', fontsize=18,
             color='white', fontweight='bold', fontfamily='monospace', y=0.98)
fig.text(0.5, 0.95, 'Simulated Benchmarks · Cloudflare Edge Network · Global Deployment',
         ha='center', fontsize=10, color='#B0BEC5', style='italic')

colors = ['#4285F4', '#EA4335', '#FBBC04', '#34A853', '#8E24AA', '#FF6D00']

# --- Plot 1: Latency Distribution ---
ax1 = axes[0, 0]
ax1.set_facecolor('#1a1e3a')
np.random.seed(42)
edge_latency = np.random.gamma(2, 15, 1000)
traditional_latency = np.random.gamma(3, 80, 1000)
ax1.hist(edge_latency, bins=50, alpha=0.8, color='#00E5FF',
         label='Edge Workers (P50: 28ms)', density=True)
ax1.hist(traditional_latency, bins=50, alpha=0.5, color='#EA4335',
         label='Traditional Server (P50: 240ms)', density=True)
ax1.set_xlabel('Response Latency (ms)', color='#B0BEC5', fontsize=10)
ax1.set_ylabel('Density', color='#B0BEC5', fontsize=10)
ax1.set_title('Request Latency Distribution', color='white',
              fontweight='bold', fontsize=13, pad=10)
ax1.legend(fontsize=9, facecolor='#1a1e3a',
           edgecolor='#546E7A', labelcolor='white')
ax1.tick_params(colors='#B0BEC5')
ax1.spines['bottom'].set_color('#546E7A')
ax1.spines['left'].set_color('#546E7A')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.axvline(x=28, color='#00E5FF', linestyle='--', alpha=0.7, linewidth=1.5)
ax1.axvline(x=240, color='#EA4335', linestyle='--', alpha=0.7, linewidth=1.5)

# --- Plot 2: Throughput Under Load ---
ax2 = axes[0, 1]
ax2.set_facecolor('#1a1e3a')
concurrent = [10, 50, 100, 250, 500, 1000, 2500, 5000, 10000]
edge_throughput = [98, 97, 96, 95, 94, 93, 91, 88, 85]
trad_throughput = [99, 95, 88, 72, 55, 38, 20, 8, 3]
ax2.plot(concurrent, edge_throughput, '-o', color='#00E5FF', linewidth=2.5, markersize=7,
         label='Edge Workers', zorder=3)
ax2.fill_between(concurrent, edge_throughput, alpha=0.15, color='#00E5FF')
ax2.plot(concurrent, trad_throughput, '-s', color='#EA4335', linewidth=2.5, markersize=7,
         label='Traditional Server', zorder=3)
ax2.fill_between(concurrent, trad_throughput, alpha=0.15, color='#EA4335')
ax2.set_xlabel('Concurrent Requests', color='#B0BEC5', fontsize=10)
ax2.set_ylabel('Success Rate (%)', color='#B0BEC5', fontsize=10)
ax2.set_title('Throughput Under Concurrency Load', color='white',
              fontweight='bold', fontsize=13, pad=10)
ax2.set_xscale('log')
ax2.legend(fontsize=9, facecolor='#1a1e3a',
           edgecolor='#546E7A', labelcolor='white')
ax2.tick_params(colors='#B0BEC5')
ax2.spines['bottom'].set_color('#546E7A')
ax2.spines['left'].set_color('#546E7A')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_ylim(0, 105)
ax2.grid(True, alpha=0.15, color='#546E7A')

# --- Plot 3: Global Edge PoP Latency ---
ax3 = axes[1, 0]
ax3.set_facecolor('#1a1e3a')
regions = ['US East', 'US West', 'EU West', 'EU Central',
           'Asia Pacific', 'Middle East', 'S. America', 'Africa']
edge_lat = [22, 18, 25, 28, 35, 42, 38, 55]
origin_lat = [45, 180, 120, 140, 280, 320, 250, 380]
x = np.arange(len(regions))
width = 0.35
bars1 = ax3.bar(x - width/2, edge_lat, width, label='Edge Workers',
                color='#00E5FF', alpha=0.85, zorder=3)
bars2 = ax3.bar(x + width/2, origin_lat, width,
                label='Origin Server (US-East)', color='#EA4335', alpha=0.7, zorder=3)
ax3.set_xlabel('Region', color='#B0BEC5', fontsize=10)
ax3.set_ylabel('Avg Latency (ms)', color='#B0BEC5', fontsize=10)
ax3.set_title('Global Edge PoP Latency Comparison',
              color='white', fontweight='bold', fontsize=13, pad=10)
ax3.set_xticks(x)
ax3.set_xticklabels(regions, rotation=30, ha='right', fontsize=8)
ax3.legend(fontsize=9, facecolor='#1a1e3a',
           edgecolor='#546E7A', labelcolor='white')
ax3.tick_params(colors='#B0BEC5')
ax3.spines['bottom'].set_color('#546E7A')
ax3.spines['left'].set_color('#546E7A')
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.grid(axis='y', alpha=0.15, color='#546E7A')
# Add improvement labels
for i, (e, o) in enumerate(zip(edge_lat, origin_lat)):
    improvement = f'{((o-e)/o*100):.0f}%↓'
    ax3.text(i, o + 12, improvement, ha='center', va='bottom', fontsize=7,
             color='#34A853', fontweight='bold')

# --- Plot 4: Cost Efficiency & Scalability ---
ax4 = axes[1, 1]
ax4.set_facecolor('#1a1e3a')
requests_per_month = [1e3, 1e4, 1e5, 1e6, 1e7, 1e8]
edge_cost = [0, 0, 0.5, 5, 50, 500]
ec2_cost = [8.5, 8.5, 12, 45, 350, 3200]
lambda_cost = [0, 0.2, 2, 20, 200, 2000]
ax4.plot(requests_per_month, edge_cost, '-o', color='#00E5FF', linewidth=2.5, markersize=7,
         label='CF Workers', zorder=3)
ax4.plot(requests_per_month, ec2_cost, '-s', color='#EA4335', linewidth=2.5, markersize=7,
         label='AWS EC2', zorder=3)
ax4.plot(requests_per_month, lambda_cost, '-^', color='#FBBC04', linewidth=2.5, markersize=7,
         label='AWS Lambda', zorder=3)
ax4.set_xlabel('Requests per Month', color='#B0BEC5', fontsize=10)
ax4.set_ylabel('Monthly Cost ($)', color='#B0BEC5', fontsize=10)
ax4.set_title('Cost Efficiency at Scale', color='white',
              fontweight='bold', fontsize=13, pad=10)
ax4.set_xscale('log')
ax4.set_yscale('log')
ax4.legend(fontsize=9, facecolor='#1a1e3a',
           edgecolor='#546E7A', labelcolor='white')
ax4.tick_params(colors='#B0BEC5')
ax4.spines['bottom'].set_color('#546E7A')
ax4.spines['left'].set_color('#546E7A')
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.grid(True, alpha=0.15, color='#546E7A')
# Free tier annotation
ax4.annotate('FREE TIER\n100K req/day', xy=(1e5, 0.5), fontsize=8, color='#00E5FF',
             fontweight='bold', ha='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#0a0e27', edgecolor='#00E5FF', alpha=0.8))

plt.tight_layout(rect=[0, 0.02, 1, 0.93])
fig.text(0.5, 0.01,
         'Designed by Mohammad E. Asadolahi  ·  Chief AI Officer @ Google  ·  Simulated Performance Benchmarks',
         ha='center', fontsize=9, color='#546E7A', style='italic')
plt.savefig('docs/performance_benchmarks.png', dpi=200, bbox_inches='tight',
            facecolor='#0a0e27', edgecolor='none')
plt.close()
print("Performance benchmarks saved.")
