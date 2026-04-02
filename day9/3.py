class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)
        print("----------------------")

manager1 = Manager("Sneha", 60000)
manager2 = Manager("rajitha", 75000)

manager1.display()
manager2.display()
        
