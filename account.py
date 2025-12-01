from abc import ABC, abstractmethod
import os
from datetime import datetime

TX_DIR = "transactions"
os.makedirs(TX_DIR, exist_ok=True)


class Account(ABC):
    """Base account class - ABSTRACTION"""
    
    def __init__(self, name: str, number: str, balance: float = 0.0):
        # hide sensitive data
        self._name = name
        self._number = number
        self._balance = balance

    def get_balance(self):
        return self._balance

    def get_number(self):
        return self._number

    def get_name(self):
        return self._name

    def save_transaction(self, kind: str, amount: float):
        """Save transaction to file"""
        fname = os.path.join(TX_DIR, f"tx_{self._number}. txt")
        with open(fname, "a") as f:
            f.write(f"{datetime.now(). strftime('%Y-%m-%d %H:%M:%S')} | {kind} | £{amount}\n")

    def show_all_transactions(self):
        """Show all transactions"""
        fname = os.path. join(TX_DIR, f"tx_{self._number}.txt")
        if os.path.exists(fname):
            with open(fname, "r") as f:
                print(f. read())
        else:
            print("No transactions yet.")

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def get_type(self):
        pass

    def to_dict(self):
        return {"name": self._name, "number": self._number, "balance": self._balance, "type": self.get_type()}