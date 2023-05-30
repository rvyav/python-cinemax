from user import User

DATA = [
    {"name": "Hulk", "price": "$29.99", "seats": ["A1", "B3", "C21"]},
    {"name": "Indiana Jones", "price": "$21.99", "seats": ["C34"]},
    {"name": "FX 10", "price": "$34.99", "seats": ["A25", "E1"]},
    {"name": "Mamfar", "price": "$12.99", "seats": []},
]


class Processor(object):
    def run(self):
        name = input("Enter your name: ")

        while True:
            email = input("Enter your email (Format must be valid!): ")

            user = User(name, email)
            check_email = user.validate_email(email)

            if not check_email:
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

        movies_range = [*range(1, len(movies) + 1)]
        movies_available = dict(zip(movies_range, movies))

        while movies_available:
            print("Current movies available: {}".format(movies_available))
            try:
                movie_selected = int(input("Select a movie by its KEY: "))
                # TODO: Mamfar movie has no seats available
                if movie_selected in movies_available.keys():
                    movie = movies_available[movie_selected]
                    print("now select seat")
                    break
                else:
                    print("Wrong KEY provided as input")
                    continue
            except Exception as e:
                print("error: {}".format(e))
                continue


if __name__ == "__main__":
    processor = Processor()
    print(processor.run())
