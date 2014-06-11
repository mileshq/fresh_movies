import unittest
from flask import Flask, url_for
from app import app

class TestIndex(unittest.TestCase):

	def setUp(self):
		self.app = app
		self.client = app.test_client()

	def tearDown(self):
		pass

	def test_home_page(self):
		response = self.client.get('/')
		print response.get_data()
		self.assertTrue('Fresh Movies' in response.get_data(as_text=True))