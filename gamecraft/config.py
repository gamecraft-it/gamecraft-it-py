
import os

CHECKOUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "gamecraft-it.github.com"))

EVENTS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "events"))
POSTS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "posts"))

class Config(object):
    REPO = "git@github.com:gamecraft-it/gamecraft-it.github.com.git"
    CHECKOUT = CHECKOUT
    VENV = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "gamecraft-it-py"))
    POSTS = POSTS
    EVENTS = EVENTS

    FREEZER_BASE_URL = "http://gamecraft-it.github.io/"
    FREEZER_DESTINATION = CHECKOUT
    FREEZER_DESTINATION_IGNORE = [".git*"]

    FLATPAGES_POSTS_ROOT = POSTS
    FLATPAGES_POSTS_EXTENSION = ".md"

    FLATPAGES_EVENTS_ROOT = EVENTS
    FLATPAGES_EVENTS_EXTENSION = ".md"

class Development(Config):
    DEBUG = True
