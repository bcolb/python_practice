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

Objects, Data Types and Pass By Reference
--------------------------------

Everything in python is an object with an associated type. Use the built-in 'type' function to check for an objects type.

In [1]: a = 5

In [2]: type(a)
Out[2]: int

In [3]: a = 'type test'

In [4]: type(a)
Out[4]: str

Python is pass by reference. Each bound variable references a location in memory where the object is located.

In [5]: id(a)
Out[5]: 4423117056

In [6]: b = a

In [7]: id(b)
Out[7]: 4423117056

In [8]: b = 'a different string'

In [9]: id(b)
Out[9]: 4422683480

In [10]: a
Out[10]: 'type test'

In [11]: b
Out[11]: 'a different string'

Functions are pass by reference, meaning that an argument passed into a function is merely a reference to an object. The function can then alter the object.

In [12]: id(a)
Out[12]: 4423117056

In [13]: def pass_by_reference_example(item):
   ....:     print id(a)
   ....:     

In [14]: pass_by_reference_example(a)
4423117056

Python is dynamically typed meaning variables can refer to different data types during runtime. However, it is strongly typed and with a few exceptions does not implicitly convert objects of different types during operations.

* Integers: 1, -3, 42
* Floats: 1.0, 3.14159, 7.77
* Complex Numbers: 3 + 2j, 4.2 + 6.3j
* Booleans: True, False

In [15]: x = 1

In [16]: type(x)
Out[16]: int

In [17]: x = 3.14159

In [18]: type(x)
Out[18]: float

In [19]: x = 3 + 2j

In [20]: type(x)
Out[20]: complex

In [21]: x = False

In [22]: type(x)
Out[22]: bool

It is worth noting that in regards to evaluation python is a strict or eager evaluator. Computations and expressions are evaluated immediately.		 
Most python objects are mutable, including user defined classes as well as lists and dicts. However, some objects like strings and tuples are immutable.
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

To properly copy a list that main contain objects use the deep copy library.

In [34]: l1 = ['a', 1, 2, 3, 4, ['listception']]

In [35]: l2 = l1

In [36]: l1
Out[36]: ['a', 1, 2, 3, 4, ['listception']]

In [37]: l2
Out[37]: ['a', 1, 2, 3, 4, ['listception']]

In [38]: l1[0] = 'b'

In [39]: l1
Out[39]: ['b', 1, 2, 3, 4, ['listception']]

In [40]: l2
Out[40]: ['b', 1, 2, 3, 4, ['listception']]

In [41]: l2 = deepcopy(l1)

In [42]: l1[0] = 'c'

In [43]: l1
Out[43]: ['c', 1, 2, 3, 4, ['listception']]

In [44]: l2
Out[44]: ['b', 1, 2, 3, 4, ['listception']]

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

Modules
-------

Modules can be created and then used in the same way that the built-in library modules are used. Below is an example module with a single function that gets Mars weather data for an external api.

    '''mars module. Get the temperature on mars'''
    import urllib.request
    import simplejson
    def report():
        url = "http://marsweather.ingenology.com/v1/latest/?format=json"
        mars_results = urllib.request.urlopen(url)
        json_results = simplejson.loads(mars_results.read())
        results = json_results['report']
        print(results)
        for result in results:
            print(result + ': ' + str(results[result]))
    if __name__ == '__main__':
        report()

To import and use this:

    >>> import mars
    >>> mars.report()
    season: Month 3
    max_temp: -31.0
    max_temp_fahrenheit: -23.8
    min_temp_fahrenheit: -115.6
    sol: 1151
    terrestrial_date: 2015-11-01
    pressure_string: Higher
    abs_humidity: None
    min_temp: -82.0
    wind_direction: --
    pressure: 901.0
    ls: 62.0
    sunrise: 2015-11-01T12:04:00Z
    wind_speed: None
    atmo_opacity: Sunny
    sunset: 2015-11-01T23:49:00Z

You can also organize modules into packages by creating a __init__.py file in the directory.

Object Oriented
---------------

To declare a class in python use the 'class' keyword. Methods are defined using the 'def' keyword, just like functions.

Class constructors are always defined as:

    def __init(self):
        self.name = 'someclass'

Methods must pass 'self' as the first argument, which is a reference to the current object. Classes can inherit from other classes by passing in the parent class during definition:

    class BorderCollie(Dog):
        ...

Note that classes must explicitly call the constructor of their parent class (assuming they have a parent class that is).

Here are a few examples of classes. Multiple classes can be defined in the same file.

    '''dogs module. Contains classes for Dog, BorderCollie, Husky.'''
    class Dog:
        '''Dog Class'''
        def __init__(self, color, age):
            self.color = color
            self.age = age
        def play(self):
            return "Rooof!"
        def __str__(self):
            return "Dog with color %s and age %s" % (self.color, self.age)
    
    class BorderCollie(Dog):
        '''Border Collie class'''
        def __init__(self, color="black/white", age=1, name="Border Collie"):
            Dog.__init__(self, color, age)
            self.name = name
        def play(self):
            return "Tilts head sideways"
    
    class Husky(Dog):
        '''Husky class'''
        def __init__(self, color="all white", age=1, name="Husky"):
            Dog.__init__(self, color, age)
            self.name = name
        def play(self):
            return "Jumps up and down"

Here's an interactive prompt using those classes:

    >>> import dogs
    >>> dog1 = dogs.Dog(color="Brown", age=4)
    >>> dog1.color
    'Brown'
    >>> dog1.age
    4
    >>> dog1.play()
    'Rooof!'
    >>> str(dog1)
    'Dog with color Brown and age 4'
    >>> dog2 = dogs.BorderCollie(name="Jimbo")
    >>> dog2.play()
    'Tilts head sideways'
    >>> str(dog2)
    'Dog with color black/white and age 1'


Control Flow
------------

Python supports short circuit evaluation.

    a = 1
    b = 9
    if a > 0 or b > 11:
        print("a or b is greater") # b never gets evaluated
    elif b < 10:
        print("B is less than 10")
    else:
        print("No conditions met")

