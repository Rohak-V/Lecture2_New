from flask import Flask, escape, request, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    render_template("index.html")


@app.route("/more")
def more():
    render_template("more.html")