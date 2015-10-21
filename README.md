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

Basically an associative array implemented with hash tables. Works by storing key value pairs.

    >>> dict = {4: "four", 5: "five"}
    >>> len(dict)
    2
    >>> dict[5]
    'five'
    >>> list(dict.keys())
    [4, 5]
    >>> dict.get(4)
    'four'
    >>> dict.get(1, "not available")
    'not available'
    >>> 4 in dict
    True
    >>> 2 in dict
    False

Sets
----

An unordered collection of unique objects.

    >>> x = set([1, 3, 5, 7, 11])
    >>> x
    {11, 1, 3, 5, 7}
    >>> 1 in x
    True
    >>> 2 in x
    False

Tuples
------

Similar to lists but are immutable (cannot be changed after creation). They are more efficient to use than lists if you don't need modifiability.

* operators: in, +, \*
* functions: len, max, min
* methods: count, index
* index and slice notation work the same way as lists but cannot be used to add, remove, or replace

    >>> t = ()
    >>> t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    >>> t = (1, 2, "three", 1, 3)
    >>> t
    (1, 2, 'three', 1, 3)
    >>> t = (4, 5, [1, 2, 3], "eight")
    >>> t[2]
    [1, 2, 3]
    >>> x = ["one", "two", "three", "four"]
    >>> t = tuple(x)
    >>> t
    ('one', 'two', 'three', 'four')
    >>> y = list(t)
    >>> y
    ['one', 'two', 'three', 'four']

Files
-----

Files are accessed via the python file object.

    >>> f = open("hello.txt", "w")
    >>> f.write("Hello world!\n")
    13
    >>> f.write("This is a simple test file to demonstrate use of the python file object")
    71
    >>> f.close()
    >>> f = open("hello.txt", "r")
    >>> line1 = f.readline()
    >>> line2 = f.readline()
    >>> f.close()
    >>> print(line1, line2)
    Hello world!
     This is a simple test file to demonstrate use of the python file object

Using the os module.

    >>> import os
    >>> print(os.getcwd())
    /Users/myusername/Programs/python_practice
    >>> print(os.path.join("Users", "myusername", "Programs"))
    Users/myusername/Programs
    >>> print(os.path.join("/", "Users", "myusername", "Programs"))
    /Users/myusername/Programs
    >>> print(os.path.join("/", "Users", "myusername", "Programs", "python_practice"))
    /Users/myusername/Programs/python_practice
    >>> filename = os.path.join("/", "Users", "myusername", "Programs", "python_practice", "hello.txt")
    >>> print(filename)
    /Users/myusername/Programs/python_practice/hello.txt
    >>> f = open(filename, "r")
    >>> print(f.readline())
    Hello world!
    
    >>> f.close()