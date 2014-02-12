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

def serve():
    """Runs the built in server

    """
    git.checkout()
    web.app.config.from_object('gamecraft.config.Development')
    log.info("Will serve on http://localhost:5000/ (you may see this message multiple times due to the reloader).")
    web.app.run(debug=True)

def build():
    """Build the static files into gamecraft-it.github.com

    """
    git.checkout()
    git.pull()
    freezer.freeze()
    log.info("Frozen to {}", config.Config.CHECKOUT)

def main():
    parser = argh.ArghParser()
    parser.add_commands([
        build,
        serve,
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
    log_handler = logbook.more.ColorizedStderrHandler(level='INFO')
    with log_handler.applicationbound():
        main()
