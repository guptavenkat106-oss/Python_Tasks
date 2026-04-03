class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)  
        self.file_size = file_size

    def display(self):
        super().display()
        print("File Size:", self.file_size, "MB")


book1 = Book("Python Basics", "John Doe", 300)
ebook1 = EBook("Learn Python", "Jane Smith", 200, 5)


print("Book Details:")
book1.display()

print("\nEBook Details:")
ebook1.display()
