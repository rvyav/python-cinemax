import re


class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def purchase(self, seat, card_status):
        pass

    def validate_email(self) -> bool:
        regex = re.compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        )
        if re.fullmatch(regex, self.email):
            return True
        else:
            return False
