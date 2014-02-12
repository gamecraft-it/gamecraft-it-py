import os
import subprocess

from gamecraft.config import Config


def checkout():
    """Checks out the static site

    """
    if not os.path.isdir(Config.CHECKOUT):
        subprocess.check_call(["git", "clone", Config.REPO, Config.CHECKOUT])

def pull():
    """Pulls the latest code

    """
    checkout()
    subprocess.check_call(["git", "pull", "--ff-only"], cwd=Config.CHECKOUT)

def push():
    """Pushes the changes (should prompt for a commit message)

    """
    checkout()
    subprocess.check_call(["git", "add", "."], cwd=Config.CHECKOUT)
    subprocess.check_call(["git", "commit"], cwd=Config.CHECKOUT)
    subprocess.check_call(["git", "push", "origin", "master"], cwd=Config.CHECKOUT)
