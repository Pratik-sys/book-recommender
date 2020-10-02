from bookrecommender import app
from flask import render_template, url_for, request
import pandas as pd
import numpy as np
import os
from bookrecommender.forms import GetField


@app.route("/home", methods=["POST", "GET"])
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/test", methods=["POST", "GET"])
def test():
    form = GetField(request.form)
    data_read = pd.read_csv("./bookrecommender/dataset.csv")
    # data_sort = data_read.sort_values(by=['rating-avg'],ascending=False).head(n=5)
    value = form.title.data
    print(value)
    p = pd.DataFrame([value], columns=["Tags"])
    x = pd.merge(p, data_read.sort_values(by=["rating-avg"], ascending=False))
    xc = pd.DataFrame(x)
    return render_template("test.html", xc=xc.to_html(), form=form, header=True)


@app.route("/display", methods=["POST", "GET"])
def display():
    return render_template("display.html")
