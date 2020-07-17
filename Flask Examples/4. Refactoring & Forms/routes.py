from app import app
from flask import render_template

import forms

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    form = forms.AddTaskForm()
    return render_template('about.html', form=form)