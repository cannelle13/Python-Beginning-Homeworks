class Product:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):
    def __init__(self, name: str, price: int, quantity: int, author: str):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}₴")
        print(f"Quantity: {self.quantity}")


book = Book("Depeche Mode", 299, 25, "Serhiy Zhadan")

book.read()
