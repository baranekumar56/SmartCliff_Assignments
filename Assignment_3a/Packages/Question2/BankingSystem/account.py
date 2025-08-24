
class Account:
    name = ""
    id = ""
    balance = ""

    def __init__(self, name, id, balance):
        self.name = name
        self.id = id
        self.balance = balance

    def check_balance(self):
        return self.balance
