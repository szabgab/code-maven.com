import echo_calc
import mock
from StringIO import StringIO

def test_add():
    with mock.patch('sys.stdout', new=StringIO()) as out:
        echo_calc.add(2, 3)
        assert out.getvalue() == "5\n"

    with mock.patch('sys.stdout', new=StringIO()) as out:
        echo_calc.add(3, 4)
        assert out.getvalue() == "7\n"

