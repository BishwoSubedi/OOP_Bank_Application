from abc import ABC, abstractmethod
import os
from datetime import datetime

TX_DIR = "transactions"
os.makedirs(TX_DIR, exist_ok=True)

class Account(ABC): #using inbuilt abstraction class in python
    def __init__(self, name: str, acc_number: int, balance: float = 0.0):
        # creating private variables to hide internal detail (Implementation of Encapsulation)
        self.__name = name
        self.__acc_number = acc_number
        self.__balance = balance

    # -------- Getters --------
    def get_name(self):
        return self.__name

    def get_acc_number(self):
        return self.__acc_number

    def get_balance(self):
        return self.__balance

    # -------- Transactions --------
    def __save_transaction(self, transaction_type: str, amount: float):
        filename = os.path.join(TX_DIR, f"tx_{self.__acc_number}.txt")
        with open(filename, "a") as f:
            f.write(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
                f"{transaction_type} | £{amount:.3f}\n"
            )

    def save_transaction(self, transaction_type: str, amount: float):
        self.__save_transaction(transaction_type, amount)

    def show_all_transactions(self):
        filename = os.path.join(TX_DIR, f"tx_{self.__acc_number}.txt")
        if os.path.exists(filename):
            with open(filename, "r") as f:
                print("\n--- Transactions ---")
                print(f.read())
        else:
            print("No transactions found.")

    # -------- Abstract methods --------
    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def get_type(self):
        pass

    def _update_balance(self, amount: float):
        self.__balance = amount
