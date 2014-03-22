
import os

PACKAGE = os.path.abspath(os.path.join(os.path.dirname(__file__)))

CHECKOUT = os.path.abspath(os.path.join(PACKAGE, "..", "gamecraft-it.github.com"))

EVENTS = os.path.abspath(os.path.join(PACKAGE, "..", "events"))
POSTS = os.path.abspath(os.path.join(PACKAGE, "..", "posts"))

STATIC = os.path.join(PACKAGE, "static")


class Config(object):
    # REPO = "git@github.com:gamecraft-it/gamecraft-it.github.com.git"
    REPO = "https://github.com/gamecraft-it/gamecraft-it-py.git"
    CHECKOUT = CHECKOUT
    VENV = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "gamecraft-it-py"))
    POSTS = POSTS
    EVENTS = EVENTS

    FREEZER_BASE_URL = "http://gamecraft-it.github.io/"
    FREEZER_DESTINATION = CHECKOUT
    FREEZER_DESTINATION_IGNORE = [".git*"]

    STATIC = STATIC

    FLATPAGES_POSTS_ROOT = POSTS
    FLATPAGES_POSTS_EXTENSION = ".md"

    FLATPAGES_EVENTS_ROOT = EVENTS
    FLATPAGES_EVENTS_EXTENSION = ".md"


class Development(Config):
    DEBUG = True
