import json
import os
from savings_account import SavingsAccount
from checking_account import CheckingAccount

_DATA_FILE = "accounts.json"


class Bank:
    
    def __init__(self):
        self.__accounts = {}  # private dictionary to hold accounts
        self.load()  # load existing accounts from file

    def load(self):
        if not os.path.exists(_DATA_FILE):
            return
        with open(_DATA_FILE, "r") as f:
            data = json.load(f)  # converting JSON data to Python object
        for acc in data:
            if acc["type"] == "checking":
                obj = CheckingAccount(acc["name"], acc["acc_number"], acc["balance"])
            else:
                obj = SavingsAccount(acc["name"], acc["acc_number"], acc["balance"])
            self.__accounts[acc["acc_number"]] = obj

    def save(self):
        data = [acc.to_dict() for acc in self.__accounts.values()]  # convert objects to dicts
        with open(_DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)  # save as JSON

    def create(self, name: str, acc_number: str, acc_type: str, balance: float = 0.0):
        """Create new account"""
        if acc_number in self.__accounts:
            print("Account already exists.")
            return
        if acc_type == "checking":
            acc = CheckingAccount(name, acc_number, balance)
        else:
            acc = SavingsAccount(name, acc_number, balance)
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
            print(f"{acc.get_number()} | {acc.get_name()} | {acc.get_type()} | £{acc.get_balance():.2f}")
