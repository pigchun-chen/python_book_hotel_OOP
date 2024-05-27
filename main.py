import pandas


df = pandas.read_csv("hotels.csv", dtype={"id": str})

df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_secure = pandas.read_csv("card_security.csv", dtype=str)

class User:
    def view_hotels(self):
        pass


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        self.city = df.loc[df["id"] == self.hotel_id, "city"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)
        pass

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

class ReservationTicket:
    def __init__(self,customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name} 
        City: {self.hotel.city}
        """
        return content

class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False

class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_secure.loc[df_secure["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False



print(df)


hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder= "pigchun", cvc= "123"):
        if credit_card.authenticate(given_password="mypass1"):
            print(""" Payment successful!""")
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name =name, hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit card authentication failed.")
    else:
        print("There was a problem with your payments")
else:
    print("Hotel is not free")