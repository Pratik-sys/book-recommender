from bookrecommender import app
from flask import render_template,request
import pandas as pd

@app.route("/", methods=["POST", "GET"])
def home():
    section=""
    data_read = pd.read_csv("./bookrecommender/Dataset.csv")
    if request.method == "POST":
        section = request.form["catdrop"].lower()
    sort_books = pd.DataFrame([section], columns=["Tags"])
    merge_books = pd.merge(sort_books, data_read.sort_values(by=["rating-avg"], ascending=False))
    df = pd.DataFrame(merge_books)

    return render_template("home.html",section=section,row_data=list(df.values.tolist()))
    