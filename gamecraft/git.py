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


def status():
    """git status

    """
    log.info("git status")
    subprocess.check_call(["git", "status"], cwd=Config.CHECKOUT)


def diff():
    """git diff

    """
    log.info("git diff")
    subprocess.check_call(["git", "diff"], cwd=Config.CHECKOUT)


@argh.arg("message", help="Commit message")
def publish(message):
    """Pushes the changes (should prompt for a commit message)

    Implicitly adds and removes files, this assumes the build step has done it's thing.

    """
    log.info("git add -A")
    subprocess.check_call(["git", "add", "-A"], cwd=Config.CHECKOUT)
    log.info("git commit with {!r}".format(message))
    subprocess.check_call(["git", "commit", "-m", message], cwd=Config.CHECKOUT)
    log.info("git push")
    subprocess.check_call(["git", "push", "origin", "master"], cwd=Config.CHECKOUT)
