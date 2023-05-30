import re


class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def purchase(self, seat, card):
        pass

    def validate_email(self, email: str) -> bool:
        regex = re.compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        )
        if re.fullmatch(regex, email):
            return True
        else:
            return False
