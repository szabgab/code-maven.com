import library
import mock

def my_helper(a):
    if a == 2:
        return 4
    raise Exception("Invalid test input '{}'".format(a))

library.helper = mock.MagicMock(side_effect=my_helper)

def test_library():
    assert library.main(2, 1) == 5
    assert library.main(2, -1) == 3
