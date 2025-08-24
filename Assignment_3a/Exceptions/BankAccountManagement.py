

class PayOutOfBoundsException(Exception):
    pass

class AccountManagement:

    __current_balance = None
    __max_transaction_limit = None

    def __init__(self, current_balance, max_transaction_limit):
        self.__current_balance = current_balance
        self.__max_transaction_limit = max_transaction_limit

    def with_draw_amount(self, amount):
        print(self.__current_balance, amount)
        if amount > self.__max_transaction_limit:
            s = "Amount to be withdrawn exceeds transaction limit\nMax Transaction limit: {}".format(self.__max_transaction_limit)
            raise PayOutOfBoundsException(s)

        if amount > self.__current_balance:
            raise PayOutOfBoundsException("Insufficient Funds")

        self.__current_balance -= amount

        return "Transaction Done Successfully"


am = AccountManagement(80000, 30000)

am.with_draw_amount(20000)
am.with_draw_amount(40000)



