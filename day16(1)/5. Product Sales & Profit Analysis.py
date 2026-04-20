import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})

print(df)

plt.figure(figsize=(12, 10))

# 1. Line Graph - Sales Trend
plt.subplot(2, 3, 1)
plt.plot(df["Product"], df["Sales"], marker='o', color='blue')
plt.title("Sales Trend")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid()

# 2. Bar Chart - Product vs Sales
plt.subplot(2, 3, 2)
plt.bar(df["Product"], df["Sales"], color="orange")
plt.title("Product vs Sales")

# 3. Pie Chart - Sales Contribution
plt.subplot(2, 3, 3)
plt.pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")
plt.title("Sales Contribution")

# 4. Histogram - Profit Distribution
plt.subplot(2, 3, 4)
plt.hist(df["Profit"], bins=5, color="green", edgecolor="black")
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

# 5. Scatter Plot - Sales vs Profit
plt.subplot(2, 3, 5)
plt.scatter(df["Sales"], df["Profit"], color="red")
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid()

plt.tight_layout()
plt.show()
