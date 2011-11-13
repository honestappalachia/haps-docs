README
======

This repo contains the Sphinx source for the Honest Appalachia documentation.

To get started contributing to the docs, first clone this repo. `cd` into the directory and

## Install Sphinx

We assume you have Python installed on your system.

We recommend using the pip package manager. If you don't have it:

    $ easy_install pip

Now just

    $ pip install sphinx

On some systems you might have to `sudo` the install command.

Another alternative is to use `virtualenv`. This is the setup we use. virtualenv allows you to create isolated Python "sandboxes" customized individually for your projects. If you don't have virtualenv, install it:

    $ pip install virtualenv

Then create a new virtualenv in the same directory as the cloned repo. We recommend naming it `env` -- our `.gitignore` already contains an entry to ignore such a directory. If you change the name, ignore it as it will add unnecessary bloat and meaningless conflict to the repo. 

    $ virtualenv --no-site-packages --distribute env
    $ . env/bin/activate
    $ pip install sphinx

This will install sphinx into the virtualenv.

Notice how the second command caused your prompt to be prepended by `(env)`. This indicates the virtualenv is activated. Now any Python commands you launch from this shell will be executed inside the virtualenv, and any packages you install will be installed only in the virtualenv and will not affect your whole system.

To activate the virtualenv, use the command seen above:

    $ . env/bin/activate

To deactive, simply

    $ deactivate

## Working with Sphinx

Sphinx is an awesome documentation generation tool. Originally developed to document Python and Python modules, it is flexible enough to produce documentation for anything.

Sphinx collects any ReStructuredText files (`.rst`) it finds in the current directory and uses them to generate documentation. Additionally, static resources (images, etc.) should be placed in the `_static` directory.

After making changes to the documentation, build it using the included Makefile:

    $ make html

The output will be saved in `_build/html`. To visit the homepage of the generated documentation, for example, open `_build/html/index.html` in your browser.

## Sphinx and ReStructuredText Resources

1.  [Sphinx tutorial](http://sphinx.pocoo.org/tutorial.html)
2.  [rst-primer (sphinx-specific)](http://sphinx.pocoo.org/rest.html#rst-primer)
3.  [A ReStructuredText Primer (original)](http://docutils.sourceforge.net/docs/user/rst/quickstart.html)
4.  [Sphinx theming](http://sphinx.pocoo.org/theming.html)
