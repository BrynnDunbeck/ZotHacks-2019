from flask import render_template, flash, redirect
from app import app
from app.forms import SearchForm

@app.route('/', methods = ['GET', 'POST'])
@app.route('/search', methods = ['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect('/results')
    return render_template('search.html', form = form)

@app.route('/results')
def results():
    return render_template('results.html')
