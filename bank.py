from account import Account
from savings_account import SavingsAccount
from checking_account import CheckingAccount

class Bank(Account):
    def __init__(self, name="Bank", acc_number=0, balance=0.0):
        super().__init__(name, acc_number, balance)
        self.__accounts = {}  # holds customer accounts

    # -------- Abstract method implementations --------
    def deposit(self, amount: float):
        if amount <= 0:
            return False
        self._update_balance(self.get_balance() + amount)
        self.save_transaction("Bank Deposit", amount)
        return True

    def withdraw(self, amount: float):
        if amount <= 0 or amount > self.get_balance():
            return False
        self._update_balance(self.get_balance() - amount)
        self.save_transaction("Bank Withdrawal", amount)
        return True

    def get_type(self):
        return "Bank"

    # -------- Bank-specific methods --------
    def create(self, name: str, acc_number: str, acc_type: str, balance: float):
        if acc_number in self.__accounts:
            print("Account already exists.")
            return

        if acc_type == "checking":
            acc = CheckingAccount(name, acc_number, balance)
        else:
            acc = SavingsAccount(name, acc_number, balance)

        self.__accounts[acc_number] = acc
        print(f"Account {acc_number} created successfully.")

    def get(self, acc_number: str):
        return self.__accounts.get(acc_number)

    def list_all(self):
        if not self.__accounts:
            print("No accounts found.")
            return

        print("\n--- All Accounts ---")
        for acc in self.__accounts.values():
            print(
                f"{acc.get_acc_number()} | "
                f"{acc.get_name()} | "
                f"{acc.get_type()} | "
                f"£{acc.get_balance():.3f}"
            )

 
    def save(self):
        pass
