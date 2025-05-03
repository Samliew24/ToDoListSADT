import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app import app

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        # Test if homepage loads correctly
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_add_task(self):
        # Test adding a new task
        response = self.app.post('/add', data=dict(title="Test Task"))
        self.assertEqual(response.status_code, 302)  # Should redirect after adding

    def test_complete_task(self):
        # Dummy test, you can improve later
        pass

    def test_delete_task(self):
        # Dummy test, you can improve later
        pass

if __name__ == '__main__':
    unittest.main()
