"""The webapp and rendering engine

"""

import datetime

import flask

from flask_flatpages import FlatPages

import iso8601

app = flask.Flask(__name__)
app.config.from_object('gamecraft.config.Config')
# If you want more page types just add 'em here
event_pages = FlatPages(app=app, name="events")
posts_pages = FlatPages(app=app, name="posts")

@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/about/")
def about():
    return flask.render_template("about.html")

@app.route("/events/")
def events():
    today = datetime.datetime.combine(datetime.date.today(), datetime.time(0, 0, 0)).replace(tzinfo=iso8601.iso8601.UTC)
    p = iso8601.parse_date
    all_events = sorted(event_pages, key=lambda event: event.meta['start'])
    future_events = [event for event in all_events if p(event.meta['start']) >= today]
    past_events = [event for event in all_events if p(event.meta['start']) < today]
    return flask.render_template("events.html", past_events=past_events, future_events=future_events)

@app.route("/events/<event>/")
def view_event(event):
    event = event_pages.get_or_404(event)
    return flask.render_template("event.html", event=event)

# @app.route("/posts/")
# def posts():
#     posts = [post for post in posts_pages]
#     return flask.render_template("posts.html", posts=posts)

# @app.route("/posts/<post>/")
# def view_post(post):
#     post = post_pages.get_or_404(post)
#     return flask.render_template("post.html", post=post)
