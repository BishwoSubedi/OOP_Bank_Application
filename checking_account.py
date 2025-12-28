from account import Account

class CheckingAccount(Account):
    def __init__(self, name, acc_number, balance=0.0, fee=1.0):
        super().__init__(name, acc_number, balance)
        self.__fee = fee

    def deposit(self, amount: float):
        if amount <= 0:
            return False
        self._update_balance(self.get_balance() + amount)
        self.save_transaction("Deposit", amount)
        return True

    def withdraw(self, amount: float):
        total = amount + self.__fee
        if amount <= 0 or total > self.get_balance():
            return False
        self._update_balance(self.get_balance() - total)
        self.save_transaction("Withdrawal", amount)
        return True

    def get_type(self):
        return "checking"
