class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"


def save_to_file(employees, filename="employees.txt"):
    try:
        with open(filename, "w") as file:
            for emp in employees.values():
                file.write(f"{emp.emp_id},{emp.name},{emp.salary}\n")
        print("Data saved successfully.\n")
    except IOError:
        print("Error: Unable to write to file.\n")


def main():
    employees = {}

    print("=== Employee Management System ===")

    while True:
        print("\n1. Add Employee")
        print("2. Display All Employees")
        print("3. Save to File")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")

            try:
                salary = float(input("Enter Salary: "))
            except ValueError:
                print("Invalid salary! Please enter a numeric value.")
                continue

            emp = Employee(emp_id, name, salary)
            employees[emp_id] = emp
            print("Employee added successfully.")

        elif choice == "2":
            if not employees:
                print("No employees found.")
            else:
                print("\n--- Employee List ---")
                for emp in employees.values():
                    print(emp.display())

        elif choice == "3":
            save_to_file(employees)

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


main()
