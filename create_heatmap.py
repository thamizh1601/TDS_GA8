import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors
from PIL import Image

# Read the Excel file
df = pd.read_excel(r'd:\IIT\Data Science Diploma\TDS\GA8\q4\q-excel-correlation-heatmap.xlsx')

# Calculate correlation matrix
corr_matrix = df.corr()

# Create Red-White-Green colormap (like Excel conditional formatting)
colors = ['#F8696B', '#FFFFFF', '#63BE7B']  # Red, White, Green
cmap = mcolors.LinearSegmentedColormap.from_list('excel_rwg', colors)

# Create figure
fig, ax = plt.subplots(figsize=(6, 5), dpi=100)

# Create heatmap
sns.heatmap(
    corr_matrix, 
    annot=True, 
    fmt='.2f',
    cmap=cmap,
    center=0,
    vmin=-1,
    vmax=1,
    square=True,
    linewidths=0.5,
    linecolor='gray',
    cbar_kws={'shrink': 0.8, 'label': 'Correlation'},
    ax=ax,
    annot_kws={'size': 9}
)

# Style
ax.set_title('Supply Chain Metrics Correlation Matrix', fontsize=11, fontweight='bold', pad=10)
plt.xticks(rotation=45, ha='right', fontsize=8)
plt.yticks(rotation=0, fontsize=8)
plt.tight_layout()

# Save
output_path = r'd:\IIT\Data Science Diploma\TDS\GA8\q4\heatmap.png'
plt.savefig(output_path, dpi=100, bbox_inches='tight', facecolor='white', edgecolor='none')
plt.close()

# Resize to 500x500 if needed
img = Image.open(output_path)
img_resized = img.resize((500, 500), Image.Resampling.LANCZOS)
img_resized.save(output_path)

print(f"Heatmap saved to: {output_path}")
print(f"Final size: 500x500 pixels")
