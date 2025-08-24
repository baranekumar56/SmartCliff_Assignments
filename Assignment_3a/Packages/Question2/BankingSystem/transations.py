from account import Account

def deposit(account: Account, amount):
    account.balance += amount

def withdraw(account: Account, amount):
    if account.balance >= amount:
        account.balance -= amount
    else:
        raise ValueError("Insufficient Balance")