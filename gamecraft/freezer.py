"""Freezer"""

from gamecraft.web import app
from flask_frozen import Freezer

freezer = Freezer(app)

def freeze():
    """Generate the static site into gamecraft-it.github.com

    """
    app.config.from_object("gamecraft.config.Config")
    freezer.freeze()