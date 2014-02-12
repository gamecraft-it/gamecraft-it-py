import os
import subprocess

import argh

import logbook

from gamecraft.config import Config

log = logbook.Logger(__name__)

def checkout():
    """Checks out the static site

    """
    if not os.path.isdir(Config.CHECKOUT):
        log.info("Checking out {}", Config.CHECKOUT)
        subprocess.check_call(["git", "clone", Config.REPO, Config.CHECKOUT])
    log.debug("Already checked out {}", Config.CHECKOUT)

def pull():
    """Pulls the latest code

    """
    log.info("git pull --ff-only")
    subprocess.check_call(["git", "pull", "--ff-only"], cwd=Config.CHECKOUT)

@argh.arg("message", help="Commit message")
def push(message):
    """Pushes the changes (should prompt for a commit message)

    """
    log.info("git add .")
    subprocess.check_call(["git", "add", "."], cwd=Config.CHECKOUT)
    log.info("git commit with {!r}".format(message))
    subprocess.check_call(["git", "commit", "-m", message], cwd=Config.CHECKOUT)
    log.info("git push")
    subprocess.check_call(["git", "push", "origin", "master"], cwd=Config.CHECKOUT)
