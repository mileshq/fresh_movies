import unittest
from app import app
from app.RottenTomatoesAPIManager import RottenTomatoesAPIManager

class TestAPIs(unittest.TestCase):
	
	def setUp(self):
		self.app = app.test_client()

	def tearDown(self):
		pass

	def test_movie_search(self):
		rt = RottenTomatoesAPIManager(app.config['ROTTEN_TOMATOES_API_KEY'])
		rt_results = rt.movies_search("X-Men Origins - Wolverine", page_limit=10, page=1)
		assert "X-Men Origins - Wolverine" == rt_results['movies'][0]['title']
		assert 2009 == rt_results['movies'][0]['year']

if __name__ == '__main__':
    unittest.main()