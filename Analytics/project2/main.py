import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Scenario 1: Data Loading & Preprocessing
# 1. Load the dataset
df = pd.read_csv('ign.csv')

# 2. Display Head, Tail, Shape
print("--- First 5 rows ---")
print(df.head())
print("\n--- Last 5 rows ---")
print(df.tail())
print("\n--- Shape ---")
print(df.shape)

# 3. Remove unnecessary column
if 'Unnamed: 0' in df.columns:
    df.drop(columns=['Unnamed: 0'], inplace=True)

# 4. Check missing values
print("\n--- Missing values before handling ---")
print(df[['score', 'genre', 'platform']].isnull().sum())

# 5. Handle missing values
df['score'] = df['score'].fillna(df['score'].mean())
df['genre'] = df['genre'].fillna(df['genre'].mode()[0])

# 6. Ensure correct data types
df['score'] = df['score'].astype(float)
df['release_year'] = df['release_year'].astype(int)
df['release_month'] = df['release_month'].astype(int)
df['release_day'] = df['release_day'].astype(int)

print("\n--- Data Types After Cleaning ---")
print(df.dtypes)

# Scenario 2: Line Graph (Score Trend)
yearly_avg = df.groupby('release_year')['score'].mean()
years = yearly_avg.index.to_numpy()
avg_scores = yearly_avg.values

plt.plot(years, avg_scores, marker='o')
plt.title("Average Game Score Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.grid(True)
plt.savefig("avg_score_trend.png")
plt.close()

# Scenario 3: Filtering + Bar Chart
high_rated = df[df['score'] > 7]
platform_counts = high_rated['platform'].value_counts().head(10)
platforms = platform_counts.index.to_numpy()
counts = platform_counts.values

plt.bar(platforms, counts)
plt.title("Top 10 Platforms with Games Scored > 7")
plt.xlabel("Platform")
plt.ylabel("Count of Games")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_platforms_bar.png")
plt.close()

# Scenario 4: Aggregation + Pie Chart
genre_counts = df['genre'].value_counts().head(5)
genres = genre_counts.index.to_numpy()
genre_values = genre_counts.values

plt.pie(genre_values, labels=genres, autopct='%1.1f%%', startangle=140)
plt.title("Top 5 Genres Distribution")
plt.axis('equal')
plt.savefig("genre_distribution.png")
plt.close()

# Scenario 5: Advanced Analysis
# Part 1: Feature Engineering
def categorize_score(score):
    if score >= 9: return "Excellent"
    elif score >= 7: return "Good"
    else: return "Average"

df['score_category'] = df['score'].apply(categorize_score)
df['editors_choice_numeric'] = df['editors_choice'].map({'Y': 1, 'N': 0})

# Part 2: NumPy Analysis
# Calculate yearly score growth
yearly_growth = np.diff(avg_scores)
print("\n--- Yearly Score Growth ---")
print(yearly_growth)

# Part 3: Visualizations
# 4. Line Graph (Average score per release_year) - Already saved as avg_score_trend.png in Scen 2? 
# The prompt asks for score_trend.png in Scen 5, let's reuse/redo.
plt.plot(years, avg_scores, color='blue', marker='s')
plt.title("Trend of Average Score per Year")
plt.xlabel("Year")
plt.ylabel("Avg Score")
plt.savefig("score_trend.png")
plt.close()

# 5. Stacked Bar Chart: score_category per release_year
category_pivot = df.groupby(['release_year', 'score_category']).size().unstack(fill_value=0)
category_pivot.plot(kind='bar', stacked=True)
plt.title("Score Category Distribution per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.legend(title="Category")
plt.savefig("score_category_stacked.png")
plt.close()

# 6. Histogram: distribution of score
plt.hist(df['score'], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Game Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("score_distribution.png")
plt.close()

# Part 5: Insights
correlation = df['editors_choice_numeric'].corr(df['score'])
max_score_year = yearly_avg.idxmax()
print(f"\n--- Insights ---")
print(f"Year with highest average score: {max_score_year}")
print(f"Correlation between Editor's Choice and Score: {correlation:.4f}")