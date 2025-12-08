from account import Account


class SavingsAccount(Account):
    def deposit(self, amount:float):
        if amount<=0:
            print("Invalid deposit amount")
            return False
        new_balance=self.get_balance()+amount
        self._update_balance(new_balance)
        self.save_transaction("Deposit", amount)
        print(f"Deposited £{amount:.2f} | Balance: £{self.get_balance():.2f}")
        
    def withdraw(self, amount:float):
        if amount<=0:
            print("Invalid withdrawal amount")
            return False
        if amount>self.get_balance():
            print("Insufficient funds")
            return False
        new_balance=self.get_balance()-amount
        self._update_balance(new_balance)
        self.save_transaction("Withdrawal", amount)
        print(f"Withdrew £{amount:.2f} | Balance: £{self.get_balance():.2f}")
        return True
    
    def get_type(self):
        return "Savings"