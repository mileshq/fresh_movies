from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class SearchMovieForm(Form):
	movie = StringField('', [Required("Required.")])
	submit = SubmitField('Search')
