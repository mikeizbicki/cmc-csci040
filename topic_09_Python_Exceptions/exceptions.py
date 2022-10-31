# There are 9 Exceptions that you are required to know for the next quiz.
# This file reviews these exceptions and their causes.

########################################
# ZeroDivisionError:
# whenever you divide by 0

'''
12 / 0
12 / 0.0
12 // 0
12 % 0
'''

########################################
# AttributeError:
# whenever the `object.function()` syntax is used, but `.function` is not applicable for `object`

'''
xs = [1, 2, 3]          # mutable, things you change
xs.replace(2, 3)

s = 'hello '            # immutable, things you can't change
s.append('world')
'''

########################################
# IndexError:
# Whenever the [] notation is used is out of bounds for a *list*

'''
xs = [1, 2, 3]
xs[3]
'''

########################################
# KeyError:
# Whenever the [] notation is used is out of bounds for a *dictionary*

'''
d = { 'text': 'hello world' }
d['created_at']
'''

########################################
# NameError/UnboundLocalError:
# Whenever a variable is used that has not been defined

'''
example

d = { 'text': 'hello world' }
d[text]

def foo():
    new_example += 1
    return new_example
foo()
'''

########################################
# TypeError:
# There are several potential causes of this exception.

# 1. math operations are used on incompatible types

'''
'My age is ' + 35
None + 'test'
[1, 2, 3] + 4
'''

# NOTE:
# the following math operations are allowed
'''
4 + 0.4
'x' * 40   # but 'x' * 40.0 is not allowed
'''

# 2. len() is used on non-container types

'''
x = 5
len(x)
'''

# 3. subscripts are used on types that do not support them:

'''
x = 5
x[0]

xs = [1, 2, 3]
xs['test']
'''

# 4. parens are used on non-functions

'''
x = 5
x()

def foo():
    return 5
foo()
# bar = foo + 10
foo = 5
foo()
'''

# 5. a function is called with the wrong number of arguments
'''
len()

xs = []
ys = []
len(xs, ys)
'''

########################################
# AssertionError:
# whenever the `assert` function is called with a falsey argument

'''
assert(False)
assert(2 > 3)
assert([])
'''

# assert is commonly used inside functions to ensure that the input values are "reasonable"
def maximum_value(xs):
    '''
    Computes the maximum value of the list xs.
    '''
    assert(len(xs) > 0)
    maximum = xs[0]
    for x in xs:
        if x > maximum:
            maximum = x
    return maximum


########################################
# ValueError:
# indicates that a "bad" value was passed to a function
# it's like assert, but allows for more user-friendly messages

'''
import math
math.sqrt(-1)

int(2.3)
int('2.3')
int('test')
'''

def maximum_value2(xs):
    '''
    Computes the maximum value of the list xs.
    '''
    if len(xs) != 0:
        raise ValueError('the input list cannot be empty')
    maximum = xs[0]
    for x in xs:
        if x > maximum:
            maximum = x
    return maximum

########################################
# Any error can be "raised" from within a function

'''
def example():
    raise TypeError
example()
'''
