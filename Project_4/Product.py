from TypeChecker import *
class Product:
    def __init__(self, product_id, name, price, quantity, description, conductor):
        self.product_id = TypeChecker.integer(product_id)
        self.name = TypeChecker.nonEmpty(name)
        self.price = TypeChecker.nonNegative(price)
        self.quantity = quantity
        self.description = description
        self.conductor = conductor

    def restock(self, amount):
        self.conductor.restock(self, amount)

    def sell(self, amount):
        self.conductor.sell(self, amount)

    def get_details(self, isStr = False):
        if isStr:
            return "Product id: " + str(self.product_id) + "\nName: " + self.name + "\nPrice: " + str(self.price) + "\nQuantity: " + str(self.quantity)
        else:
            print(self.get_details())

    def __str__(self):
        return self.get_details(True)