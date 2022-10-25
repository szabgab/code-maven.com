import unittest

def middle(s):
    return s[len(s)/2]

class TestSome(unittest.TestCase):
    def setUp(self):
        print("in setUp")
    def tearDown(self):
        print("in tearDown")

    def test_one(self):
        print("test_one")
        #self.assertTrue(  middle("abc") == "b" )
        ##self.assertTrue(  middle("abcd") == "b" )
        #self.assertEqual(  middle("abcd"), "b" )


    def test_another(self):
        print("test_another")
        #self.assertTrue(  middle("a") == "a" )
        ##self.assertTrue(  middle("abcd") == "b" )
        #self.assertEqual(  middle("ab"), "a" )

