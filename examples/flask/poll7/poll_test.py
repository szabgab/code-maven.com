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

    @unittest.expectedFailure
    def test_empty_result(self):
        rv = self.app.get('/results')
        self.assertEqual(rv.status_code, 200)
        self.assertRegexpMatches(rv.data, 'No results yet')

    def test_vote(self):
        rv = self.app.get('/poll?field=Flask')
        self.assertRegexpMatches(rv.data, '<h1>Thank you for submitting your vote for</h1>')

        rv_results = self.app.get('/results')
        self.assertRegexpMatches(rv_results.data, '<li>Flask 1</li>')
        self.assertRegexpMatches(rv_results.data, '<li>Django 0</li>')


if __name__ == '__main__':
    unittest.main()

