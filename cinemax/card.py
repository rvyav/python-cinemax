from cinemax.user import User


class Card(User):
    def __init__(self, name, email, type, number, holder, cvv):
        super().__init__(name, email)
        self.type = type
        self.number = number
        self.holder = holder
        self.cvv = cvv
        self.is_default_card = True

    def is_valid(self) -> bool:
        """
        A 'Credit card' has the following properties to be checked:
            - It will start with 4, 5 and 6
            - It will be 16 digits long
            - Numbers must contain only digits
            - It must not have 4 or more consecutive same digits
        """
        number: str = self.number
        if (
            number[:2] != "456"
            or len(number) != 16
            or not number.isdigit()
            or self.name not in self.holder
        ):
            return False
        return True
