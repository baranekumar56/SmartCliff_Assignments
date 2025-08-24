
from products import Product

class Cart:

    def __init__(self):
        self.cart = []

    def add_to_cart(self, product: Product):
        self.cart.append(product)

    def remove_from_cart(self, name):
        for i in range(0, len(self.cart)):
            if self.cart[i].name == name:
                self.cart.pop(i)


    def get_total(self):
        summ = 0
        for i in self.cart:
            summ += i.price
        return summ

