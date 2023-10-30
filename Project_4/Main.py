from Conductor import *
from Product import *
from TypeChecker import *
class Main:
    def __init__(self):
        self.history = list()
        self.products = list()
        self.conductor = Conductor(self.history)
        self.id_counter = 0
        self.commands = {
            "add" : self.createProduct,
            "pop" : self.popProduct,
            "restock" : self.restock,
            "sell" : self.sell,
            "exit" : exit,
            "show" : self.show
        }

    def restock(self):
        id = int(TypeChecker.isDigit(input("Product id: ")))
        try:
            ind = list(map(lambda x: x.product_id, self.products)).index(id)
            amount = TypeChecker.nonNegative(int(TypeChecker.isDigit(input("Amount: "))))
            self.conductor.restock(self.products[ind], amount)
        except Exception as e:
            print("ERROR:", e)
    
    def sell(self):
        id = int(TypeChecker.isDigit(input("Product id: ")))
        try:
            ind = list(map(lambda x: x.product_id, self.products)).index(id)
            amount = TypeChecker.nonNegative(int(TypeChecker.isDigit(input("Amount: "))))
            self.conductor.sell(self.products[ind], amount)
        except Exception as e:
            print("ERROR: ", e)

    def createProduct(self):
        name = TypeChecker.nonEmpty(input("Name: "))
        price = TypeChecker.nonNegative(int(TypeChecker.isDigit(input("Price: "))))
        quantity = TypeChecker.nonNegative(int(TypeChecker.isDigit(input("Quantity: "))))
        description = input("Description: ")

        try:
            newProduct = Product(self.id_counter, name, price, quantity, description, self.conductor)
            self.products.append(newProduct)
            self.id_counter += 1
        except Exception as e:
            print("ERROR:", e)
    
    def popProduct(self):
        id = int(TypeChecker.isDigit(input("Product id: ")))
        try:
            ind = list(map(lambda x: x.product_id, self.products)).index(id)
            self.products.pop(ind)
        except Exception as e:
            print("ERROR:", e)

    def show(self):
        print("\n".join(map(str, self.products)))

    def run(self):
        while True:
            command = input("Input your command("+ ','.join(self.commands.keys()) +"): ")
            while not command in self.commands:
                command = input("Please, input valid command: ")
            self.commands[command]()

if __name__ == "__main__":
    main = Main()
    main.run()