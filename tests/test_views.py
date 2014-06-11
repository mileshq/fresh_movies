import unittest
from flask import Flask
from config import config
from app import app

def dummyRT():
     return ""

class TestIndex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config.from_object(config['unit_test'])
        cls.client = app.test_client()

    def test_index_http_resopnse_code(self):
        response = self.client.get('/test')
        self.assertEquals(response.status_code, 200)

    def test_movie(self):
        response = self.client.get('/movies')
        self.assertEquals(response.status_code, 200)


    def test_get_movies(self):
        from app import views
        oldFunction = views.getMovies
        view.getMovies = dummyRT()

        response = self.client.post('/movies',{"title":"How to Train Your Dragon 2"})

        view.getMovies = oldFunction
