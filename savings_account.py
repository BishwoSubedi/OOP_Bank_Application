from account import Account


class SavingsAccount(Account):
    # inheritance
    def deposit(self, amount: float):
        if amount <= 0:
            print("Invalid amount.")
            return False
        self._balance += amount
        self.save_transaction("Deposit", amount)
        print(f"Deposited £{amount}.  Balance: £{self._balance}")
        return True

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Invalid amount.")
            return False
        if amount > self._balance:
            print("No money.")
            return False
        self._balance -= amount
        self.save_transaction("Withdraw", amount)
        print(f"Withdrew £{amount}. Balance: £{self._balance}")
        return True

    def get_type(self):
        return "savings"