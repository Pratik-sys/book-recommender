from bookrecommender import app
from flask_table import Table, Col
from flask import render_template, url_for, request
import pandas as pd
import numpy as np
import os
from bookrecommender.forms import GetField
# from IPython.display import Image, HTML


class BookTable(Table):
    image = Col('Image')
    Title = Col('Title')
    Edition = Col('Edition')
    Publishers = Col('Publishers')
    Tags = Col('Tags')


# def path_to_image_html(path):
#     return '<img src="'+ path + '" style=max-height:124px;"/>'

@app.route("/home", methods=["POST", "GET"])
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/display", methods=["POST", "GET"])
def display():
    return render_template("display.html")

@app.route("/recommend", methods=["POST", "GET"])
def recommend():

    form = GetField(request.form)
    data_read = pd.read_csv("./bookrecommender/MD.csv")    
    sort_books = pd.DataFrame([form.title.data], columns=["Tags"])
    merge_books = pd.merge(sort_books, data_read.sort_values(by=["rating-avg"], ascending=False))
    df = pd.DataFrame(merge_books)
    output_dict = df.to_dict(orient='records') 
    table = BookTable(output_dict) 
    return render_template("test.html", df=table.__html__(), form=form)




# @app.route("/ok", methods=["POST", "GET"])
# def ok():
#     data_read = pd.read_csv("./bookrecommender/test2.csv")
#     df = pd.DataFrame(data_read)

#     return render_template("ok.html", df=df.to_html(classes='table', escape=False))