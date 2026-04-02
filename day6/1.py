bjects = ("math", "science", "english")

student_names = set()
student_marks = {}

def recursive_total(marks_list):
    if len(marks_list) == 0:
        return 0
    return marks_list[0] + recursive_total(marks_list[1:])


def add_student():
    try:
        name = input("Enter student name: ")

        if name in student_names:
            print("Student already exists!")
            return

        marks = []

        for subject in subjects:
            try:
                mark = float(input(f"Enter marks of {subject}: "))
                marks.append(mark)
            except ValueError:
                print("Invalid input! Please enter numeric marks.")
                return

        student_names.add(name)
        student_marks[name] = marks

    except Exception as e:
        print("Error:", e)


def display_students():
    if not student_marks:
        print("No records found.")
        return

    for name, marks in student_marks.items():
        print(f"{name} : {marks}")


def calculate_average():
    try:
        name = input("Enter student name to calculate average: ")

        if name not in student_marks:
            raise NameError

        marks = student_marks[name]

        if not isinstance(marks, list):
            raise TypeError

        total = recursive_total(marks)
        print("Total marks:", total)

        try:
            average = total / len(marks)
            print("Average marks:", average)
        except ZeroDivisionError:
            print("Cannot divide by zero.")

    except NameError:
        print("Student name not found.")
    except TypeError:
        print("Marks data type error")
    except Exception as e:
        print("Error:", e)


def main():
    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Calculate Average")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            calculate_average()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


main()
