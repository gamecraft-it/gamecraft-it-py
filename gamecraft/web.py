"""The webapp and rendering engine

"""

import flask

app = flask.Flask(__name__)
app.config.from_object('gamecraft.config.Config')

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/about/")
def about():
    return ""

@app.route("/events/")
def events():
    return ""