from bank import Bank


def main():
    bank = Bank()
    
    while True:
        print("\n--- Bank Menu ---")
        print("1.  Create Account")
        print("2. Show Accounts")
        print("3.  Open Account")
        print("4.  Exit")
        choice = input("Choose: ").strip()
        
        if choice == "1":
            name = input("Name: ")
            number = input("Account number: ")
            acc_type = input("Type (savings/checking): ").lower() or "savings"
            try:
                balance = float(input("Balance: £"))
            except:
                print("Invalid amount.")
                continue
            bank.create(name, number, acc_type, balance)
            
        elif choice == "2":
            bank.list_all()
            
        elif choice == "3":
            number = input("Account number: ")
            acc = bank.get(number)
            if not acc:
                print("Not found.")
                continue
            while True:
                print(f"\n--- {acc.get_number()} ({acc.get_type()}) ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Balance")
                print("4.  Transactions")
                print("5. Back")
                sub = input("Choose: ")
                
                if sub == "1":
                    try:
                        amt = float(input("Amount: $"))
                        acc.deposit(amt)
                        bank.save()
                    except:
                        print("Invalid amount.")
                elif sub == "2":
                    try:
                        amt = float(input("Amount: $"))
                        acc.withdraw(amt)
                        bank.save()
                    except:
                        print("Invalid amount.")
                elif sub == "3":
                    print(f"Balance: £{acc.get_balance()}")
                elif sub == "4":
                    acc.show_all_transactions()
                elif sub == "5":
                    break
                    
        elif choice == "4":
            print("Bye!")
            break


if __name__ == "__main__":
    main()