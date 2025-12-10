import json
import os
from savings_account import SavingsAccount
from checking_account import CheckingAccount

_DATA_FILE = "accounts.json"


class Bank:

    def __init__(self):
        self.__accounts = {}
        self.load()

    def load(self):
        if not os.path.exists(_DATA_FILE):
            return

        with open(_DATA_FILE, "r") as f:
            data = json.load(f)

        for acc in data:
            if acc["type"] == "checking":
                obj = CheckingAccount(acc["name"], acc["acc_number"], acc["balance"])
            else:
                obj = SavingsAccount(acc["name"], acc["acc_number"], acc["balance"])

            self.__accounts[acc["acc_number"]] = obj

    def save(self):
        data = [acc.to_dict() for acc in self.__accounts.values()]
        with open(_DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def create(self, name: str, acc_number: str, acc_type: str, balance: float):
        if acc_number in self.__accounts:
            print("Account already exists.")
            return

        acc = (
            CheckingAccount(name, acc_number, balance)
            if acc_type == "checking"
            else SavingsAccount(name, acc_number, balance)
        )

        self.__accounts[acc_number] = acc
        self.save()
        print(f"Account {acc_number} created.")

    def get(self, acc_number: str):
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
                f"£{acc.get_balance():.3f}"
            )
