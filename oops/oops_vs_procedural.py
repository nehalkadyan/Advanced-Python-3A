# Create a program for Bank Transaction features
# like deposit money into bank, withdraw money and check current balance
# in your account

# user details
name = "John Doe"
account_number = "AC1002"
balance = 100000

def deposit_money(amount):
    # make the balance global
    global balance

    # check whether the amount is valid
    if amount > 0:
        # add the amount in the current balance
        balance += amount
        print(f"Deposited amount {amount}")
    else:
        print("Invalid Amount")

def withdraw_money(amount):
    global balance

    if amount > balance:
        print(f"Insufficient Balance")
    else:
        balance -= amount
        print(f"money withdrawn : {amount}")

def check_balance():
    print(f"Current Balance {balance}")

deposit_money(5000)
withdraw_money(20000)
check_balance()