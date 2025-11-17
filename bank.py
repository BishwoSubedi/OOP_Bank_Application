from saving_account import SavingsAccount
from checking_account import CheckingAccount

class Bank:
    def __init__(self):
        self.accounts = {}  #  Account object

    def create_account(self, name, acc_type="savings", balance=0, **kwargs):
        acc_no = f"AC{len(self.accounts)+1:06}"
        if acc_type.lower() == "savings":
            acc = SavingsAccount(name, acc_no, balance, kwargs.get("interest_rate", 0.02))
        else:
            acc = CheckingAccount(name, acc_no, balance, kwargs.get("fee", 0))
        self.accounts[acc_no] = acc
        return acc_no

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if not sender or not receiver:
            raise ValueError("One or both accounts not found")
        sender.withdraw(amount)
        receiver.deposit(amount)
