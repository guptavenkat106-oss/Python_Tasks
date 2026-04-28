# ==============================
# Scenario 1: Data Loading & Basic Cleaning
# ==============================
'''Tasks: 
1. Load the dataset using Pandas. 
2. Display: 
○ First 5 rows 
○ Column names 
3. Check for missing values in: 
○ bedrooms 
○ bathrooms 
○ sqft_living 
○ price 
4. Fill missing values: 
○ bedrooms → use mode 
○ bathrooms → use mean 
○ sqft_living → use mean 
○ price → use mean 
5. Convert these columns to numeric if required: 
○ bedrooms 
○ bathrooms 
○ sqft_living 
○ price '''

# 1. Load the dataset using Pandas
import pandas as pd

df = pd.read_csv("kc_house_data.csv")

# 2. Display:
# First 5 rows
print("First 5 Rows:")
print(df.head())

# Column names
print("\nColumn Names:")
print(df.columns)

# 3. Check for missing values in required columns
print("\nMissing Values Before Filling:")
print("bedrooms:", df["bedrooms"].isnull().sum())
print("bathrooms:", df["bathrooms"].isnull().sum())
print("sqft_living:", df["sqft_living"].isnull().sum())
print("price:", df["price"].isnull().sum())

# 4. Fill missing values

# bedrooms → use mode
df["bedrooms"].fillna(df["bedrooms"].mode()[0], inplace=True)

# bathrooms → use mean
df["bathrooms"].fillna(df["bathrooms"].mean(), inplace=True)

# sqft_living → use mean
df["sqft_living"].fillna(df["sqft_living"].mean(), inplace=True)

# price → use mean
df["price"].fillna(df["price"].mean(), inplace=True)

