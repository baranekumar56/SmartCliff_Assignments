
initial_balance = int(input())

transactions = list(map(int, input().split()))


#we iterate through the transaction list and update initial balance with that ith transaction
def calculate_balance(initial_balance, transactions):

    for i in transactions:
        initial_balance += i

    return initial_balance

print(calculate_balance(initial_balance, transactions))