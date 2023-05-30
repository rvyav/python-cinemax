import random
import string


class Ticket:
    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.seat_number = seat_number
        self.id = "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(8)
        )

    def is_seat_available(self):
        pass

    def get_ticket_price(self):
        pass

    def generate_pdf(self):
        pass
