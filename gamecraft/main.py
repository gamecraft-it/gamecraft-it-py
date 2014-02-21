import os
import subprocess

import argh

import logbook
# from logbook.compat import redirect_logging
# redirect_logging()
import logbook.more

from gamecraft import (
    config,
    freezer,
    git,
    web,
)

log = logbook.Logger(__name__)

@argh.arg("--port", default=5000, type=int, help="Port to listen on")
@argh.arg("--host", default="localhost", help="Host interface to listen on, use 0.0.0.0 for all")
def serve(port=8080, host="localhost"):
    """Runs the built in server

    """
    git.checkout()
    web.app.config.from_object('gamecraft.config.Development')
    log.info("Will serve on http://{host}:{port}/ (you may see this message multiple times due to the reloader).".format(host=host, port=port))
    web.app.run(
        debug=True,
        host=host,
        port=port,
    )

def build():
    """Build the static files into gamecraft-it.github.com

    """
    git.checkout()
    git.pull()
    freezer.freeze()
    log.info("Frozen to {}", config.Config.CHECKOUT)

def update():
    """Update dependencies and libraries

    """
    pip = os.path.join(config.Config.VENV, "bin", "pip")
    subprocess.check_call([pip, "install", "-U", "-r", "requirements.txt"])

def main():
    parser = argh.ArghParser()
    parser.add_commands([
        build,
        serve,
        update,
    ])
    parser.add_commands([
        git.checkout,
        git.pull,
        git.push,
    ],
        namespace="git",
        title="Git related commands",
    )
    parser.dispatch()

if __name__ == '__main__':
    log_handler = logbook.more.ColorizedStderrHandler(level='DEBUG')
    with log_handler.applicationbound():
        main()
