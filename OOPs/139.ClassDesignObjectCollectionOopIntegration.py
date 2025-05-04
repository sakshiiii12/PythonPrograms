#Design a simple inventory system with a Product class and an Inventory class to manage product stock.
#(Covers: Class Design, Object Collection, OOP Integration)

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_inventory(self):
        for p in self.products:
            print(f"{p.name}: {p.stock} in stock")

inv = Inventory()
inv.add_product(Product("Laptop", 5))
inv.add_product(Product("Mouse", 10))
inv.display_inventory()
