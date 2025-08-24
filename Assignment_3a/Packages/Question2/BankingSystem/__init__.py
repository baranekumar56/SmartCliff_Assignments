
from account import Account
from transations import deposit, withdraw
from loan import Loan

def main():
    account = Account("barane",3454353, 10000)
    print(account.check_balance())

    deposit(account, 10000)
    withdraw(account, 100)

    l = Loan(10000, 10, 12)
    print(l.calculate_EMI())

if __name__ == "__main__":
    main()