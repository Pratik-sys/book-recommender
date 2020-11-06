from bookrecommender import app
from flask import render_template, url_for, request
import pandas as pd
from bookrecommender.forms import GetField

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

@app.route("/display", methods=["POST", "GET"])
def display():
    return render_template('display.html')

@app.route("/test", methods=["POST", "GET"])
def test():
    return render_template('test.html')
    
@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == 'POST':
        title = request.form["books"]
    else:
        title = DEFAULT_TITLE

    data_read = pd.read_csv("./bookrecommender/Dataset.csv")
    title_sort = pd.DataFrame([title], columns=["Title"])
    merge_title = pd.merge(title_sort, data_read.sort_values(by=["rating-avg"], ascending=False))
    publisher_sort = pd.DataFrame([title], columns=["Publishers"])
    merge_publisher = pd.merge(publisher_sort, data_read.sort_values(by=["rating-avg"], ascending=False))
    title_df = pd.DataFrame(merge_title)
    publish_df = pd.DataFrame(merge_publisher)

    return render_template('search.html', title=list(title_df.values.tolist()),publish=list(publish_df.values.tolist()))
    