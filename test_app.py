import unittest
import json
import requests

class TestApp(unittest.TestCase):
    
    def test_hello_returns_200(self):
        response = requests.get('http://localhost:5050/api/hello')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()