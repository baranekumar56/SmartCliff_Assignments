
from products import Product
from discount import apply_coupons
from cart import Cart

def main():
    c = Cart()

    print("Enter 1 to add product \n"
          "Enter 2 remove product \n"
          "Enter 3 to enter coupons\n"
          "Enter 4 to get Total Value")
    discounts = 0
    choice = int(input())
    while True:
        match choice:
            case 1:
                name = input("Enter Product Name:")
                id = input("Enter Product Id:")
                price = int(input("Enter Product Price:"))
                prod = Product(id, name, price)
                c.add_to_cart(prod)
                choice = int(input("Enter Choice"))

            case 2:
                name = input("Enter Product Name to remove:")
                c.remove_from_cart(name)
                choice = int(input("Enter Choice"))

            case 3:
                coupons = list(map(int, input("Enter coupons").split()))
                discounts += sum(coupons)
                choice = int(input("Enter Choice"))

            case 4:
                print("Total:")
                print("Cart Total:", c.get_total())
                print("Total After Coupon Discounts:",apply_coupons(discounts, c.get_total()))
                return

if __name__ == "__main__":
    main()
