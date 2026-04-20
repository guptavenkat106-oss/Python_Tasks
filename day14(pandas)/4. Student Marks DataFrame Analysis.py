import pandas as pd

data = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Math": [80, 70, 60],
    "Science": [90, 60, 70]
})

data["Total"] = data["Math"] + data["Science"]

top_student = data.loc[data["Total"].idxmax()]

print(data)
print("\nTop student:")
print(top_student)
