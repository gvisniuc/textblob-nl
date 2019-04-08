===========
textblob-nl
===========

.. image:: https://badge.fury.io/py/textblob-nl.png
    :target: http://badge.fury.io/py/textblob-nl
    :alt: Latest version

.. image:: https://travis-ci.org/sloria/textblob-nl.png?branch=master
    :target: https://travis-ci.org/sloria/textblob-nl
    :alt: Travis-CI

Dutch language support for `TextBlob`_.

Features
--------

- Part-of-speech tagging (``PatternTagger``)
- Sentiment analysis (``PatternAnalyzer``)
- Supports Python 2 and 3

Installing/Upgrading
--------------------

If you have `pip <http://www.pip-installer.org/>`_ installed (you should), run ::

    $ pip install -U textblob
    $ pip install -U textblob-nl

Usage
-----
.. code-block:: python

    >>> from textblob import TextBlob
    >>> from textblob_nl import PatternTagger, PatternAnalyzer
    >>> text = u"De kat wil wel vis eten maar geen poot nat maken."
    >>> blob.sentiment
    (-0.1, 0.4)

Requirements
------------

- Python >= 2.6 or >= 3.3

TODO
----

- Tokenization
- Parsing
- NLTK tagging?

License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/sloria/textblob-nl/blob/master/LICENSE>`_ file for more details.

.. _TextBlob: https://textblob.readthedocs.org/
