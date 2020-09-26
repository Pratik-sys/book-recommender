from bookrecommender import app
from flask import render_template, url_for, request
import pandas as pd 
import numpy as np
import os 

@app.route('/home', methods=['POST', 'GET'])
@app.route('/')

def home():
    return render_template("home.html")

@app.route('/test', methods=['POST', 'GET'])
def test():
    data_read = pd.read_csv("/Users/bug/book-recommendation/bookrecommender/new_dataset.csv")
    # data_sort = data_read.sort_values(by=['rating-avg'],ascending=False).head(n=5)
    p = pd.DataFrame(['AI'],columns=['Tags'])
    x = pd.merge(p,data_read.sort_values(by=['rating-avg'], ascending=False))
    h = x.to_html()
    return render_template("test.html", h=h)

@app.route('/display',methods=['POST', 'GET'])
def display():
    return render_template("display.html")