import argh

import logbook
import logbook.more

from gamecraft import (
    freezer,
    git,
    web,
)

def serve():
    """Runs the built in server

    """
    git.checkout()
    web.app.config.from_object('gamecraft.config.Development')
    web.app.run(debug=True)

def main():
    parser = argh.ArghParser()
    parser.add_commands([
        serve,
        git.checkout,
        git.pull,
        git.push,
        freezer.freeze,
    ])
    parser.dispatch()

if __name__ == '__main__':
    main()
