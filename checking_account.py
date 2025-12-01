from account import Account


class CheckingAccount(Account):
    # implementing inheritance from Account
    def __init__(self, name: str, number: str, balance: float = 0.0, fee: float = 1.0):
        super().__init__(name, number, balance)
        self. fee = fee

    def deposit(self, amount: float):
        if amount <= 0:
            print("Invalid amount.")
            return False
        self._balance += amount
        self.save_transaction("Deposit", amount)
        print(f"Deposited £{amount}. Balance: £{self._balance}")
        return True

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Invalid amount.")
            return False
        total = amount + self.fee
        if total > self._balance:
            print("Not enough money.")
            return False
        self._balance -= total
        self.save_transaction("Withdraw", amount)
        print(f"Withdrew £{amount} (fee £{self.fee}). Balance: £{self._balance}")
        return True

    def get_type(self):
        return "checking"