import pandas


df = pandas.read_csv("hotels.csv")
class User:
    def view_hotels(self):
        pass


class Hotel:
    def __init__(self, id):


    def book(self):
        pass
    def available(self):
        pass

class ReservationTicket:
    def __init__(self,customer_name, hotel_object):
    def generate(self):
        content = f"{customer_name}e of the customer hotel"
        return content

print(df)


id = input ("Enter the id of the hotel: ")
hotel = Hotel(id)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free")