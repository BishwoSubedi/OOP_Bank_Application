from savings_account import SavingsAccount
from checking_account import CheckingAccount

class Bank:

    def __init__(self):
        self.__accounts = {}  

    def create(self, name, acc_number, acc_type, balance):
        if acc_number in self.__accounts:
            print("Account already exists.")
            return

        if acc_type == "checking":
            acc = CheckingAccount(name, acc_number, balance)
        else:
            acc = SavingsAccount(name, acc_number, balance)

        self.__accounts[acc_number] = acc
        print(f"Account {acc_number} created.")

    def get(self, acc_number):
        return self.__accounts.get(acc_number)

    def list_all(self):
        if not self.__accounts:
            print("No accounts.")
            return

        print("\n--- All Accounts ---")
        for acc in self.__accounts.values():
            print(
                f"{acc.get_acc_number()} | "
                f"{acc.get_name()} | "
                f"{acc.get_type()} | "
                f"£{acc.get_balance():.2f}"
            )
