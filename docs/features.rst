reStructuredText & Sphinx features
==================================

Here are some highlights of features that are likely to be useful to data scientists and managers alike.

Basic text editing
------------------

Common text formatting is easy to implement through ``*`` and ````` characters::

    Mark *italic text* with one asterisk, **bold text** with two.
    For ``monospaced text``, use two "backquotes" instead.

Mark *italic text* with one asterisk, **bold text** with two.
For ``monospaced text``, use two "backquotes" instead.

Escaping text elements
^^^^^^^^^^^^^^^^^^^^^^

If you want to literally insert the ``*`` or ````` characters, you can escape them by including a backslash::

    \* will print the asterisk character
    \` will print the backquote character

Lists
^^^^^

You can create ordered and unordered lists easily by starting a line with ``*``, ``-``, or ``+``. Numbered lists start 
like ``1.``::

    * This will create 
    * an unordered list

      * even multiple levels

        + are possible

    1. This is an 
    2. ordered one

* This will create 
* an unordered list

  * even multiple levels

    * are possible

1. This is an 
2. ordered one

Use ``.. hlist::`` to create a list that spreads its terms over horizontal columns.

.. hlist::
   :columns: 2

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally

Code and console markup
-----------------------

Generic code sections are denoted by ending a paragraph with ``::`` characters and then indenting whatever you want to 
be highlighted as code::

    Everything with the same level of indent will be formatted as a block.

    Even across multiple paragraphs.

De-indenting then returns you to "normal" text. If you don't have any descriptive text for some reason, you can just 
put the ``::`` on a line by itself.

Importing docstrings
^^^^^^^^^^^^^^^^^^^^

You can import documentation from modules automatically::

    .. automodule:: ndvi.ndvi

.. automodule:: ndvi.ndvi
    :members:

Hard line breaks and quotes
---------------------------

You can force newlines for text by starting the line with the ``|`` character::

    | 100 Tunney's Pasture Driveway
    | Ottawa, Ontario

| 100 Tunney's Pasture Driveway
| Ottawa, Ontario

Quotes are denoted using blank spaces at the beginning of a line to inset the text.

    To be or not to be...
    *William Shakespear*

Mathematic notation
-------------------

You can enter math formulas in multiple ways. Inline expressions, like :math:`a^2 + b^2 = c^2`, are marked using 
``:math:``. Longer formulas use the ``.. math::`` directive::

    .. math::

        (a + b)^2 = a^2 + 2ab + b^2

        (a - b)^2 = a^2 - 2ab + b^2
    
.. math::

    (a + b)^2 = a^2 + 2ab + b^2

    (a - b)^2 = a^2 - 2ab + b^2

or 

.. math::
   :nowrap:

   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}

Multi-line exquations are possible as well::

    .. math::

        (a + b)^2  &=  (a + b)(a + b) \\
                   &=  a^2 + 2ab + b^2

.. math::

   (a + b)^2  &=  (a + b)(a + b) \\
              &=  a^2 + 2ab + b^2

Tables
------

Markdown doesn't support tables, though they are possible through extensions like :abbr:`GFM (GitLab Flavoured 
Markdown)`. You can generate tables in two different ways: (1) grid tables or (2) simple tables::

    +-------+----------+------+
    | Table Headings   | Here |
    +-------+----------+------+
    | Sub   | Headings | Too  |
    +=======+==========+======+
    | cell  | column spanning |
    + spans +----------+------+
    | rows  | normal   | cell |
    +-------+----------+------+
    | multi | * cells can be  |
    | line  | * formatted     |
    | cells | * paragraphs    |
    | too   |                 |
    +-------+-----------------+

+-------+----------+------+
| Table Headings   | Here |
+-------+----------+------+
| Sub   | Headings | Too  |
+=======+==========+======+
| cell  | column spanning |
+ spans +----------+------+
| rows  | normal   | cell |
+-------+----------+------+
| multi | * cells can be  |
| line  | * formatted     |
| cells | * paragraphs    |
| too   |                 |
+-------+-----------------+

::

    ===== ========= =====
    Table Headings  Here
    --------------- -----
    Sub   Headings  Too
    ===== ========= =====
    column spanning no
    --------------- -----
    cell  cell      row
    column spanning spans
    =============== =====

===== ========= =====
Table Headings  Here
--------------- -----
Sub   Headings  Too
===== ========= =====
column spanning no
--------------- -----
cell  cell      row
column spanning spans
=============== =====

Definition lists
----------------

Creating definition lists are relatively simple, and will end up creating terms for the glossary.

term
    word, expression, phrase, turn of phrase, idiom, locution; name, title, denomination, designation, label; formal 
    appellation.

Comments
--------

There is no support for comments in Markdown, which means any discussions around the content or hints need to take 
place outside of the content itself. This makes maintenance more difficult, and can lead to miscommunication between 
content maintainers.

You can create comments by creating a line with just two dots at the start::

    ..
        This will not be in the output.

..
    This will not be in the output.

Other features
--------------

reStructuredText and Sphinx have many more language features that you can explore in the `documentation 
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_.
