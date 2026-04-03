def add_bonus(func):
    def wrapper(self):
        bonus = 0.10 * self.salary   
        self.salary += bonus
        func(self)
    return wrapper


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @add_bonus
    def display_salary(self):
        print("Employee Name:", self.name)
        print("Salary after bonus:", self.salary)


emp1 = Employee("Ravi", 50000)

emp1.display_salary()
