from bank import Bank
from storage import save, load

def main():
    bank = load()
    if not bank:
        bank = Bank()

    while True:
        print("\n--- Welcome to Simple Bank ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Balance")
        print("6. View Transactions")
        print("7. Apply Interest (Savings)")
        print("8. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                name = input("Enter holder name: ")
                acc_type = input("Enter account type (savings/checking): ").lower()
                balance = float(input("Enter initial balance: "))
                if acc_type == "savings":
                    interest_rate = float(input("Enter interest rate (e.g., 0.02): "))
                    acc_no = bank.create_account(name, acc_type, balance, interest_rate=interest_rate)
                else:
                    fee = float(input("Enter withdrawal fee: "))
                    acc_no = bank.create_account(name, acc_type, balance, fee=fee)
                print(f"Account created successfully. Account number: {acc_no}")

            elif choice == "2":
                acc_no = input("Enter account number: ")
                amount = float(input("Enter deposit amount: "))
                account = bank.get_account(acc_no)
                if account:
                    account.deposit(amount)
                    print(f"Deposited £{amount:.2f}. New balance: £{account.get_balance():.2f}")
                else:
                    print("Account not found.")

            elif choice == "3":
                acc_no = input("Enter account number: ")
                amount = float(input("Enter withdraw amount: "))
                account = bank.get_account(acc_no)
                if account:
                    account.withdraw(amount)
                    print(f"Withdrawn £{amount:.2f}. New balance: £{account.get_balance():.2f}")
                else:
                    print("Account not found.")

            elif choice == "4":
                from_acc = input("Enter sender account number: ")
                to_acc = input("Enter receiver account number: ")
                amount = float(input("Enter transfer amount: "))
                bank.transfer(from_acc, to_acc, amount)
                print(f"Transferred £{amount:.2f} from {from_acc} to {to_acc}")

            elif choice == "5":
                acc_no = input("Enter account number: ")
                account = bank.get_account(acc_no)
                if account:
                    print(f"Balance: £{account.get_balance():.2f}")
                else:
                    print("Account not found.")

            elif choice == "6":
                acc_no = input("Enter account number: ")
                account = bank.get_account(acc_no)
                if account:
                    print("Transactions:")
                    for tx in account.get_transcations():
                        print(tx)
                else:
                    print("Account not found.")

            elif choice == "7":
                for acc in bank.accounts.values():
                    if acc.__class__.__name__ == "SavingsAccount":
                        acc.apply_interest()
                print("Interest applied to all savings accounts.")

            elif choice == "8":
                save(bank)
                print("Data saved. Exiting...")
                break

            else:
                print("Invalid choice.")

        except ValueError as ve:
            print(f"Error: {ve}")

if __name__ == "__main__":
    main()
