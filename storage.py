def save(bank, filename="data/bank_data.txt"):
    with open(filename, "w") as f:
        for acc_no, acc in bank.accounts.items():
            f.write(f"{acc_no},{acc.get_balance()}\n")

def load(filename="data/bank_data.txt"):
    from bank import Bank
    bank = Bank()
    try:
        with open(filename, "r") as f:
            for line in f:
                acc_no, balance = line.strip().split(",")
                balance = float(balance)
                bank.accounts[acc_no] = bank.create_account(
                    name="Restored User",
                    acc_type="savings",
                    balance=balance
                )
        return bank
    except FileNotFoundError:
        return None
