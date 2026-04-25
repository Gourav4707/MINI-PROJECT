balance = 1000
transactions = []

def check_balance():
    print(f"\nCurrent Balance: ₹{balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))
    balance += amount
    transactions.append(f"Deposited ₹{amount}")
    print("Deposit successful!")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        transactions.append(f"Withdrew ₹{amount}")
        print("Withdrawal successful!")

def show_statement():
    print("\nTransaction History:")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print("-", t)
