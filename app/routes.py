from flask import render_template, redirect, request
from app import app
from app.forms import SearchForm
import from .api import get_data

@app.route('/', methods = ['GET', 'POST'])
@app.route('/search', methods = ['POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        location = request.form.get('location')
        term = request.form.get('search')
        return redirect('/results/{}'.format(location))
    return render_template('search.html', form = form)

@app.route('/results/<location>')
def results(location):
    print(location)
    data = get_data(location)
    print(data)
    return render_template('results.html')
