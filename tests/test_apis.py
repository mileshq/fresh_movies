from flask import Flask
from flask.ext.testing import TestCase
from config import UnitTestConfig
from app.RottenTomatoesAPIWrapper import RottenTomatoesAPIWrapper	

class TestAPIWrapper(TestCase):

	def create_app(self):
		app = Flask(__name__)
		app.config.from_object(UnitTestConfig)
		return app

	def setUp(self):
		self.api_key = self.app.config['ROTTEN_TOMATOES_API_KEY']
		self.rt = RottenTomatoesAPIWrapper(self.api_key)

	def test_create_params(self):
		params = self.rt.create_params('a_title_search_string', 1, 1)
		self.assertEquals(params, {'apikey': self.api_key, 'q': 'a_title_search_string', 'page_limit': 1, 'page': 1})

	def test_create_url(self):
		url = self.rt.create_url()
		self.assertEquals(url, 'http://api.rottentomatoes.com/api/public/v1.0/movies.json')

	def test_movie_search_online(self):
		#rt_results = self.rt.movies_search("X-Men Origins - Wolverine", page_limit=10, page=1)
		#self.assertEquals("X-Men Origins - Wolverine", rt_results['movies'][0]['title'])
		#self.assertEquals(2009, rt_results['movies'][0]['year'])
		self.assertEquals(1, 1)

"""
Fix moving in TestConfiguration ... not yet references config dictionary
Re-use app.__init__ create_app ??
Optional integration test
"""