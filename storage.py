import pickle

def save(bank, filename="bank_data.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(bank, f)

def load(filename="bank_data.pkl"):
    try:
        with open(filename, "rb") as f:
            bank = pickle.load(f)
        return bank
    except FileNotFoundError:
        return None
