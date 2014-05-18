import requests

API_BASE_URL = 'http://api.rottentomatoes.com/api/public/v1.0/'

class RottenTomatoesAPIManager(object):
	
	def __init__(self, api_key):
		self.api_key = api_key

	def movies_search(self, title, page_limit=1, page=1):
		params = {
			'apikey': self.api_key,
			'q': title,
			'page_limit': page_limit,
			'page': page
			}
		url = API_BASE_URL + 'movies.json' # url join helper function?
		response = requests.get(url, params=params)
		return response.json()