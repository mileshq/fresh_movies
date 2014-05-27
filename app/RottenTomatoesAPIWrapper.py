import requests
from urlparse import urljoin

API_BASE_URL = 'http://api.rottentomatoes.com/api/public/v1.0/'

class RottenTomatoesAPIWrapper(object):
	
	def __init__(self, api_key):
		self.api_key = api_key

	def create_params(self, title, page_limit=1, page=1):
		return {
			'apikey': self.api_key,
			'q': title,
			'page_limit': page_limit,
			'page': page
			}
	
	def create_url(self, url=API_BASE_URL):
		return urljoin(url, 'movies.json')

	def movies_search(self, title, page_limit=1, page=1):
		params = self.create_params(title, page_limit, page)
		url = self.create_url()
		response = requests.get(url, params=params)
		return response.json()