import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="LMS Portfolio", url=os.getenv("URL"))

@app.route('/about')
def about():
    return render_template('about.html', title="LMS Portfolio", url=os.getenv("URL"))

@app.route('/experience')
def experience():
    return render_template('experience.html', title="LMS Portfolio", url=os.getenv("URL"))

@app.route('/map')
def map():
    return render_template('map.html', title="LMS Portfolio", url=os.getenv("URL"))

