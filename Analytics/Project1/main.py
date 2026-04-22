import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =================================================================
# SCENARIO 1: Basic Data Loading & Cleaning
# =================================================================
# 1. Load the dataset
df = pd.read_csv('railway_gauges.csv')

# 2. Display preview
print("--- Scenario 1: Data Preview ---")
print(df.head())
print("\nColumn Names:", df.columns.tolist())

# 3. Check for missing values and replace them with 0
df.fillna(0, inplace=True)

# 4. Convert all gauge columns to numeric types
gauge_cols = ['Broad', 'Metre', 'Narrow', 'Total']
df[gauge_cols] = df[gauge_cols].apply(pd.to_numeric, errors='coerce')

# =================================================================
# SCENARIO 2: Simple Visualization
# =================================================================
# 1 & 2. Plotting Total tracks over years
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Total'], marker='o', linestyle='-', color='teal', label='Total Track Length')

# 3. Adding Title and Labels
plt.title('Scenario 2: Total Railway Track Growth Over Years')
plt.xlabel('Year')
plt.ylabel('Distance (km)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

# 4. Trend Identification: The trend is generally increasing.

# =================================================================
# SCENARIO 3: Filtering + Bar Chart
# =================================================================
# 1. Filter for years after 2000
modern_df = df[df['Year'] > 2000].copy()

# 2 & 3. Plot a grouped bar chart for Broad, Metre, and Narrow Gauges
modern_df.plot(x='Year', y=['Broad', 'Metre', 'Narrow'], kind='bar', figsize=(12, 6))

# 4. Add labels and legend
plt.title('Scenario 3: Gauge Comparison (Post-2000)')
plt.ylabel('Distance (km)')
plt.xlabel('Year')
plt.legend(title='Gauge Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Insight: Broad Gauge significantly dominates in recent years.

# =================================================================
# SCENARIO 4: Feature Engineering + Pie Chart
# =================================================================
# 1 & 2. Calculate total sum and create structure
gauge_totals = df[['Broad', 'Metre', 'Narrow']].sum()

# 3 & 4. Plot pie chart with percentage labels
plt.figure(figsize=(7, 7))
plt.pie(gauge_totals, labels=gauge_totals.index, autopct='%1.1f%%', startangle=140, 
        colors=['#66b3ff', '#ff9999', '#99ff99'])
plt.title('Scenario 4: Historical Contribution by Gauge Type')
plt.show()

# 5. Interpretation: Broad Gauge contributes the largest share to the network.

# =================================================================
# SCENARIO 5: Advanced Analysis + Multiple Graphs
# =================================================================
# 1. Create Percentage Columns
df['% Broad'] = (df['Broad'] / df['Total']) * 100
df['% Metre'] = (df['Metre'] / df['Total']) * 100
df['% Narrow'] = (df['Narrow'] / df['Total']) * 100

# 2. Use NumPy to calculate yearly growth
df['Yearly_Growth'] = np.append([0], np.diff(df['Total']))

# 3a. Line Graph for all gauges
plt.figure(figsize=(10, 5))
for col in ['Broad', 'Metre', 'Narrow']:
    plt.plot(df['Year'], df[col], label=col, marker='.')
plt.title('Scenario 5a: Individual Gauge Trends')
plt.xlabel('Year')
plt.ylabel('Distance (km)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 3b. Stacked bar chart showing composition
df.plot(x='Year', y=['Broad', 'Metre', 'Narrow'], kind='bar', stacked=True, 
        figsize=(12, 6), color=['#66b3ff', '#ff9999', '#99ff99'])
plt.title('Scenario 5b: Railway Gauge Composition (Stacked)')
plt.ylabel('Distance (km)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Highlights
highest_growth_year = df.loc[df['Yearly_Growth'].idxmax(), 'Year']
metre_decline = df['Metre'].iloc[-1] < df['Metre'].iloc[0]

print("\n--- Scenario 5: Final Insights ---")
print(f"Year with highest growth: {highest_growth_year}")
print(f"Decline observed in Metre Gauge: {metre_decline}")

# 5. Final Conclusion
print("\nConclusion: Is the railway system shifting towards a single dominant gauge?")
print("Yes. The visualizations clearly show that while the total network grows, "
      "Broad Gauge is expanding rapidly while Metre and Narrow Gauges are being "
      "phased out, confirming a move toward a single dominant gauge.")