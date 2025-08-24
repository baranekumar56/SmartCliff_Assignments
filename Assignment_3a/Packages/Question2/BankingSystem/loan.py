
class Loan:
    loan_amount = None
    rate = None
    duration = None

    def __init__(self, loan_amount, rate, duration):
        self.loan_amount = loan_amount
        self.rate = rate
        self.duration = duration

    def calculate_EMI(self):
        return (self.loan_amount * self.rate * (1 + self.rate) ** self.duration) / (1 + self.rate) ** self.duration - 1

