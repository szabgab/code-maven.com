import unittest
from test_app import SomeTestCase


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(SomeTestCase('test_add'))
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)

