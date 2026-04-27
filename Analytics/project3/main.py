'''
=================================================================================================================================
---------------------------------------------📊 Project Title: Scottish Hills Data Analysis--------------------------------------
--------------------------------------Analyze Scottish Hills dataset using NumPy, Pandas, Matplotlib-----------------------------
=================================================================================================================================
'''
'''
=================================================================================================================================
 📦 1. Import Required Libraries
=================================================================================================================================
 👉 Import numpy
 👉 Import pandas
 👉 Import matplotlib.pyplot
 👉 (Optional) Import os for folder creation
<Import your libraries>
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

'''
=================================================================================================================================
 🟢 SCENARIO 1: Data Loading & Preprocessing
=================================================================================================================================
�� Tasks:
1. Load the dataset using Pandas.
2. Display:
   ○ First 5 rows (head())
   ○ Column Names
3. Check for missing values in:
   ○ Height, Region
4. Handle missing values:
   ○ Fill numeric column Height with mean
   ○ Fill categorical column Region with mode
5. Convert the Height column into numeric if required.
'''
# ------------------------------
# STEP 1: LOAD DATASET
# ------------------------------
df = pd.read_csv("C:/Users/DELL/OneDrive/Desktop/python tasks/Analytics/project3/scottish_hills.csv")

# ------------------------------
# STEP 2: CONVERT HEIGHT (safety)
# ------------------------------
df["Height"] = pd.to_numeric(df["Height"], errors='coerce')

# ------------------------------
# STEP 3: CREATE REGION COLUMN
# ------------------------------
lat_mid = df["Latitude"].median()
lon_mid = df["Longitude"].median()

def assign_region(row):
    lat = row["Latitude"]
    lon = row["Longitude"]
    
    if lat >= lat_mid and lon >= lon_mid:
        return "North-East"
    elif lat >= lat_mid and lon < lon_mid:
        return "North-West"
    elif lat < lat_mid and lon >= lon_mid:
        return "South-East"
    else:
        return "South-West"

df["Region"] = df.apply(assign_region, axis=1)

# ------------------------------
# STEP 4: HANDLE MISSING VALUES
# ------------------------------
# Fill Height with mean
df["Height"] = df["Height"].fillna(df["Height"].mean())

# Fill Region with mode
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])

# ------------------------------
# STEP 5: OUTPUT
# ------------------------------
print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

'''
=================================================================================================================================
 🟢 SCENARIO 2: Line Graph (Score Trend) + Save
=================================================================================================================================
�� Tasks:
1. Select Hill Name and Height
2. Take first 10 rows only.
3. Convert Height into NumPy arrays.
4. Plot a line graph:
    ○ X-axis → index (0-9)
    ○ Y-axis → Height
5. Add:
    ○ Title
    ○ Axis labels
6. Save the graph: plt.savefig("hill_heights_line.png")
'''

# 1. Select required columns
data = df[['Hill Name', 'Height']]

# 2. Take first 10 rows
data_10 = data.head(10)

# 3. Convert Height to NumPy array
height_array = np.array(data_10['Height'])

# 4. Plot line graph
plt.figure()
plt.plot(range(10), height_array, marker='o')

# 5. Add title and labels
plt.title("Height Variation of First 10 Hills")
plt.xlabel("Index (0–9)")
plt.ylabel("Height")
plt.tight_layout()

# Save the graph
plt.savefig("C:/Users/DELL/OneDrive/Desktop/python tasks/Analytics/project3/scottish_hills.png")

# Show plot
plt.show()

'''
=================================================================================================================================
 🟡 SCENARIO 3: Filtering + Bar Chart + Save
=================================================================================================================================
 �� Tasks:
1. Filter hills where:
    ○ Height > 900
2. Count number of hills per Region.
3. Select top Regions.
4. Convert results into NumPy arrays.
5. Plot a bar chart:
    ○ X-axis → Region
    ○ Y-axis → count
6. Rotate x-axis labels for readability and clarity.
Save the graph: plt.savefig("tall_hills_bar.png")

