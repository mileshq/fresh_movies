from flask import render_template, request
from flask.ext.wtf import form
from RottenTomatoesAPIWrapper import RottenTomatoesAPIWrapper
from forms import SearchMovieForm
from app import app

@app.route('/movies', methods=['GET', 'POST'])
def index():
	form = SearchMovieForm()
	if request.method == 'GET':
		return render_template('movies.html', form=form)

	elif request.method == 'POST':
		if form.validate_on_submit() == False:
			return render_template('movies.html', form=form)

        results = getMovies(form.search_movie.data)
        return render_template('movies.html', results=results, form=form)

def getMovies(data):
    rt = RottenTomatoesAPIWrapper(app.config['ROTTEN_TOMATOES_API_KEY'])
    return rt.movies_search(data, page_limit=10, page=1)['movies']

@app.route('/test')
def test_route():
	return "Hello world"
