
class InvalidAgeError(Exception):
    pass

class SeatLimitError(Exception):
    pass

class FlightTicketBooker:

    def book_seat(self, name, age, seats):
        can_book = True
        try :
            age = int(age)
            if age < 0 or age > 120:
                raise InvalidAgeError()
        except ValueError:
            print("Age should be an integer")
            can_book = False
        except InvalidAgeError:
            print("Age Should be greater than 0 and less than 120")
            can_book = False


        try:
            seats = int(seats)
            if seats < 0 :
                raise ValueError("seats cannot bbe less than 1")
                can_book = False

            if seats > 6:
                raise SeatLimitError("Cannot Book more than 6 seats at once")
                can_book = False

        except ValueError :
            can_book = False
            print("Seats should be an integer")
        except SeatLimitError as e:
            print(e)

        if can_book:
            return "Booking Done successfully"
        else:
            return "Booking failed"


ftb = FlightTicketBooker()
print(ftb.book_seat("barane", 19, 4))