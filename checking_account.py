from account import Account

class CheckingAccount(Account):
#  implementing inheritance
    def __init__(self, name, acc_number, balance=0.0, fee=1.0):
        super().__init__(name, acc_number, balance)
        self.__fee = fee
    #  implementation of polymorphism
    def deposit(self, amount: float):
        if amount <= 0:
            print("Invalid deposit amount")
            return False

        self._update_balance(self.get_balance() + amount)
        self.save_transaction("Deposit", amount)
        print(f"Deposited £{amount:.2f} | Balance £{self.get_balance():.2f}")
        return True
     
    def withdraw(self, amount: float):
        total = amount + self.__fee

        if amount <= 0:
            print("Invalid withdrawal amount")
            return False

        if total > self.get_balance():
            print("Insufficient funds")
            return False

        self._update_balance(self.get_balance() - total)
        self.save_transaction("Withdrawal", amount)
        print(
            f"Withdrew £{amount:.2f} (Fee £{self.__fee:.2f}) "
            f"| Balance £{self.get_balance():.2f}"
        )
        return True

    def get_type(self):
        return "checking"
