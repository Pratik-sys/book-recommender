from bookrecommender import app
from flask import render_template, url_for, request
import pandas as pd
import numpy as np
from bookrecommender.forms import GetField


@app.route("/home", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def home():

    form = GetField(request.form)
    data_read = pd.read_csv("./bookrecommender/new_dataset.csv")
    sort_books = pd.DataFrame([form.title.data], columns=["Tags"])
    merge_books = pd.merge(
        sort_books, data_read.sort_values(by=["rating-avg"], ascending=False)
    )
    df = pd.DataFrame(merge_books)
    return render_template(
        "home.html",
        df=df.to_html(),
        form=form,
        column=df.columns.values,
        row_data=list(df.values.tolist()),
    )