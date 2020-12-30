Internationalization
====================

Sphinx is already set up for localization (l10n) and internationalization (i18n) in the interface, so when you generate 
outputs for either French or English all the UI components will be translated for you automatically. All you have to 
worry about is your own content.

Internally, Sphinx uses the **gettext** open standard for providing l10n and i18n. This means you write your documents 
in a defined source language, then generate message files that can be translated. All of these files are basic text 
documents, and work well with revision control. This lets you include them in your integration pipelines, and 
create a new deployment every time the documentation is updated.

Required components
-------------------

The ``sphinx-intl`` package is used to generate i18n message files::

   pip install sphinx-intl

The basic configuration was done for you when using ``sphinx-quickstart``. These values should already be in your 
`conf.py` file::

   locale_dirs = ['locale/']   # can be anything, but locale is best practice
   gettext_compact = False

Prepare for translation
-----------------------

The source text is converted to translation templates through the help of a ``make`` command::

   make gettext

The templates end up in ``_build/gettext``, if you want to look at them.

Generate message files
----------------------

The files that actually get translated are ``.po`` files. You will end up with a ``.po`` file for each of the source 
files, which are generated from the templates created in the last section.

Generate po files.

We’ll use the pot files generated in the above step::

   $ sphinx-intl update -p _build/gettext -l fr

You can specify multiple languages by supplying more ``-l`` switches to build multiple languages at once.

Once completed, the generated po files will be placed in the below directories::

   ./locale/fr/LC_MESSAGES/

Translate text
--------------

As noted above, these are located in the ``./locale/<lang>/LC_MESSAGES`` directory. Each paragraph of text in the source 
document is set as a ``msgid``, and the translated text is assigned to the ``msgstr`` value::

    msgid "Generate po files."
    msgstr "<FILL HERE BY TARGET LANGUAGE>"

Use your favourite text editor to update the ``.po`` files. The ``msgstr`` values are valid markup, so you can continue 
to use the appropriate ``rst`` commands.

Images with localized text can be name according to their language, so ``myfigure.png`` would have ``myfigure.fr.png`` 
as the localized image. How to detect translated images is handled through ``figure_language_filename`` in ``conf.py``.

Build translated outputs
------------------------

When you build oututs it will look up the value of the language parameter in ``conf.py`` or you may also specify the 
parameter on the command line. Since your source language is set in ``conf.py``, you select the target language on the 
command line::

   $ make -e SPHINXOPTS="-D language='fr'" html

You will find the translated documents in the ``_build/html`` directory, ready to be published. Any images with the 
appropriate translation will be used automatically, otherwise the original is used.

Updating translations when text changes
---------------------------------------

When your documentation changes it will be necessary to build new ``.pot`` and ``.po`` files. Building `.pot` files is 
the same process as earlier::

   make gettext

``sphinx-intl`` is able to tell what has changed in the translations, and so will be able to merge the already changed 
text with the new modifications::

   $ sphinx-intl update -p _build/locale

You can now translate the new text and rebuild the outputs as above.
