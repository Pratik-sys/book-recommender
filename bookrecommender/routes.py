from bookrecommender import app
from flask import render_template, url_for, request
import pandas as pd

# from bookrecommender.forms import GetField

DEFAULT_H = "Python Programming"


@app.route("/home", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        h = request.form["catdrop"]
    else:
        h = DEFAULT_H
    data_read = pd.read_csv("./bookrecommender/new_dataset.csv")
    new = pd.DataFrame(data_read)
    sort_books = pd.DataFrame([h], columns=["Tags"])
    merge_books = pd.merge(
        sort_books, data_read.sort_values(by=["rating-avg"], ascending=False)
    )
    df = pd.DataFrame(merge_books)

    return render_template(
        "home.html",
        row_data=list(df.values.tolist()),
        new_row=list(new.values.tolist()),
    )

