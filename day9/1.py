class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks   # fixed here

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print("----------------------")


student1 = Student("Venkat", 1, 84)
student2 = Student("Srikanth", 2, 77)
student3 = Student("Akhil", 3, 90)

student1.display()
student2.display()
student3.display()
