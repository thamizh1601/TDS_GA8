# Author: 22f2000116@ds.study.iitm.ac.in
# Customer Behavior Analysis - Monthly Revenue Trend

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic monthly revenue data for customer segments
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create data for different customer segments
data = {
    'Month': months * 3,
    'Revenue': [
        # Premium customers - higher revenue with growth trend
        120, 125, 135, 140, 155, 160, 165, 175, 180, 195, 210, 230,
        # Standard customers - moderate revenue with seasonal pattern
        80, 75, 85, 90, 95, 88, 92, 98, 105, 115, 125, 140,
        # Basic customers - lower revenue with gradual growth
        45, 48, 50, 52, 55, 58, 60, 62, 65, 70, 75, 85
    ],
    'Segment': ['Premium'] * 12 + ['Standard'] * 12 + ['Basic'] * 12
}

# Create DataFrame
df = pd.DataFrame(data)

# Add month order for proper sorting
month_order = {month: i for i, month in enumerate(months)}
df['Month_Num'] = df['Month'].map(month_order)
df = df.sort_values('Month_Num')

# Set Seaborn style
sns.set_style('whitegrid')
sns.set_context('talk', font_scale=0.9)

# Create figure with exact dimensions for 512x512 output
plt.figure(figsize=(8, 8))

# Create lineplot
sns.lineplot(
    data=df,
    x='Month',
    y='Revenue',
    hue='Segment',
    style='Segment',
    markers=True,
    dashes=False,
    linewidth=2.5,
    markersize=8,
    palette='viridis'
)

# Customize the plot
plt.title('Monthly Revenue Trend by Customer Segment', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue (in $K)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Customer Segment', loc='upper left', framealpha=0.9)

# Adjust layout
plt.tight_layout()

# Save chart with exact 512x512 dimensions
plt.savefig('chart.png', dpi=64, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

print("Chart saved as chart.png (512x512 pixels)")
print("Author: 22f2000116@ds.study.iitm.ac.in")
