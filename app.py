from datetime import date

from flask import Flask, render_template, url_for
from flask import g

app = Flask(__name__)

def get_date():
    today = date.today()
    today_string = today.strftime("%B %d, %Y")
    return today_string

month = get_date().split()[0]

app.jinja_env.globals["date"] = get_date()
app.jinja_env.globals["month"] = month

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/undergraduate")
def undergraduate():
    return render_template("undergraduate.html")

@app.route("/internships")
def internships():
    return render_template("interns.html")

@app.route("/post_graduate")
def postgrad():
    return render_template("postgrad.html")

@app.route("/essays")
def essays():
    return render_template("essays.html")

@app.route("/others")
def others():
    return render_template("others.html")

@app.route(f"/<string:page_name>")
def pages(page_name):
    return render_template(page_name)

@app.route("/robots.txt")
def robot():
    return render_template("robots.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=False)