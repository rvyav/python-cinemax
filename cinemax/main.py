from user import User
from typing import List, Dict

DATA = [
    {"name": "Hulk", "price": "$29.99", "seats": ["A1", "B3", "C21"]},
    {"name": "Indiana Jones", "price": "$21.99", "seats": ["C34"]},
    {"name": "FX 10", "price": "$34.99", "seats": ["A25", "E1"]},
    {"name": "Mamfar", "price": "$12.99", "seats": []},
]


class Processor:
    def run(self):
        name = input("Enter your name: ")

        while True:
            email = input("Enter your email (Format must be valid!!): ")

            user = User(name, email)
            is_email_valid = user.validate_email(email)

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

        # we just assume array of seats here will never be empty
        seats_available = _selection_mapper(movie_meta_data["seats"])

        while seats_available:
            # select seat

            # in a SQL case, this action would be locked
            # in a countdown thread so the seat row
            # cannot be accessed for a specific amount of time

            print("Seats currently available: {}".format(seats_available))

            try:
                seat_selected = int(input("Select a seat by its KEY: "))
                if seat_selected in seats_available.keys():
                    print("seat selected {}".format(seat_selected))
                    break
                else:
                    print("Wrong KEY provided as input")
                    continue
            except Exception as e:
                print("error: {}".format(e))
                continue


def _selection_mapper(selection: List[Dict[str, str]]) -> Dict[str, str]:
    """
    map index key with available selection of items.
    :selection: list of selected items
    """
    selection_range = [*range(1, len(selection) + 1)]
    return dict(zip(selection_range, selection))


if __name__ == "__main__":
    processor = Processor()
    print(processor.run())
