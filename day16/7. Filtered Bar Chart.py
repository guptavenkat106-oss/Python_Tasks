import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

names = ["A", "B", "C", "D", "E"]
marks = np.array([45, 80, 60, 30, 90])

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

filtered_df = df[df["Marks"] > 50]

plt.bar(filtered_df["Name"], filtered_df["Marks"])

plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.title("Students with Marks > 50")

plt.show()
