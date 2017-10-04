import unittest
from mymod_1 import is_anagram

class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(  is_anagram("abc", "acb") )
        self.assertTrue(  is_anagram("silent", "listen") )
        self.assertFalse( is_anagram("one", "two") )

    def test_multiword_anagram(self):
        self.assertTrue( is_anagram("ana gram", "naga ram") )
        self.assertTrue( is_anagram("anagram", "nag a ram") )

if __name__ == '__main__':
    unittest.main()
