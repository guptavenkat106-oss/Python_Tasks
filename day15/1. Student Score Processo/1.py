import math

students = [
    ("karthik", 78),
    ("nag", 45),
    ("phani", 62),
    ("satya", 39),
    ("anand", 55)
]

student_dict = dict(students)

passed_students = []
total_marks = 0

for name, marks in student_dict.items():
    total_marks += marks
    if marks > 50:
        passed_students.append(name)

average = total_marks / len(student_dict)
average = math.floor(average) 

with open("results.txt", "w") as file:
    file.write("Student Scores:\n")
    for name, marks in student_dict.items():
        file.write(f"{name}: {marks}\n")
    
    file.write("\nStudents scoring above 50:\n")
    for name in passed_students:
        file.write(name + "\n")
    
    file.write(f"\nAverage Score: {average}")

print("Processing complete. Results saved to results.txt")
