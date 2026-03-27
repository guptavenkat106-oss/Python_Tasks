students={
    "nithin":76,
    "pradeep":90,
    "siva":65
    }
top_student=max(students,key=students.get)
highest_marks=students[top_student]
print("top student:",top_student)
print("highest marks:",highest_marks)
