def calc(a, op, b):
    '''
        from calc import calc
        calc(2, '+', 3)
    '''
    if op == '+':
        return a + b
    if op == '*':
        return a * b
    if op == '-':
        return a - b
    if op == '/':
        return a / b
    raise Exception("Operator '{}' not supported".format(op))


def test_calc():
    assert calc(2, '+', 3) == 5
    assert calc(2, '*', 3) == 6
    assert calc(8, '-', 3) == 5
    assert calc(8, '/', 2) == 4

    import pytest
    with pytest.raises(Exception) as exinfo:
        calc(2, '**', 3)
    assert exinfo.type == Exception
    assert str(exinfo.value) == "Operator '**' not supported"

# To test this module, run pytest calc.py
