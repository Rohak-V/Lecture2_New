from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello World!"
    return render_template("index.html", headline=headline)


@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)