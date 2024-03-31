"""This is a basic ATM Application.
This is a program consists of the basic actions of an ATM.
"""

accounts = [
    {
    "pin": 123456,
    "balance" : 1436.19},
    {
    "pin" : 246802,
    "balance": 3571.87},
    {
    "pin": 135791,
    "balance" : 543.79},
    {
    "pin" : 123987,
    "balance": 25.89},
    {
    "pin" : 269731,
    "balance": 3278.42}
]

# Define the `login` function for the ATM application.
def login(pin):
    global current_account
    for account in accounts:
        if int(pin) == account["pin"]:
            current_account = account
            print("Login successful. ")
            return
    print("Invalid PIN. Please try again. ")
current_account = None
# Define the `check_balance` function for the ATM application.
def check_balance():
     if current_account is not None:
        print(f"Your current balance is: ${current_account['balance']:.2f}")
     else:
        print("No account is currently logged in. Please login first.")
    
    

# Define the `make_deposit` function for the ATM application.
def make_deposit(account_balance, deposit):
    deposit_balance = account_balance
    if deposit > 0:
        deposit_balance = account_balance + deposit
    return deposit_balance

