from bank_account import Account

class CheckingAccount(Account):
    def __init__(self, name, account_number, balance=0, fee=0):
        super().__init__(name, account_number, balance)
        self._fee = fee

    def withdraw(self, amount):
        total = amount + self._fee
        if total > self.get_balance():
            raise ValueError("Insufficient funds including fee")
        super().withdraw(amount)
        if self._fee > 0:
            super().withdraw(self._fee)
