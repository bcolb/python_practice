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

You can also slice a list to form a smaller section of that list. Slicing lists will create a new copy of the list, not a reference to the existing list.

    >>>l = [1, 2, 3, 4, 5, 6]
    >>>l[:3]
    [1, 2, 3]
    >>>l[1:]
    [2, 3, 4, 5, 6]

List comprehension is pretty cool in python.

    >>> string_of_numbers = "1 2 3 4 5 6 7 8 9 10"
    >>> string_array = string_of_numbers.split(' ')
    >>> string_array
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    >>> num_array = [int(x) for x in string_array]
    >>> num_array
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> squares = [x**2 for x in num_array]
    >>> squares
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

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

Control Flow
------------

A number of data types can be used as boolean values.

Values evaluated as false include: False, 0, None, [], "", and other empty values.

Values evaluted as true include: True, 1, and everything else that's not an empty value.

Comparison expression can be made with the following operators:

    >, >=, <, <=, ==, !=, is, not, in, is not, not in

if-elif-else
------------

    >>> x = 7
    >>> if x < 7:
    ...     y = -9
    ...     z = 5
    ... elif x > 7:
    ...     y = 10
    ...     z = 1
    ... else:
    ...     y = 1
    ...     z = 2
    ... 
    >>> print(x, y, z)
    7 1 2

The block of code following the first condition evaluted to true will be executed. If none of the if or elif conditions evalute to true and an else clause is included, then the block of code proceeding the else clause will execute. The elif and else clauses are optional.

While Loops
-----------

While loops will continue to execute as long as the condition evaluates to true.

    >>> while count < 1000:
    ...     count *= 2
    ...     print(count)
    ... 
    2
    4
    8
    16
    32
    64
    128
    256
    512
    1024

The break and continue statements can also be used within the loop. The break statement will end the loop while the continue statement will abort the current interation of the loop.

for loops
---------

For loops are able to loop over any iterable type in python, including lists or tuples. The for loop in python is more like a for each loop in some other languages.

    >>> a_list = ["item one", 2, 3, "four", "Penguin", "Gnu"]
    >>> for item in a_list:
    ...     print(item)
    ... 
    item one
    2
    3
    four
    Penguin
    Gnu

You can still loop through a number space using the range function.

    >>> for i in range(0, 10):
    ...     print("i = ", i)
    ... 
    i =  0
    i =  1
    i =  2
    i =  3
    i =  4
    i =  5
    i =  6
    i =  7
    i =  8
    i =  9

functions
---------

Python functions are defined using the 'def' keyword.

    >>> def hello():
    ...     print("Hello world!")
    ... 
    >>> hello()
    Hello world!

Arguments can be passed in one of several ways, for instance by position:

    >>> def foo_bar(x, y, z):
    ...     sum = x + y + z
    ...     product = x * y * z
    ...     print("Sum = ", sum)
    ...     print("Product = ", product)
    ... 
    >>> foo_bar(1, 3, 9)
    Sum =  13
    Product =  27

Or you can use keyword arguments, or a combination of both:

    >>> def example(x, y=2, z=17):
    ...     print("x: ",x)
    ...     print("y: ",y)
    ...     print("z: ",z)
    ... 
    >>> example(1, 2, 3)
    x:  1
    y:  2
    z:  3
    >>> example(0)
    x:  0
    y:  2
    z:  17

Extra positional arguments can be collected into a tuple using *, and extra keywords into a dictionary using **:

    >>> def extra_tuple(*tup):
    ...     print(tup)
    ... 
    >>> extra_tuple(1, 2, 3, 4, 10)
    (1, 2, 3, 4, 10)
    >>> def extra_dictionary(**dictionary):
    ...     print(dictionary)
    ... 
   >>> extra_dictionary(n=1, d=2)
   {'d': 2, 'n': 1}

You can return a value using the return statement:

    >>> def hello_world():
    ...     return "Hello world!"
    ... 
    >>> hello_world()
    'Hello world!'

If a value isn't explicity returned, then the None value is returned.

Exceptions
----------

In python exceptions can be caught and handled by using the try-except-finally-else statements. This structure also allows you to catch and handle custom exceptions defined by the program. Uncaught exceptions cause the program to exit.

    >>> def open_file(filename):
    ...     try:
    ...         f = open(filename, 'r')
    ...         print(f.readline())
    ...         f.close()
    ...     except IOError as error:
    ...         print("The file %s could not be opened" % (filename))
    ...     else:
    ...         print("No exception occurred!")
    ...     finally:
    ...         print("This will always get executed")
    ... 
    >>> open_file("hello.txt")
    The file hello.txt could not be opened
    This will always get executed
    >>> open_file("README.md")
    python_practice
    
    No exception occurred!
    This will always get executed

Noe that both the else and finally clauses are optional.
