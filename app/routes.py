from flask import render_template, redirect, request
from app import app
from app.forms import SearchForm
from .api import get_data

@app.route('/', methods = ['GET', 'POST'])
@app.route('/search', methods = ['POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        location = request.form.get('location')
        term = request.form.get('search')
        return redirect('/results/{}/{}'.format(location, term))
    return render_template('search.html', form = form)

@app.route('/results/<location>/<term>')
def results(location, term):
    business = get_data(location)
    form = 
    return render_template('results.html')