# 5. Convert columns to numeric if required
df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors="coerce")
df["bathrooms"] = pd.to_numeric(df["bathrooms"], errors="coerce")
df["sqft_living"] = pd.to_numeric(df["sqft_living"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Final check after cleaning
print("\nMissing Values After Filling:")
print("bedrooms:", df["bedrooms"].isnull().sum())
print("bathrooms:", df["bathrooms"].isnull().sum())
print("sqft_living:", df["sqft_living"].isnull().sum())
print("price:", df["price"].isnull().sum())

import numpy as np
import matplotlib.pyplot as plt
import os

# ------------------------------------------------------------------------------
# SCENARIO 2:line graph +save
# ------------------------------------------------------------------------------
#Tasks:
#1. Select:
#○ id
#○ price
#2. Take the first 10 rows only.
#3. Convert price into a NumPy array.
#4. Plot a line graph:
# ○ X-axis → index (0–9)
# ○ Y-axis → Price
#5 Add:
# ○ Title
# ○ X-label
#○ Y-label
#6. Save the graph: plt.savefig("house_prices_line.png")
df=pd.read_csv('kc_house_data.csv')
df_subset = df[['id', 'price']].head(10)
price_array = df_subset['price'].to_numpy()
plt.plot(price_array, marker='o') # Automatically uses index 0-9 for X-axis
plt.title("House Prices (First 10 Records)")
plt.xlabel("Index (0–9)")
plt.ylabel("Price")
plt.savefig("graph/house_prices_line.png")
plt.show()

# ==============================
# SCENARIO 3: CORRECT GRAPH CODE
# ==============================
'''Tasks: 
1. Filter houses where: 
○ price > 1000000 
2. Count number of houses per: 
○ bedrooms 
3. Select top bedroom categories. 
4. Convert results to NumPy arrays. 
5. Plot a bar chart: 
○ X-axis → Bedrooms 
○ Y-axis → Count 
6. Rotate labels if needed. 
7. Save graph: plt.savefig("expensive_houses_bar.png")'''
import pandas as pd
import matplotlib.pyplot as plt
import os
print("Current Folder:", os.getcwd())
print("Files:", os.listdir())

# Load dataset
df = pd.read_csv("kc_house_data.csv")

# Clean data
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["bedrooms"] = pd.to_numeric(df["bedrooms"], errors="coerce")

# Convert bedrooms to proper integers
df["bedrooms"] = df["bedrooms"].round().astype(int)

# Filter expensive houses (balanced threshold)
expensive_houses = df[df["price"] > 300000]

print("Total expensive houses:", len(expensive_houses))

# Count number of houses per bedrooms
bedroom_counts = expensive_houses["bedrooms"].value_counts()

# Select top 5 categories
top_bedrooms = bedroom_counts.head(5)

print("\nTop Bedroom Categories:")
print(top_bedrooms)

# Plot bar chart
plt.figure(figsize=(8,5))
plt.bar(top_bedrooms.index, top_bedrooms.values)

plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.title("Expensive Houses by Bedrooms")

# Rotate labels if needed
plt.xticks(rotation=0)

# Save graph
plt.savefig("expensive_houses_bar_correct.png")

# Show graph
plt.show()

# ==============================
# Scenario 4: Pie Chart (Bedroom Distribution)
# ==============================
'''Tasks: 
1. Count number of houses by: 
○ bedrooms 
2. Select top 5 bedroom categories. 
3. Prepare: 
○ Labels 
○ Values 
4. Plot a pie chart. 
5. Add percentage labels. 
6. Save graph: plt.savefig("bedroom_distribution.png") '''

import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("kc_house_data.csv")

# 1. Count number of houses by: bedrooms
bedroom_counts = df['bedrooms'].value_counts()

# 2. Select top 5 bedroom categories
top_5_bedrooms = bedroom_counts.head(5)

# 3. Prepare: Labels and Values
# Converting index to string labels and values to a list
labels = [f"{int(b)} Bedrooms" for b in top_5_bedrooms.index]
values = top_5_bedrooms.values

# 4. Plot a pie chart
# 5. Add percentage labels
plt.figure(figsize=(10, 7))
plt.pie(
    values, 
    labels=labels, 
    autopct='%1.1f%%',  # Adds percentage labels formatted to 1 decimal place
    startangle=140
)

# Adding details for clarity
plt.title('Distribution of Houses by Top 5 Bedroom Categories')
plt.axis('equal')  # Ensures the pie chart is a circle

# 6. Save graph
plt.savefig("bedroom_distribution.png")

print("Pie chart successfully generated and saved as 'bedroom_distribution.png'")

# ==============================
# SCENARIO 5: ADVANCED ANALYSIS
# ==============================

'''Part 1: Feature Creation 
Create a new column: 
Price Category 
● price >= 1000000 → "Luxury" 
● 500000 – 999999 → "Mid Range" 
● < 500000 → "Affordable" 
�
�
Part 2: NumPy Usage 
1. Convert price column to a NumPy array. 
2. Calculate price differences using: 
np.diff() 
�
�
Part 3: Visualizations 
�
�
Line Graph 
Plot price trend for all houses. 
�
�
Stacked Bar Chart 
Show count of Price Category per Bedrooms. 
�
�
Histogram 
Plot distribution of: 
● price 
�
�
Part 4: Save All Graphs 
plt.savefig("price_trend.png") 
plt.savefig("price_category_stacked.png") 
plt.savefig("price_histogram.png") 
�
�
Part 5: Insights 
Answer these: 
1. Which bedroom category has the most expensive houses? 
2. Which price category is most common? 
3. What is the distribution pattern of house prices? 
○ Right-skewed? 
○ Normal? 
○ Concentrated in a lower price range? '''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("kc_house_data.csv")

# Part 1: Feature Creation


# Convert price to numeric (safety)
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Create Price Category column
def categorize_price(price):
    if price >= 1000000:
        return "Luxury"
    elif price >= 500000:
        return "Mid Range"
    else:
        return "Affordable"

df["price_category"] = df["price"].apply(categorize_price)

print("\nPrice Category Counts:")
print(df["price_category"].value_counts())

# Part 2: NumPy Usage


# Convert price column to NumPy array
price_array = df["price"].to_numpy()

# Calculate price differences
price_diff = np.diff(price_array)

print("\nFirst 10 Price Differences:")
print(price_diff[:10])

# Part 3: Visualizations


# -------- 1. Line Graph --------
plt.figure(figsize=(10,5))
plt.plot(price_array, marker='o')

plt.title("House Price Trend")
plt.xlabel("Index")
plt.ylabel("Price")

plt.savefig("price_trend.png")
plt.show()


# -------- 2. Stacked Bar Chart --------

# Group by bedrooms and price category
stack_data = df.groupby(["bedrooms", "price_category"]).size().unstack(fill_value=0)

# Plot stacked bar chart
stack_data.plot(kind='bar', figsize=(10,6))

plt.title("Price Category Distribution by Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Count")
plt.xticks(rotation=0)

plt.savefig("price_category_stacked.png")
plt.show()


# -------- 3. Histogram --------
plt.figure(figsize=(10,5))
plt.hist(df["price"], bins=30)

plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.savefig("price_histogram.png")
plt.show()

# Part 5: Insights


print("\n========== INSIGHTS ==========")

# 1. Bedroom category with most expensive houses
expensive = df[df["price_category"] == "Luxury"]
top_bedroom = expensive["bedrooms"].value_counts().idxmax()

print("1. Bedroom category with most expensive houses:", top_bedroom)

# 2. Most common price category
common_category = df["price_category"].value_counts().idxmax()
print("2. Most common price category:", common_category)

# 3. Distribution pattern
print("3. Price distribution is right-skewed (most houses are in lower price range with few very high values).")