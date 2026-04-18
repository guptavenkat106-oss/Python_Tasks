import random
import numpy as np
import pandas as pd
import math

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = self.assign_grade()

    def assign_grade(self):
        # Assign grade using conditions
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        elif self.marks >= 40:
            return 'D'
        else:
            return 'F'

def simulate_results(num_students=10):
    try:
        students = []
        marks_list = []

        # Generate random marks using loop
        for i in range(num_students):
            name = f"Student_{i+1}"
            marks = random.randint(0, 100)
            student = Student(name, marks)

            students.append(student)
            marks_list.append(marks)

        marks_array = np.array(marks_list)

        # Math module statistics
        mean_marks = math.fsum(marks_list) / len(marks_list)
        max_marks = max(marks_list)
        min_marks = min(marks_list)

        data = {
            "Name": [s.name for s in students],
            "Marks": [s.marks for s in students],
            "Grade": [s.grade for s in students]
        }

        df = pd.DataFrame(data)

        # Save report to file
        df.to_csv("exam_report.csv", index=False)

        # Print results
        print("Student Results:\n")
        print(df)

        print("\nStatistics:")
        print(f"Mean Marks: {mean_marks:.2f}")
        print(f"Max Marks: {max_marks}")
        print(f"Min Marks: {min_marks}")

        print("\nReport saved as 'exam_report.csv'")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    simulate_results(10)