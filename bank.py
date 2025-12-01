import json
import os
from savings_account import SavingsAccount
from checking_account import CheckingAccount

DATA_FILE = "accounts.json"


class Bank:
    
    def __init__(self):
        self.accounts = {}
        self.load()

    def load(self):
        """Load accounts from file"""
        if not os.path.exists(DATA_FILE):
            return
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        for acc in data:
            if acc["type"] == "checking":
                obj = CheckingAccount(acc["name"], acc["number"], acc["balance"])
            else:
                obj = SavingsAccount(acc["name"], acc["number"], acc["balance"])
            self.accounts[acc["number"]] = obj

    def save(self):
        """Save accounts to file"""
        data = [acc.to_dict() for acc in self.accounts.values()]
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def create(self, name: str, number: str, acc_type: str = "savings", balance: float = 0.0):
        """Create new account"""
        if number in self.accounts:
            print("Account exists.")
            return
        if acc_type == "checking":
            acc = CheckingAccount(name, number, balance)
        else:
            acc = SavingsAccount(name, number, balance)
        self.accounts[number] = acc
        self.save()
        print(f"Account {number} created.")

    def get(self, number: str):
        return self.accounts.get(number)

# showing all accounts
    def list_all(self):

        if not self.accounts:
            print("No accounts.")
            return
        for acc in self.accounts.values():
            print(f"{acc. get_number()} | {acc.get_name()} | {acc.get_type()} | ${acc.get_balance()}")