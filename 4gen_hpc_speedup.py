import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Set matplotlib to use standard formatting with LaTeX-like appearance
mpl.rcParams['text.usetex'] = False
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['mathtext.fontset'] = 'cm'

# Data for V100, A100, H100, B200 Dense performance (TFLOPS/TOPS)
precisions = ['FP64', 'FP32', 'TF32', 'FP16/BF16', 'INT8']

# V100 (Volta - 2017): 7.8 FP64, 15.7 FP32, N/A TF32, 125 FP16 Tensor, N/A INT8 Tensor
v100_perf = [7.8, 15.7, 0, 125, 0] 
# A100 (Ampere - 2020): 9.7 FP64, 19.5 FP32, 156 TF32, 312 FP16, 624 INT8
a100_perf = [9.7, 19.5, 156, 312, 624]
# H100 (Hopper - 2022): 34 FP64, 67 FP32, 494.5 TF32, 989 FP16, 1978 INT8
h100_perf = [34, 67, 494.5, 989, 1978] 
# B200 (Blackwell - 2024): 37 FP64, 75 FP32, 1125 TF32, 2250 FP16, 4500 INT8
b200_perf = [37, 75, 1125, 2250, 4500]

# Calculate speedup relative to their own FP64
v100_speedup = [p / v100_perf[0] if p > 0 else 0 for p in v100_perf]
a100_speedup = [p / a100_perf[0] if p > 0 else 0 for p in a100_perf]
h100_speedup = [p / h100_perf[0] if p > 0 else 0 for p in h100_perf]
b200_speedup = [p / b200_perf[0] if p > 0 else 0 for p in b200_perf]

precisions.reverse()
v100_speedup.reverse()
a100_speedup.reverse()
h100_speedup.reverse()
b200_speedup.reverse()

x = np.arange(len(precisions))
width = 0.2

fig, ax = plt.subplots(figsize=(13, 7))

# Plot bars with chronological color grading
bars0 = ax.bar(x - 1.5*width, v100_speedup, width, label='V100 (Volta - 2017)', color='#1d3557', zorder=3)
bars1 = ax.bar(x - 0.5*width, a100_speedup, width, label='A100 (Ampere - 2020)', color='#2a9d8f', zorder=3)
bars2 = ax.bar(x + 0.5*width, h100_speedup, width, label='H100 (Hopper - 2022)', color='#e9c46a', zorder=3)
bars3 = ax.bar(x + 1.5*width, b200_speedup, width, label='B200 (Blackwell - 2024)', color='#e63946', zorder=3)

ax.set_xlabel('Data Format / Precision', fontsize=12, labelpad=10)
ax.set_ylabel('Speedup Multiplier vs Own FP64', fontsize=12, labelpad=10)
# ax.set_title('4 Generations of Datacenter GPUs: Precision Speedup vs FP64', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(precisions)

# Use symmetrical log scale (symlog) to properly handle the zero values (N/A features on Volta)
ax.set_yscale('symlog', base=2, linthresh=1)
ax.set_ylim(0, 256)

ax.minorticks_on()
ax.tick_params(axis='x', which='minor', bottom=False)

ax.grid(which='major', axis='y', linestyle='-', linewidth=0.75, color='gray', alpha=0.6, zorder=0)
ax.grid(which='minor', axis='y', linestyle=':', linewidth=0.75, color='gray', alpha=0.4, zorder=0)

# Add value labels
def add_labels(bars):
    for bar in bars:
        yval = bar.get_height()
        if yval == 0:
            ax.text(bar.get_x() + bar.get_width()/2, 0.2, 'N/A', 
                    ha='center', va='bottom', fontsize=8, fontweight='bold', rotation=90)
        else:
            ax.text(bar.get_x() + bar.get_width()/2, yval * 1.05, f'{yval:.0f}x', 
                    ha='center', va='bottom', fontsize=8, fontweight='bold')

add_labels(bars0)
add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

ax.legend(loc='upper right', fontsize=11)

plt.tight_layout()
plt.savefig('4gen_hpc_speedup.png', dpi=300)