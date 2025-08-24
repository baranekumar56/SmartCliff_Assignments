

class NegativeValueError(Exception):
    pass

class ZeroOrderError(Exception):
    pass


class OrderProcessor:

    def process_order(self, orders):
        for order in orders:

            if len(order) == 0:
                raise ZeroOrderError("Order list cannot be empty")


            quantity = int(order[1])
            if quantity < 0:
                raise NegativeValueError("Quantity cannot be negative")

            price = int(order[1])
            if price < 0:
                raise NegativeValueError("Price cannot be negative")


        print("Orders have been processed success fully")


op = OrderProcessor()
op.process_order([["soap", "erg", 1000], ["mouse",100,1000],[]])

