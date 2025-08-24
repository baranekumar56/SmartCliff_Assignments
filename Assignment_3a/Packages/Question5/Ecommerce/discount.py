
def apply_coupons(discounts, total):

    if discounts >= 100 :
        return 0

    return total * (1 - (discounts / 100))