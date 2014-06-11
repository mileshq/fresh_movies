import unittest
from flask import Flask
from config import config
from app import app

class TestIndex(unittest.TestCase):
	
	def setUp(self):
		app.config.from_object(config['unit_test'])
		self.client = app.test_client()
		
	def test_index_url_route_resolves(self):
		pass

	def test_index_http_response_code(self):
		response = self.client.get('/movies')
		self.assert200(response)

	def test_index_template_used(self):
		pass