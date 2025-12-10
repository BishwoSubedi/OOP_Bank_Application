from bank import Bank

def main():
    bank = Bank()

    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. Show Accounts")
        print("3. Open Account")
        print("4. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("Name: ").strip()

            # Account number validation (integer only)
            while True:
                acc_number = input("Account number (numbers only): ").strip()
                if acc_number.isdigit():
                    break
                else:
                    print("Error: Account number must be an integer.")

            # Account type validation
            while True:
                acc_type = input("Type (savings/checking): ").lower().strip()
                if acc_type in ("savings", "checking"):
                    break
                else:
                    print("Error: Account type must be 'savings' or 'checking'.")

            # Balance input validation
            while True:
                try:
                    balance = float(input("Initial Balance (£): "))
                    break
                except ValueError:
                    print("Error: Invalid amount. Please enter a number.")

            bank.create(name, acc_number, acc_type, balance)

        elif choice == "2":
            bank.list_all()

        elif choice == "3":
            # Correct variable usage
            acc_number = input("Account number: ").strip()
            acc = bank.get(acc_number)

            if not acc:
                print("Account not found.")
                continue

            while True:
                print(f"\n--- Account {acc.get_acc_number()} ({acc.get_type()}) ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Balance")
                print("4. Transactions")
                print("5. Back")

                sub = input("Choose: ").strip()

                if sub == "1":
                    try:
                        amt = float(input("Deposit Amount (£): "))
                        if acc.deposit(amt):
                            bank.save()
                    except ValueError:
                        print("Invalid amount.")

                elif sub == "2":
                    try:
                        amt = float(input("Withdraw Amount (£): "))
                        if acc.withdraw(amt):
                            bank.save()
                    except ValueError:
                        print("Invalid amount.")

                elif sub == "3":
                    print(f"Current Balance: £{acc.get_balance():.3f}")

                elif sub == "4":
                    acc.show_all_transactions()

                elif sub == "5":
                    break

                else:
                    print("Invalid choice.")

        elif choice == "4":
            print("Thank you for using the bank system.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
