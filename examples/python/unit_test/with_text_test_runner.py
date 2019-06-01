import unittest
import app

class WidgetTestCase(unittest.TestCase):
    def test_add(self):
        assert app.add(2, 2) == 4
        assert app.add(2, 3) == 5

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_add'))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)

