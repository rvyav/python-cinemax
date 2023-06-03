import random
import string

from cinemax.user import User


class Ticket(User):
    def __init__(self, name, email, price, seat_number):
        super().__init__(name, email)
        self.price = price
        self.seat_number = seat_number
        self.id = "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(8)
        )

    def generate_pdf(self):
        print("PDF GENERATED")
