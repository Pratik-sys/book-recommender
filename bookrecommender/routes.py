from bookrecommender import app
from flask import render_template, url_for

@app.route('/home', methods=['POST', 'GET'])
@app.route('/')

def home():
    return render_template("home.html")