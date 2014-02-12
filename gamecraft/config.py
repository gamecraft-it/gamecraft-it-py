
import os

CHECKOUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "gamecraft-it.github.com"))

class Config(object):
    REPO = "git@github.com:gamecraft-it/gamecraft-it.github.com.git"
    CHECKOUT = CHECKOUT
    PAGES = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "pages"))
    POSTS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "posts"))
    EVENTS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "events"))

    FREEZER_BASE_URL = "http://gamecraft-it.github.io/"
    FREEZER_DESTINATION = CHECKOUT
    FREEZER_DESTINATION_IGNORE = [".git*"]

class Development(Config):
    DEBUG = True
