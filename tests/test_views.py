from flask import Flask, url_for
from flask.ext.testing import TestCase
from config import UnitTestConfig
from app import views

class TestIndex(TestCase):
	
	def create_app(self):
		app = Flask(__name__)
		app.config.from_object(UnitTestConfig)
		#print "create_app: {}".format(__name__)
		return app

	def test_index_url_route_resolves(self):
		# test the decorator resolves
		# index_function = resolve('/')
		# self.assertEqual(views.index, index_function)
		# app.url_map
		#with self.app.test_request_context():
		#print "test_index_resolves: {}".format(url_for('index'))
		pass

	def test_index_http_response_code(self):
		response = self.client.get('/')
		print response.data
		self.assert200(response)

	def test_index_template_used(self):
		#response = self.client.get('/')
		#assertTemplateUsed
		pass

"""
"""