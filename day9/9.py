class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand


class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, brand, model):
        super().__init__(name, price, brand)
        self.model = model

    def display(self):   
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("----------------------")


phone1 = MobilePhone("iPhone", 80000, "Apple", "iPhone 14")

phone1.display()  
