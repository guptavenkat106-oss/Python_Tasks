import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print(df)

plt.figure(figsize=(6,4))
plt.plot(df["Student"], df["Marks"], marker='o')
plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()
plt.show()

plt.figure(figsize=(6,4))
plt.bar(df["Student"], df["Marks"], color="skyblue")
plt.title("Student vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

pass_fail = df["Marks"] > 50
labels = ["Pass", "Fail"]
values = [pass_fail.sum(), (~pass_fail).sum()]

plt.figure(figsize=(5,5))
plt.pie(values, labels=labels, autopct="%1.1f%%", colors=["green", "red"])
plt.title("Pass vs Fail Distribution")
plt.show()

plt.figure(figsize=(6,4))
plt.hist(df["Marks"], bins=5, color="orange", edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(df.index, df["Marks"], color="purple")
plt.title("Index vs Marks")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.grid()
plt.show()
