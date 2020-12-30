Getting Started
===============

The quickest way to being a new documentation project is to run the :command:`sphinx-quickstart` command from the 
:file:`docs` directory::

    $ sphinx-quickstart

This will ask you a series of questions and get you started with a default project::

    Welcome to the Sphinx 2.4.4 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Selected root path: .

    You have two options for placing the build directory for Sphinx output.
    Either, you use a directory "_build" within the root path, or you separate
    "source" and "build" directories within the root path.
    > Separate source and build directories (y/n) [n]: 

    The project name will occur in several places in the built documentation.
    > Project name: NDVI Calculator
    > Author name(s): Reginald Maltais
    > Project release []: 

    If the documents are to be written in a language other than English,
    you can select a language here by its language code. Sphinx will then
    translate text that it generates into that language.

    For a list of supported codes, see
    https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
    > Project language [en]: 

    Creating file ./conf.py.
    Creating file ./index.rst.
    Creating file ./Makefile.
    Creating file ./make.bat.

    Finished: An initial directory structure has been created.

    You should now populate your master file ./index.rst and create other documentation
    source files. Use the Makefile to build the docs, like so:
        make builder
    where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

Each time you change the source documents you can build a new copy by running the builder::

    $ make html

This builds the entire documentation tree and puts the output in :file:`_build`.