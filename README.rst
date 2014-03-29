BiSheng
=======

.. image:: https://badge.fury.io/py/bisheng.png
    :target: http://badge.fury.io/py/bisheng

.. image:: https://travis-ci.org/eliangcs/bisheng.png?branch=master
    :target: https://travis-ci.org/eliangcs/bisheng

.. image:: https://coveralls.io/repos/eliangcs/bisheng/badge.png?branch=master
    :target: https://coveralls.io/r/eliangcs/bisheng

A set of utility functions for processing Chinese text. Current features
include:

* Add spaces between Chinese/Japanese/Korean characters and halfwidth
  characters

* Convert traditional Chinese to simplified Chinese and the other way around


Installation
------------
::

    $ pip install bisheng


Usage
-----

Add spaces between Chinese characters and halfwidth characters::

    >>> import bisheng
    >>> print bisheng.add_spaces(u'BiSheng由Python寫成，名字源自1000多年前的活字印刷術發明人-畢昇。')
    BiSheng 由 Python 寫成，名字源自 1000 多年前的活字印刷術發明人 - 畢昇。

Specify the characters you want to exclude::

    >>> print bisheng.add_spaces(u'中[括]弧')
    中 [括] 孤

    >>> print bisheng.add_spaces(u'中[括]弧', exclude='[]')
    中[括]弧

Traditional/simplified Chinese conversion::

    >>> print bisheng.to_simp(u'畢昇')
    毕升

    >>> print bisheng.to_trad(u'毕升')
    畢升
