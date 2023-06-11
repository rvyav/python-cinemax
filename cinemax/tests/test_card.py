import pytest
from cinemax.card import Card
from cinemax.user import User


@pytest.fixture
def card_one():
    user = User("John", "john@gmail.com")
    card = Card(user.name, user.email, "debit", "4561234567123456", "John Doe", "001")
    return card


@pytest.fixture
def card_two():
    user = User("Helena", "h.markov124@hotmail.com")
    card = Card(
        user.name, user.email, "credit", "4561234567123456", "Avery Jones", "001"
    )
    return card


@pytest.fixture
def card_three():
    user = User("Helena", "h.markov124@hotmail.com")
    card = Card(
        user.name, user.email, "credit", "739108300028103", "Helena Davis", "001"
    )
    return card


class TestCard:
    def test_card_valid(self, card_one: Card):
        assert card_one.is_valid()

    def test_card_name_not_valid(self, card_two: Card):
        assert not card_two.is_valid()

    def test_card_number_not_valid(self, card_three: Card):
        assert not card_three.is_valid()
