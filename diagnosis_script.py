import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'sans-serif'

# 1. Load Financial Dataset
print("=== LOADING ENTERPRISE DATASET ===")
data = {
    'Year': [2021, 2022, 2023, 2024, 2025],
    'Revenue': [365817, 394328, 383285, 391000, 385000],
    'COGS': [212981, 223546, 214137, 218960, 215600],
    'Gross_Profit': [152836, 170782, 169148, 172040, 169400],
    'RD': [21914, 26251, 29915, 30500, 30800],
    'SGA': [21973, 25094, 24938, 25800, 26950],
    'Net_Income': [94680, 99803, 96995, 100910, 100100],
    'Total_Assets': [351002, 352755, 337418, 345000, 350000],
    'Total_Equity': [63090, 50672, 62146, 68000, 72843]
}
df = pd.DataFrame(data)

# Compute DuPont Drivers
df['Net_Profit_Margin'] = (df['Net_Income'] / df['Revenue']) * 100
df['Asset_Turnover'] = df['Revenue'] / df['Total_Assets']
df['Equity_Multiplier'] = df['Total_Assets'] / df['Total_Equity']
df['ROE'] = (df['Net_Income'] / df['Total_Equity']) * 100

print(df[['Year', 'ROE', 'Net_Profit_Margin', 'Asset_Turnover', 'Equity_Multiplier']])

# 2. Plot DuPont Deconstruction Trend
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Apple Inc. - DuPont Deconstruction History', fontsize=16, fontweight='bold')

sns.lineplot(data=df, x='Year', y='ROE', ax=axes[0,0], marker='o', color='purple', linewidth=2.5)
axes[0,0].set_title('Return on Equity (ROE) %', fontweight='bold')
axes[0,0].set_xticks(df['Year'])

sns.lineplot(data=df, x='Year', y='Net_Profit_Margin', ax=axes[0,1], marker='o', color='teal', linewidth=2.5)
axes[0,1].set_title('Net Profit Margin %', fontweight='bold')
axes[0,1].set_xticks(df['Year'])

sns.lineplot(data=df, x='Year', y='Asset_Turnover', ax=axes[1,0], marker='o', color='coral', linewidth=2.5)
axes[1,0].set_title('Asset Turnover Ratio', fontweight='bold')
axes[1,0].set_xticks(df['Year'])

sns.lineplot(data=df, x='Year', y='Equity_Multiplier', ax=axes[1,1], marker='o', color='crimson', linewidth=2.5)
axes[1,1].set_title('Financial Leverage (Equity Multiplier)', fontweight='bold')
axes[1,1].set_xticks(df['Year'])

plt.tight_layout()
plt.savefig('dupont_deconstruction_trends.png', dpi=300)
print("\n[SUCCESS] Saved DuPont Trend Chart as 'dupont_deconstruction_trends.png'")

# 3. Cost Structure Breakdown Chart
plt.figure(figsize=(8, 6))
costs = ['COGS', 'R&D', 'SG&A', 'Taxes (Est)', 'Net Income']
values = [56, 8, 7, 3, 26]
colors = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c']
plt.pie(values, labels=costs, autopct='%1.1f%%', colors=colors, startangle=140, explode=(0, 0, 0, 0, 0.1))
plt.title('Apple Inc. - Enterprise Value & Cost Structure Deconstruction (2025)', fontsize=14, fontweight='bold')
plt.savefig('cost_structure_breakdown.png', dpi=300)
print("[SUCCESS] Saved Cost Structure Chart as 'cost_structure_breakdown.png'")

print("\nAnalysis completed successfully!")
