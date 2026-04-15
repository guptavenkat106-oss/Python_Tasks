import numpy as np
import pandas as pd

# Given data
arr = np.array([
    [80, 90],
    [70, 60],
    [85, 95]
])

df = pd.DataFrame(arr, columns=["Math", "Science"])

df["Total"] = df["Math"] + df["Science"]

top_student = df[df["Total"] == df["Total"].max()]

print(df)
print("\nTop Student:")
print(top_student)
