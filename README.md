python_practice
=======================

A repo for review of python 2 and 3, practice problems in python, learning advanced python features, and exploring new python packages.

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
* FLoats: 1.0, 3.14159, 7.77
* Complex Numbers: 3 + 2j
* Booleans: True, False

    x = 1
    x = True
    x = 3.14159

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