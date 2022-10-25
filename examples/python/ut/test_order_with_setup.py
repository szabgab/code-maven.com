import unittest

class TestOrder(unittest.TestCase):
    def helper(self):
        print("helper") 

    def setUp(self):
        print("in setUp")

    def tearDown(self):
        print("in tearDown")

    def test_one(self):
        print("test_one")

    def test_another(self):
        print("test_another")


