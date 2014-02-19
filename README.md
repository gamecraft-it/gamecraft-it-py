gamecraft-it-py
===============

Experimental python version of gamecraft-it (jekyll annoys me, I only want to be fighting bootstrap).

## Building / Serving / Pushing

1. python go.py help

At this point you should get some help.

*NB* this requires virtualenv & git to be available on the PATH. You might need to run some voodoo combination of "brew install python git" / "cinst python git" and then "pip install virtualenv".

Some commands which are correct as of this README:

1. serve - runs a local webserver at http://localhost:5000/
2. freeze - generates the static files into gamecraft-it.github.com
3. push / pull / checkout - performs git actions (push is most interesting)

(Pushing requires push rights to git@github.com:gamecraft-it/gamecraft-it.github.com.git)

## Structure

gamecraft-it-py

    /events - gamecraft events, upcoming and past. .md Markdown files with metadata at the top
    /gamecraft - python code
        web.py - used to map to pages and for build
        /static - static files, available via {{ url_for('static', filename='...') }} in templates
        /templates - Jinja 2 templates
    (/gamecraft-it-py - python virtualenv built to hold libraries)
    /gamecraft-it.github.com - git checkout of static site, files built into here and pushed from here
    (/gamecraft.egg-info - python package metadata)
    /posts - blog posts in .md markdown, metadata at top
