from datetime import datetime
from Transaction import *
class Conductor:
    def __init__(self, history):
        self.history = history
        self.transaction_id = 0

    def restock(self, product, amount):
        transaction = Transaction(self.transaction_id, product, "restock", amount, str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")), self.history)
        try:
            transaction.execute()
            self.transaction_id += 1
            self.history.append(transaction)
        except Exception as e:
            print("ERROR:", str(e))

    def sell(self, product, amount):
        transaction = Transaction(self.transaction_id, product, "sell", amount, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), self.history)
        try:
            transaction.execute()
            self.transaction_id += 1
            self.history.append(transaction)
        except Exception as e:
            print("ERROR:", e)