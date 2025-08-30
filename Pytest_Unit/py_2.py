# Fixture in PyTest

class Person:
    def __init__(self, name, favorite_color, year_born):
        self.name = name
        self.fav_color = favorite_color
        self.year_born = year_born
        self.friends = set()

    def add_friend(self, other_person):
        if not isinstance(other_person, Person): raise TypeError(other_person, 'is not a ', Person)
        self.friends.add(other_person)
        other_person.friends.add(self)

    def __repr__(self):
        return f'Person(name={self.name})' \
        f'Fav color={self.fav_color}' \
        f'year born={self.year_born}' \
        f'friends={[f.name for f in self.friends]}'


# --------------------------------------------------------------------------------------------------------
def test_name():
    terry = Person(
        'Suresh', 
        'Red',
        2006
    )

    assert terry.name == 'Suresh'

def test_add_friend():
    terry = Person(
        'Suresh', 
        'Red',
        2006
    )

    eric = Person(
        'Pritam',
        'Blue',
        2005
    )

    terry.add_friend(eric)
    assert eric in terry.friends
    assert terry in eric.friends
# -------------------------------------------------------------------------------------------------------

# this havy for more friend
import pytest

@pytest.fixture
def person_name():
    return 'Suresh Polai'

@pytest.fixture
def birth_year():
    return 2006

@pytest.fixture
def fav_colors():
    return 'Black'

def test_person_name(person_name, fav_colors, birth_year):
    person = Person(person_name, fav_colors, birth_year)
    assert person.name == person_name

def test_person_name_1(person_name, fav_colors, birth_year):
    person = Person(person_name, fav_colors, birth_year)

    # Expected mapping
    expected = {
        "name": person_name,
        "fav_color": fav_colors,
        "year_born": birth_year,
    }

    # Loop se saare attribute check karne ke liye
    for attr, expected_value in expected.items():
        actual_value = getattr(person, attr)
        assert actual_value == expected_value, f"{attr} mismatch: {actual_value} != {expected_value}"


# ------------------------------------------------------------------------------------
def test_person_name():
    lstOfData = [
        ('Suresh polai', 'Black', 2006),
        ('Pritam Updhayay', 'Blue', 2005)
    ]

    persons = list(map(lambda t: Person(*t), lstOfData))

    # assert persons[0].name == "Suresh polai"
    # assert persons[1].name == "Pritam Updhayay"

    for i in range(len(persons)):
        assert persons[i].name == lstOfData[i][0]


# ------------------------------------------------------------------------------------
# parameterizing fixture

import math

def is_prime(x):
    return all(x % factor != 0 for factor in range(2, int(x/2)))

@pytest.fixture(params=[2, 3, 5, 7, 11, 13, 17, 19, 101]) #  102
def prime_number(request):
    return request.param

def test_prime(prime_number):
    assert is_prime(prime_number) == True

# ----------------------------------------------------------------------------------
x = 0.1 + 0.2
y = 0.3

print('x==y', x==y)
print(x, '!=', y)

from pytest import approx
print(0.1 + 0.2 == approx(0.3))

# -------------------------------------------------------------------------------------