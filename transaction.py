from datetime import datetime

class Transaction:
    def __init__(self, ttype, amount, balance_after, note=""):
        self.timestamp = datetime.now()
        self.type = ttype  # refers to transaction type what type of transaction you want to do such as DEPOSIT or WITHDRAWAL
        self.amount = amount
        self.balance_after = balance_after
        self.note = note

    def __str__(self):
        return f"{self.timestamp} | {self.type} | Amount: £{self.amount:.2f} | Balance: £{self.balance_after:.2f} | {self.note}"


# #  checking the ouput
# t=Transaction("DEPOSIT", 100.0, 150.0, "Initial deposit")
# print(t)