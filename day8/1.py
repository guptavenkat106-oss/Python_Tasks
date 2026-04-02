def add_attendance(name):
    with open("attendance.txt", "a") as file:
        file.write(name + "\n")

def display_attendance():
    try:
        with open("attendance.txt", "r") as file:
            print("\nAttendance रिकॉर्ड:")
            print(file.read())
    except FileNotFoundError:
        print("No attendance records found.")

student_name = input("Enter student name: ")
add_attendance(student_name)
display_attendance()
