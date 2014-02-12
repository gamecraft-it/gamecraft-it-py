"""Freezer"""
from flask_frozen import Freezer

import logbook

from gamecraft.web import app

freezer = Freezer(app)

log = logbook.Logger(__name__)

def freeze():
    """Generate the static site into gamecraft-it.github.com

    """
    app.config.from_object("gamecraft.config.Config")
    log.info("Writing out static files...")
    freezer.freeze()
