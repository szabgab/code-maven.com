import pytest

def deposit(money):
    if money < 0:
        raise ValueError('Cannot deposit negative sum')

    # balance += money

def test_negative_deposit():
    with pytest.raises(ValueError) as e:
        deposit(-1)
    assert str(e.value) == 'Cannot deposit negative sum' 
