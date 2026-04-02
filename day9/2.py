class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area of Retangle:", area)
        print("----------------------")

rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 4)

rect1.calculate_area()
rect2.calculate_area()
        
