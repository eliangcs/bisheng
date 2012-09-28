BiSheng
=======

BiSheng is a Python library that adds spaces between Chinese/Japanese/Korean
characters and halfwidth charaters (such as English letters), making the
article more beautiful and easier to read.

For example, the input text::

    BiSheng由Python寫成，名字源自1000多年前的活字印刷術發明人-畢昇。
    BiSheng由Python写成，名字源自1000多年前的活字印刷术发明人-毕升。
    BiShengはPythonで書かれ、名前は1000年前から活字印刷術の発明家-毕升。
    BiSheng은Python으로 작성되어,이름은1000년전의 이동 타입 기술의 발명가에서 유래-필승.

will become::

    BiSheng 由 Python 寫成，名字源自 1000 多年前的活字印刷術發明人 - 畢昇。
    BiSheng 由 Python 写成，名字源自 1000 多年前的活字印刷术发明人 - 毕升。
    BiSheng は Python で書かれ、名前は 1000 年前から活字印刷術の発明家 - 毕升。
    BiSheng 은 Python 으로 작성되어, 이름은 1000 년전의 이동 타입 기술의 발명가에서 유래 - 필승.

Installation
------------

Use ``pip``::

    $ pip install bisheng

or ``easy_install``::

    $ easy_install bisheng

Usage
-----

Call ``bisheng.add_spaces()`` and that's it::

    >>> import bisheng
    >>> bisheng.add_spaces(u'測試test') == u'測試 test'
    True
