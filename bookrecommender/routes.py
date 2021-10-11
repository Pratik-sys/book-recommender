from bookrecommender import app
from flask import render_template,request
import pandas as pd

DEFAULT_H = "Python Programming"
DEFAULT_TITLE = ""
@app.route("/home", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def home():
    data_read = pd.read_csv("./bookrecommender/Dataset.csv")
    if request.method == "POST":
        h = request.form["catdrop"].lower()
    else:
        h = DEFAULT_H
    sort_books = pd.DataFrame([h], columns=["Tags"])
    merge_books = pd.merge(sort_books, data_read.sort_values(by=["rating-avg"], ascending=False))
    df = pd.DataFrame(merge_books)

    return render_template("home.html",row_data=list(df.values.tolist()))
    