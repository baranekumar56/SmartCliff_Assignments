
# declarations for exceptions

class InputMismatchException(ValueError):
    pass

class NumberFormatException(Exception):
    pass

class ArrayIndexOutOfBoundsException(Exception):
    pass

class Book:
    name = None
    idd = None
    price = None
    quantity = None

    def __init__(self, name, idd, price, quantity):
        self.name = name
        self.idd = idd
        self.price = price
        self.quantity = quantity




# this class will be going the use Book object
class Inventory:

    max_capacity = None
    # list of books
    books = None

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.books = []

    def add_book(self):
        # this function gets all the details for book from the user
        try:
            name = input("Enter Book Name:")
            idd = int(input("Enter Book Id:"))

            while True:
                try :
                    price = input("Enter Price: ")
                    if not price.isdigit():
                        raise InputMismatchException()
                    break
                except InputMismatchException:
                    print("Please Enter a valid Price for the book")

            while True:
                try:
                    quantity = int(input("Enter Quantity: "))
                    if quantity < 0:
                        raise NumberFormatException()
                    break
                except NumberFormatException:
                    print("Please enter quantity in Positive")

            #when everything is good we append the book object to books array

            book = Book(name, idd, price, quantity)
            self.books.append(book)
            return True
        except Exception as e:
            print("Can not create Book object", e)

        return False

    def get_book_info_by_index(self):
        while True:
            try:
                index = int(input("Enter Index: "))
                if index < 0 or index >= len(self.books):
                    raise ArrayIndexOutOfBoundsException()

                return self.books[index]
            except ArrayIndexOutOfBoundsException :
                print("Index out of Bounds, enter between {} - {}".format(0, len(self.books)-1))


def main():

    inv = Inventory(3)
    inv.add_book()
    inv.add_book()
    inv.add_book()
    book = inv.get_book_info_by_index()
    print(book.__dict__)


if __name__ == "__main__":
    main()
