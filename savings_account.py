from account import Account

class SavingsAccount(Account):

    def deposit(self, amount: float):
        if amount <= 0:
            return False
        self._update_balance(self.get_balance() + amount)
        self.save_transaction("Deposit", amount)
        return True

    def withdraw(self, amount: float):
        if amount <= 0 or amount > self.get_balance():
            return False
        self._update_balance(self.get_balance() - amount)
        self.save_transaction("Withdrawal", amount)
        return True

    def get_type(self):
        return "savings"
