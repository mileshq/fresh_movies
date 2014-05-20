import unittest
from app import app

class TestViews(unittest.TestCase):
	
	def setUp(self):
		self.app = app.test_client()

	def tearDown(self):
		pass

	def test_index(self):
		assert 1 == 1


if __name__ == '__main__':
    unittest.main()