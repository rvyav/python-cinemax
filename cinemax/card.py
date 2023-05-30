from cinemax.user import User


class Card(User):
    def __init__(self, name, email, type, number, holder, cvv):
        super().__init__(name, email)
        self.type = type
        self.number = number
        self.holder = holder
        self.cvv = cvv
        self.is_default_card = True

    def is_valid(self, number: str) -> bool:
        """
        A 'Credit card' has the following properties to be checked:
            - It will start with 4, 5 and 6
            - It will be 16 digits long
            - Numbers must contain only digits
            - It may have digits in four groups separated by '-'
            - It must not use any other separator like space or underscore
            - It must not have 4 or more consecutive same digits
        """
        # check holder vs name
        pass
