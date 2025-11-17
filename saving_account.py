from bank_account import Account

class SavingsAccount(Account):
    def __init__(self, name, account_number, balance=0,interest_rate=0.02):
        super().__init__(name, account_number, balance)
        self.interest_rate=interest_rate
    
    def apply_interest(self):
        interest=self.get_balance*self.interest_rate/12
        if interest>0:
            self.deposit(interest)  
