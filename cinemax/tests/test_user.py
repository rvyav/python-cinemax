import pytest
from cinemax.user import User


@pytest.fixture
def user_one():
    user = User("Ema", "jo3.com")
    return user


@pytest.fixture
def user_two():
    user = User("Gamoche Desniv", "ga221@outlook.com")
    return user


@pytest.fixture
def user_three():
    user = User("Sienna", "si.milena@gmail.com")
    return user


def test_user_one_email_not_valid(user_one: User):
    assert not user_one.validate_email()


def test_user_two_email_valid(user_two: User):
    assert user_two.validate_email()


def test_user_three_email_valid(user_three: User):
    assert user_three.validate_email()
