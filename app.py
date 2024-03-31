from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/<string:page_name>")
def pages(page_name):
    return render_template(page_name)
