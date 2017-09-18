from app import app
from flask import url_for
import unittest

class JackalFlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        del self.app

    def test_index(self):
        """Assert that user successfully lands on index page"""
        result = self.app.get('/index')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'wgx731', result.data)

    def test_home(self):
        """Assert that user successfully lands on home page"""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'GOOGL', result.data)
        self.assertIn(b'AAPL', result.data)

if __name__ == '__main__':
    unittest.main()