'''

# 1. Filter hills where Height > 900
tall_hills = df[df['Height'] > 900]

# 2. Count number of hills per Region
region_counts = tall_hills['Region'].value_counts()

# 3. Select top regions
top_regions = region_counts.head()

# 4. Convert results into NumPy arrays
regions_array = np.array(top_regions.index)
counts_array = np.array(top_regions.values)

# 5. Plot bar chart
plt.figure()
plt.bar(regions_array, counts_array)

# 6. Add labels and title
plt.title("Number of Tall Hills (>900m) per Region")
plt.xlabel("Region")
plt.ylabel("Count")

# Rotate x-axis labels
plt.xticks(rotation=0)
plt.tight_layout()

# Save the graph
plt.savefig("C:/Users/DELL/OneDrive/Desktop/python tasks/Analytics/project3/scottish_hills.csv.png")

# Show plot
plt.show()

'''
=================================================================================================================================
 🟡 SCENARIO 4: Pie Chart (Region Distribution) + Save
=================================================================================================================================
�� Tasks:
1. Count the number of hills per Region.
2. Select top 5 regions using Pandas.
3. Prepare labels and values.
4. Plot a pie chart:
5. Add percentage labels (autopct).
Save the graph: plt.savefig("region_distribution.png")
'''
# 1. Count hills per Region
region_counts = df["Region"].value_counts()

# 2. Select top 5 regions
top_regions = region_counts.head(5)

# 3. Prepare labels and values
labels = top_regions.index
values = top_regions.values

# 4. Plot pie chart
plt.figure(figsize=(10, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)

# 5. Title
plt.title("Distribution of Hills by Region")
plt.tight_layout()

# Save graph
plt.savefig("C:/Users/DELL/OneDrive/Desktop/python tasks/Analytics/project3/scottish_hills.csv.png")

# Show plot
plt.show()
'''
=================================================================================================================================
 🔴 SCENARIO 5: Advanced Analysis + Multiple Graphs
=================================================================================================================================
�� Part 1: Feature Creation
1. Create a new column:
○ Height Category:
■ Height >= 1000 → "Very High"
■ 800–999 → "High"
■ < 800 → "Moderate"
�� Part 2: NumPy Usage
2. Convert Height column to NumPy array.
Calculate height differences using:
np.diff()
�� Part 3: Visualizations
�� Line Graph
4. Plot height trend for all hills.
�� Stacked Bar Chart
5. Show count of Height Category per Region.
�� Histogram
6. Plot distribution of Height.
�� Part 4: Save All Graphs
plt.savefig("height_trend.png")
plt.savefig("height_category_stacked.png")
plt.savefig("height_histogram.png")
�� Part 5: Insights
● Which region has tallest hills
● Which category is most common
● Distribution pattern of heights

'''

# ------------------------------
# PART 1: FEATURE CREATION
# ------------------------------
def height_category(h):
    if h >= 1000:
        return "Very High"
    elif h >= 800:
        return "High"
    else:
        return "Moderate"

df["Height_Category"] = df["Height"].apply(height_category)

# ------------------------------
# PART 2: NUMPY USAGE
# ------------------------------
height_array = np.array(df["Height"])

# Calculate differences
height_diff = np.diff(height_array)

print("\nFirst 10 Height Differences:")
print(height_diff[:10])

# ------------------------------
# PART 3: VISUALIZATIONS
# ------------------------------

# 🔹 1. Line Graph (Height Trend)
plt.figure()
plt.plot(range(len(height_array)), height_array)
plt.title("Height Trend of All Hills")
plt.xlabel("Index")
plt.ylabel("Height")
plt.tight_layout()
plt.savefig("C:/Users/DELL/OneDrive/Desktop/python tasks/Analytics/project3/scottish_hills.csv.png")
plt.show()


# 🔹 2. Stacked Bar Chart (Category per Region)
category_region = pd.crosstab(df["Region"], df["Height_Category"])

category_region.plot(kind="bar", stacked=True)
plt.title("Height Category Distribution per Region")
plt.xlabel("Region")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("C:/Users/DELL/OneDrive/Desktop/python tasks/Analytics/project3/scottish_hills.csv.png")
plt.show()


# 🔹 3. Histogram (Height Distribution)
plt.figure()
plt.hist(df["Height"], bins=10, edgecolor = 'black')
plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("C:/Users/DELL/OneDrive/Desktop/python tasks/Analytics/project3/scottish_hills.csv.png")
plt.show()


# ------------------------------
# PART 4: INSIGHTS
# ------------------------------

# Tallest region
tallest_region = df.groupby("Region")["Height"].mean().idxmax()

# Most common category
common_category = df["Height_Category"].value_counts().idxmax()

print("\nInsights We have Got are:")
print("Tallest Region (avg height):", tallest_region)
print("Most Common Height Category:", common_category)
'''
================================================================================================================
-----------------------------------------------------THE END----------------------------------------------------
================================================================================================================
'''
