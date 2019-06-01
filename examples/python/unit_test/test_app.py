import unittest
import app

class SomeTestCase(unittest.TestCase):
    def test_add(self):
        assert app.add(2, 2) == 4
        assert app.add(2, 3) == 5


