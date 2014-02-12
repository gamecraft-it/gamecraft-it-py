gamecraft-it-py
===============

Experimental python version of gamecraft-it (jekyll annoys me, I only want to be fighting bootstrap).

## Building / Serving / Pushing

1. virtualenv gamecraft-it-py
2. gamecraft-it-py/bin/pip install -r requirements.txt
3. gamecraft-it-py/bin/python go.py help

At this point you should get some help

(Pushing requires push rights to git@github.com:gamecraft-it/gamecraft-it.github.com.git)

## Structure

- events contains the events we want to promote
- posts contain any blog posts
- pages contain fixed pages (so index.html maps to /, foo.md maps to /foo and a sub folder maps to a subfolder). .html are rendered as jinja templates using templates. .md is rendered as markdown, then the templates are used.
- templates contain the Jinja templates for the site (for the most part we shouldn't have to touch these much)
