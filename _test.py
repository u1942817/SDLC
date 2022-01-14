import pytest

def upper_case(x):
    return x.upper()

def test_upper_case():
    assert upper_case('cellis')=='CELLIS'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        upper_case(9)

def upper_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.upper()

def test_number():
    a = 10
    assert a== 10

#real example
class InsufficientAmount(Exception):
    pass

class Wallet:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InSufficientAmount('Not enough to spend {}'.format)(amount)
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount