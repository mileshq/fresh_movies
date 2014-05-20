from app import app
from flask import render_template, request, flash
from flask.ext.wtf import form
from RottenTomatoesAPIManager import RottenTomatoesAPIManager
from forms import SearchMovieForm

@app.route('/', methods=['GET', 'POST'])
def index():
	form = SearchMovieForm()
	if request.method == 'GET':
		return render_template('movies.html', form=form)

	elif request.method == 'POST':
		if form.validate_on_submit() == False:
			return render_template('movies.html', form=form)

		rt = RottenTomatoesAPIManager(app.config['ROTTEN_TOMATOES_API_KEY'])
		rt_results = rt.movies_search(form.search_movie.data, page_limit=10, page=1)
		return render_template('movies.html', results=rt_results['movies'], form=form)
