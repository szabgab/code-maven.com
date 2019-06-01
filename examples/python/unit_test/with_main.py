import unittest
import app

class WidgetTestCase(unittest.TestCase):
    def test_add(self):
        assert app.add(2, 2) == 4
        assert app.add(2, 3) == 5

if __name__ == "__main__":
    unittest.main()
