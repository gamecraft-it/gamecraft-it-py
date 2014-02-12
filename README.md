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

- events contains the events we want to promote
- posts contain any blog posts
- pages contain fixed pages (so index.html maps to /, foo.md maps to /foo and a sub folder maps to a subfolder). .html are rendered as jinja templates using templates. .md is rendered as markdown, then the templates are used.
- templates contain the Jinja templates for the site (for the most part we shouldn't have to touch these much)
