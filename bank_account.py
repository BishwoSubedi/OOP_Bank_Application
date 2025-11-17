from transaction import Transaction
class Account:
    def __init__(self,name,account_number,balance=0):
     self.__name=name
     self.__account_number=account_number
     self.__balance=balance
     self.__transactions=[]
     
     if  balance>0:
         self.__transactions.append(Transaction("Deposit",balance,balance,"Initial Deposit"))
    
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Deposit amount cannot be less than zero")
        
        self.__balance+=amount
        self.__transactions.append(Transaction("Deposit",amount,self.__balance))
        
    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("Withdrawl must be positive")
        if amount>self.__balance:
            raise ValueError("Insufficient Funds")
        self.__balance-=amount
         
    def get_balance(self):
        return self.__balance
    
    def get_transcations(self):
        return self.__transactions