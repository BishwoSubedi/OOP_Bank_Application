from account import Account

class CheckingAccount(Account):

    def __init__(self, name: str, number: str, balance: float = 0.0, fee: float = 1.0):
        super().__init__(name, number, balance)
        self.__fee = fee  # private fee

    def deposit(self, amount: float):
        if amount <= 0:
            print("Invalid deposit amount.")
            return False

        new_balance = self.get_balance() + amount
        self._update_balance(new_balance)
        self.save_transaction("Deposit", amount)
        print(f"Deposited £{amount:.3f} | Balance £{self.get_balance():.3f}")
        return True

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return False

        total = amount + self.__fee
        if total > self.get_balance():
            print("Insufficient funds.")
            return False

        new_balance = self.get_balance() - total
        self._update_balance(new_balance)
        self.save_transaction("Withdraw", amount)
        print(
            f"Withdrew £{amount:.3f} (Fee £{self.__fee:.3f}) | Balance £{self.get_balance():.3f}"
        )
        return True

    def get_type(self):
        return "checking"
