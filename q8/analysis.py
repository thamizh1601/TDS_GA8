# Manufacturing Performance Analysis
# Author: 22f2000116@ds.study.iitm.ac.in
# Email: 22f2000116@ds.study.iitm.ac.in
# Generated with LLM assistance (ChatGPT/Claude)

import matplotlib.pyplot as plt
import numpy as np

# Equipment Efficiency Rate - 2024 Quarterly Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
efficiency_rates = [75.38, 76.95, 80.85, 76.46]
industry_target = 90
average_efficiency = 77.41

# Print analysis summary
print("=" * 50)
print("Manufacturing Performance Analysis")
print("Author: 22f2000116@ds.study.iitm.ac.in")
print("=" * 50)
print(f"\nQuarterly Equipment Efficiency Rates (2024):")
for q, rate in zip(quarters, efficiency_rates):
    print(f"  {q}: {rate}")
print(f"\nAverage Efficiency Rate: {average_efficiency}")
print(f"Industry Target: {industry_target}")
print(f"Gap to Target: {industry_target - average_efficiency:.2f} points")
print(f"\nRecommended Solution: Implement Predictive Maintenance Program")
print("=" * 50)

# Create visualization
fig, ax = plt.subplots(figsize=(10, 6))

# Bar chart for quarterly data
bars = ax.bar(quarters, efficiency_rates, color=['#e74c3c', '#e67e22', '#27ae60', '#e74c3c'], 
              edgecolor='black', linewidth=1.2, alpha=0.8)

# Add industry target line
ax.axhline(y=industry_target, color='#2ecc71', linestyle='--', linewidth=2, label=f'Industry Target: {industry_target}')

# Add average line
ax.axhline(y=average_efficiency, color='#3498db', linestyle='-', linewidth=2, label=f'Current Average: {average_efficiency}')

# Add value labels on bars
for bar, rate in zip(bars, efficiency_rates):
    height = bar.get_height()
    ax.annotate(f'{rate}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=12, fontweight='bold')

# Customize the plot
ax.set_xlabel('Quarter', fontsize=12, fontweight='bold')
ax.set_ylabel('Equipment Efficiency Rate (%)', fontsize=12, fontweight='bold')
ax.set_title('Equipment Efficiency Rate - 2024 Quarterly Analysis\n22f2000116@ds.study.iitm.ac.in', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_ylim(70, 95)
ax.legend(loc='upper right', fontsize=10)
ax.grid(axis='y', alpha=0.3)

# Add gap annotation
ax.annotate(f'Gap: {industry_target - average_efficiency:.2f}',
            xy=(3.5, (industry_target + average_efficiency) / 2),
            fontsize=11, color='red', fontweight='bold',
            ha='center')

# Draw arrow showing gap
ax.annotate('', xy=(3.3, industry_target), xytext=(3.3, average_efficiency),
            arrowprops=dict(arrowstyle='<->', color='red', lw=2))

plt.tight_layout()
plt.savefig('efficiency_chart.png', dpi=100, bbox_inches='tight', facecolor='white')
plt.close()

print("\nVisualization saved as: efficiency_chart.png")
print("\nAnalysis complete!")
print("Email: 22f2000116@ds.study.iitm.ac.in")
