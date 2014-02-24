import os
import subprocess

import argh

import logbook

from gamecraft.config import Config

log = logbook.Logger(__name__)

def run(cmd):
    log.info(" ".join(cmd))
    subprocess.check_call(cmd, cwd=Config.CHECKOUT)


def checkout():
    """Checks out the static site

    """
    if not os.path.isdir(Config.CHECKOUT):
        log.info("Checking out {}", Config.CHECKOUT)
        subprocess.check_call(["git", "clone", Config.REPO, Config.CHECKOUT])
    log.debug("Already checked out {}", Config.CHECKOUT)


def pull():
    """Pulls the latest code and resets

    """
    run(["git", "pull", "--ff-only"])
    run(["git", "reset", "--hard", "origin/master"])
    run(["git", "clean", "--force", "-d"])


def status():
    """git status

    """
    run(["git", "status"])


def diff():
    """git diff

    """
    run(["git", "diff"])


@argh.arg("message", help="Commit message")
def publish(message):
    """Pushes the changes (should prompt for a commit message)

    Implicitly adds and removes files, this assumes the build step has done it's thing.

    """
    run(["git", "add", "-A"])
    run(["git", "commit", "-m", message])
    run(["git", "push", "origin", "master"])
