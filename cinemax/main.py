from user import User
from typing import List, Dict

from cinemax.card import Card
from cinemax.ticket import Ticket

DATA = [
    {"name": "Hulk", "price": "$29.99", "seats": ["A1", "B3", "C21"]},
    {"name": "Indiana Jones", "price": "$21.99", "seats": ["C34"]},
    {"name": "FX 10", "price": "$34.99", "seats": ["A25", "E1"]},
    {"name": "Mamfar", "price": "$12.99", "seats": []},
]

CREDIT_CARD = "credit"
DEBIT_CARD = "debit"


class Processor:
    def run(self):
        name = input("Enter your name: ")

        while True:
            email = input("Enter your email (Format must be valid!!): ")

            user = User(name, email)
            is_email_valid = user.validate_email()

            if not is_email_valid:
                print("Email format is not correct")
                continue
            else:
                break

        movies = [
            values
            for movies_data in DATA
            for key, values in movies_data.items()
            if key == "name"
        ]

        movies_available = _selection_mapper(movies)

        while movies_available:
            # movie selection
            print("Movies currently available: {}".format(movies_available))
            try:
                movie_selected = int(input("Select a movie by its KEY: "))
                if movie_selected in movies_available.keys():
                    movie = movies_available[movie_selected]
                    if movie == "Mamfar":
                        print(
                            "Unfortunately, the movie {} has no seats left".format(
                                movie
                            )
                        )
                        print("Please select another movie...")
                        del movies_available[movie_selected]
                        continue
                    break
                else:
                    print("Wrong KEY provided as input")
                    continue
            except Exception as e:
                print("error: {}".format(e))
                continue

        movie_meta_data = [
            movies_data for movies_data in DATA if movie in movies_data["name"]
        ][0]

        # we just assume the array of seats here will never be empty
        seats_available = _selection_mapper(movie_meta_data["seats"])

        while seats_available:
            # seat selection

            # in a SQL case, this action would be locked
            # in a countdown thread so the seat row
            # cannot be accessed for a specific amount of time
            print("Seats currently available: {}".format(seats_available))

            try:
                seat_selected = int(input("Select a seat by its KEY: "))
                if seat_selected in seats_available.keys():
                    seat_price = movie_meta_data["price"]
                    print("seat selected {}".format(seat_selected))
                    print("seat price is: {}".format(seat_price))

                    while seat_price:
                        try:
                            card_type_input = input("Enter card Type: ")
                            card_number_input = input("Enter card Number: ")
                            card_holder_input = input("Enter card Holder: ")
                            card_cvv = input("Enter card CVV: ")

                            card = Card(
                                name,
                                email,
                                card_type_input,
                                card_number_input,
                                card_holder_input,
                                card_cvv,
                            )

                            if card.is_valid():
                                seats_available: list[str] = movie_meta_data["seats"]
                                print(
                                    "Current seats available: {}".format(
                                        seats_available
                                    )
                                )

                                while True:
                                    seat_selection = input("Enter seat number: ")

                                    if seat_selection in seats_available:
                                        seats_available.remove()

                                        ticket = Ticket(seat_price, seat_selection)

                                        ticket.generate_pdf()
                                        break
                                    else:
                                        continue

                            else:
                                print("wrong")
                                continue
                        except Exception as e:
                            print("error: {}".format(e))
                else:
                    print("Wrong KEY provided as input")
                    continue
            except Exception as e:
                print("error: {}".format(e))
                continue


def _selection_mapper(selection: List[Dict[str, str]]) -> Dict[str, str]:
    """
    mapping range as keys with available selection of items.
    :selection: list of selected items
    """
    selection_range = [*range(1, len(selection) + 1)]
    return dict(zip(selection_range, selection))


if __name__ == "__main__":
    processor = Processor()
    print(processor.run())
