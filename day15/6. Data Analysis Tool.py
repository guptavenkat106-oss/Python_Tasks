import numpy as np
import pandas as pd

def data_analysis():
    print("=== Student Marks Analysis ===")

    marks = np.random.randint(0, 101, 10)

    students = [f"Student_{i+1}" for i in range(10)]

    df = pd.DataFrame({
        "Name": students,
        "Marks": marks
    })

    print("\n--- All Students ---")
    print(df)

    passing = df[df["Marks"] >= 40]

    print("\n--- Passing Students ---")
    print(passing)

    mean_marks = np.mean(df["Marks"])
    print(f"\nAverage Marks: {mean_marks:.2f}")

    print("\n--- Individual Results ---")
    for index, row in df.iterrows():
        status = "Pass" if row["Marks"] >= 40 else "Fail"
        print(f"{row['Name']} -> {row['Marks']} ({status})")


data_analysis()
