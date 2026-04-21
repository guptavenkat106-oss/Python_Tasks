import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file into a Pandas DataFrame [cite: 6, 8]
# Pandas is a powerful data analysis library for manipulation [cite: 3]
df = pd.read_csv('railway_gauges.csv')

# 2. Display initial data [cite: 8]
# head() displays the first 5 rows and tail() displays the last 5 [cite: 9, 10]
print(df.head())

# 3. Find the year with the maximum total installations [cite: 16]
# idxmax() identifies the index of the first occurrence of the maximum value [cite: 15]
max_year_info = df.iloc[[df['Total'].idxmax()]]
print("Year with maximum installations:")
print(max_year_info)

# 4. Data Visualization [cite: 20]
# Drop 'Total' column before plotting to compare individual gauges [cite: 24]
df_plot = df.drop('Total', axis=1)

# Generate a bar chart using 'Year' for the x-axis [cite: 22, 25]
ax = df_plot.plot(x="Year", kind="bar")

# Configure labels and title [cite: 26, 27, 28, 29]
plt.xticks(rotation=70)
plt.xlabel('Year')
plt.ylabel('Total')
plt.title('Gauges: Number of railway tracks installed per year')

# Save and show the output graph [cite: 29, 30, 31]
plt.savefig('rail_gauges.png')
plt.show()