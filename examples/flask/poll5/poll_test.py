from __future__ import print_function
import os
import unittest
import poll

class PollTestCase(unittest.TestCase):
    def setUp(self):
        if os.path.exists(poll.filename):
            os.remove(poll.filename)
        self.app = poll.app.test_client()

    def tearDown(self):
        if os.path.exists(poll.filename):
            os.remove(poll.filename)

    def test_main_page(self):
        rv = self.app.get('/')
        self.assertRegexpMatches(rv.data, '<title>Which web framework do you use\?</title>')
        self.assertRegexpMatches(rv.data, '<input type="radio" name="field" value="Flask"> Flask<br>')


if __name__ == '__main__':
    unittest.main()

