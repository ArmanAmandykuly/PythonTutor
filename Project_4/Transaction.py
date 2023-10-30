from TypeChecker import *
from Product import *
class Transaction:
    def __init__(self, transaction_id, product, transaction_type, amount, date, history):
        self.transaction_id = TypeChecker.integer(transaction_id)
        self.product = TypeChecker.isTypeEq(product, Product)
        self.transaction_type = TypeChecker.nonEmpty(transaction_type)
        self.amount = TypeChecker.nonNegative(amount)
        self.date = TypeChecker.nonEmpty(date)
        self.history = TypeChecker.isTypeEq(TypeChecker.nonNull(history), list)
    
    def execute(self):
        try:
            if self.transaction_type == "restock":
                self.product.quantity += self.amount
            elif self.transaction_type == "sell":
                self.product.quantity = TypeChecker.nonNegative(self.product.quantity - self.amount)
        except RuntimeError:
            raise RuntimeError("Not enough stock")