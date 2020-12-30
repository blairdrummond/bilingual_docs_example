Markdown vs reStructuredText
============================

Markdown is commonly used for writing documentation and other elements in a project. While it is possible to continue 
using Markdown in Sphinx, it is not recommended for a few different reasons.

* Lack of a standard
* Flavours
* Lack of Extensibility
* Lack of Semantic Meaning

Markdown was originally `created by John Gruber <https://daringfireball.net/projects/markdown/>`_ for use in blog 
engines. It was only intended to produce HTML output using text normally found in a blog article. It covers a fair 
amount of normal text use cases, but purposely excludes some of the more difficult elements such as tables and figures.
Support for extensions are also missing, which means your documents have very little semantic meaning. This replicates 
the problem commonly found with PDF parsing.

Due to the lack of a formal standard, Markdown has several different *flavours* that are not consistent across 
implementations. For example, GitLab uses one flabour, but GitHub uses another. These are mostly consistent for normal 
cases, but are not guaranteed to be. Other flavours exist as well, such as the one implemented by ``pandoc``.

reStructuredText as a solution
------------------------------

reStructuredText was invented for the purpose of writing technical documentation, and thus addresses the problems with 
Markdown through different features of the specification. For most normal writing, the overlap between the two 
makes producing ``.rst`` documents trivial if you are used to Markdown.

.. warning::

   This may not be true for all flavours of Markdown. `Refer to this gist <https://gist.github.com/dupuy/1855764>`_ to 
   see overlap and some differences.

Avoid converting existing documents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When starting a new Sphinx project you should produce ``.rst`` documents, but if you already have ``.md`` documents 
there is no reason to re-write them. Sphinx can use ``recommonmark`` to include markdown documents as source files.

.. literalinclude:: conf.py
   :language: python
   :lines: 30-36
