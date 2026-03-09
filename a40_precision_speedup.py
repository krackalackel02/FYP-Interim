import matplotlib.pyplot as plt
import matplotlib as mpl

# Set matplotlib to use LaTeX-style formatting (Computer Modern)
mpl.rcParams['text.usetex'] = False
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['mathtext.fontset'] = 'cm'

# Data for NVIDIA A40 Dense performance
precisions = ['FP64', 'FP32', 'TF32', 'FP16 / BF16', 'INT8']
performance = [0.584375, 37.4, 74.8, 149.7, 299.3]


# Calculate speedup relative to FP64
speedup = [p / performance[0] for p in performance]
precisions.reverse()
performance.reverse()
speedup.reverse()

fig, ax = plt.subplots(figsize=(10, 6))

# Adding zorder=3 ensures bars are drawn on top of the background grids
bars = ax.bar(precisions, speedup, color=['#e63946', '#f4a261', '#e9c46a', '#2a9d8f', '#264653', '#1d3557'], zorder=3)

# ax.set_title('NVIDIA A40: Relative Speedup by Precision (Dense)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Data Format / Precision', fontsize=12, labelpad=10)
ax.set_ylabel('Speedup Multiplier vs FP64', fontsize=12, labelpad=10)

ax.set_yscale('log', base=2)
ax.set_ylim(0.5, 2048)

# Enable minor ticks
ax.minorticks_on()
# Disable minor ticks on the x-axis since it's categorical data
ax.tick_params(axis='x', which='minor', bottom=False)

# Add major and minor grids to the y-axis (zorder=0 places them behind the bars)
ax.grid(which='major', axis='y', linestyle='-', linewidth=0.75, color='gray', alpha=0.6, zorder=0)
ax.grid(which='minor', axis='y', linestyle=':', linewidth=0.75, color='gray', alpha=0.4, zorder=0)

# Add value labels on top of bars
for bar, mult in zip(bars, speedup):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval * 1.15, f'{mult:.0f}x', 
            ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('a40_precision_speedup_latex.png', dpi=300)