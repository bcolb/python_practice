python_practice
=======================

A repo for review of python 2 and 3, practice problems in python, learning advanced python features, and exploring new python packages.

Helpful Links
=============

* Install [Python 3.5](https://www.python.org/downloads/release/python-350/)

Python Fundamentals (Python 3)
=======================

### Helpful Functions

    help()    # Provides information about functions and documentation
    dir()     # Lists the objects in a namespace
    globals() # Lists global variables
    locals()  # Lists local variables

Data Types
----------

Python is dynamically typed so variables can refer to different data types during runtime.

* Integers: 1, -3, 42
* Floats: 1.0, 3.14159, 7.77
* Complex Numbers: 3 + 2j, 4.2 + 6.3j
* Booleans: True, False
    >>>x = 1
    >>>x = 3.14159
    >>>x = 3 + 2j
    >>>x = False

Basic arithmetic operators include:

* addition: + 
* subtraction: -
* multiplication: *
* division (float): /
* division (truncation): //
* exponentiation: **
* modulus: %

Math module includes useful functions.

    >>> round(3.14159)
    3
    >>> import math
    >>> math.ceil(3.14159)
    4

Lists
-----

A list can include multiple data types including other lists, tuples, Strings, etc.

    >>>l = []
    >>>l = [1]
    >>>l = [1, 2, 3, 4]
    >>>l = [1, 2, [3, 4], 5]
    >>>l[2]
    [3, 4]
    >>>l[2][1]
    4

Lists can be indexed from the front with positive indices or from the rear with negative indices.

    >>>l = [1, 2, 3, 4, 5, 6]
    >>>l[0]
    1
    >>>l[-1]
    6
    >>>l[-3]
    4

You can also slice a list to form a smaller section of that list.

    >>>l = [1, 2, 3, 4, 5, 6]
    >>>l[:3]
    [1, 2, 3]
    >>>l[1:]
    [2, 3, 4, 5, 6]

There are additional list methods and operators.

* operators: in, +, *
* functions: len, max, min
* methods: append, count, extend, index, insert, pop, remove, reverse, sort

Strings
-------

Strings are immutable in python. Operators and functions on strings return entirely new strings.

    "Can use double quotes and can contain 'single quotes'"
    'Single quotes can contain "double quotes"'
    '''\tStarts with a tab, ends with a newline\n'''
    """Triple quoted strings can contain newlines"""

* operators: int, +, *
* functions: len, max, min
* index and slice notation also work, but cannot be used to add, remove or replace elements

Regular expressions

    >>> y = "To be or not to be, that is \tthe \tquestion"
    >>> y
    'To be or not to be, that is \tthe \tquestion'
    >>> print(y)
    To be or not to be, that is	the	question
    >>> y.replace("question", "answer")
    'To be or not to be, that is \tthe \tanswer'
    >>> print(y)
    To be or not to be, that is	the	question
    >>> import re
    >>> regexpr = re.compile(r"[\t ]+")
    >>> regexpr.sub(" ", y)
    'To be or not to be, that is the question'

Convert other data types to strings

    >>> e = 2.718
    >>> x = ["one", 2, 3.0, "four", ["a", "b"], (5, 6)]
    >>> print("The constant e is:", e, "and the list x is:", x)
    The constant e is: 2.718 and the list x is: ['one', 2, 3.0, 'four', ['a', 'b'], (5, 6)]
    >>> print("the value of %s is: %.2f" % ("e", e))
    the value of e is: 2.72

Dictionaries
------------

