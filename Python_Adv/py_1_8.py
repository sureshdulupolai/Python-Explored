"""

🏦 Account(Suresh, Balance: ₹5000)
BankAccount(owner='Priya', balance=3000)
Balance length: 5000
Merge Accounts: 🏦 Account(Suresh, Balance: ₹8000)
Subtract Accounts: 🏦 Account(Suresh, Balance: ₹2000)
Equal? False
Who is richer? Suresh
First Transaction: Deposit
Deposited ₹2000, New Balance: ₹7000
🔑 Access granted to Priya's account
🏦 Account(Priya, Balance: ₹3000)
🔒 Account Priya closed (with block ended)


"""
class BankAccount:
    def __init__(self, owner, balance=0):
        # __init__ → object initialization
        self.owner = owner
        self.balance = balance

    def __str__(self):
        # __str__ → human-readable string (print)
        return f"🏦 Account({self.owner}, Balance: ₹{self.balance})"

    def __repr__(self):
        # __repr__ → developer-friendly string
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

    def __len__(self):
        # __len__ → treat balance as "length"
        return self.balance

    def __add__(self, other):
        # __add__ → combine 2 accounts (balance merge)
        return BankAccount(self.owner, self.balance + other.balance)

    def __sub__(self, other):
        # __sub__ → subtract balances
        return BankAccount(self.owner, self.balance - other.balance)

    def __eq__(self, other):
        # __eq__ → equality check (==)
        return self.balance == other.balance

    def __lt__(self, other):
        # __lt__ → less than (<)
        return self.balance < other.balance

    def __gt__(self, other):
        # __gt__ → greater than (>)
        return self.balance > other.balance

    def __getitem__(self, index):
        # __getitem__ → support indexing (dummy transactions)
        transactions = ["Deposit", "Withdraw", "Transfer"]
        return transactions[index]

    def __call__(self, amount):
        # __call__ → make object callable like function (deposit money)
        self.balance += amount
        return f"Deposited ₹{amount}, New Balance: ₹{self.balance}"

    def __enter__(self):
        # __enter__ → Context manager (with statement start)
        print(f"🔑 Access granted to {self.owner}'s account")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # __exit__ → Context manager end
        print(f"🔒 Account {self.owner} closed (with block ended)")
        return False  # do not suppress exceptions


# ----------------- DEMO -----------------
a1 = BankAccount("Suresh", 5000)
a2 = BankAccount("Priya", 3000)

# 1. __str__ + __repr__
print(a1)        # human readable
print(repr(a2))  # developer readable

# 2. __len__
print("Balance length:", len(a1))

# 3. __add__ + __sub__
print("Merge Accounts:", a1 + a2)
print("Subtract Accounts:", a1 - a2)

# 4. __eq__, __lt__, __gt__
print("Equal?", a1 == a2)
print("Who is richer?", "Suresh" if a1 > a2 else "Priya")

# 5. __getitem__
print("First Transaction:", a1[0])

# 6. __call__
print(a1(2000))  # deposit using callable

# 7. __enter__ and __exit__
with a2 as acc:
    print(acc)


