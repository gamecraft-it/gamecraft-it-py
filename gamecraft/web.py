"""The webapp and rendering engine

"""

import flask

from flask_flatpages import FlatPages

app = flask.Flask(__name__)
app.config.from_object('gamecraft.config.Config')
event_pages = FlatPages(app=app, name="events")
posts_pages = FlatPages(app=app, name="posts")

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/about/")
def about():
    return flask.render_template("index.html")

@app.route("/events/")
def events():
    events = [event for event in event_pages]
    return flask.render_template("events.html", events=events)

@app.route("/event/<event>/")
def view_event(event):
    event = event_pages.get_or_404(event)
    return flask.render_template("event.html", event=event)

@app.route("/posts/")
def posts():
    posts = [post for post in posts_pages]
    return flask.render_template("posts.html", posts=posts)

@app.route("/posts/<post>/")
def view_post(post):
    post = post_pages.get_or_404(post)
    return flask.render_template("post.html", post=post)
