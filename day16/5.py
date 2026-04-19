import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

plt.bar(df["Product"], df["Sales"])

plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales Bar Chart")

plt.show()
