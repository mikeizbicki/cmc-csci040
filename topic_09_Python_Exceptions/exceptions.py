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
# whenever the `object.function()` syntax is used, 
# but `.function` is not applicable for `object`

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
xs[-4]
'''
# NOTE: if using a slice (colon in []), never get IndexError

########################################
# KeyError:
# Whenever the [] notation is used is "doesn't exist" = "out of bounds" for a *dictionary*

'''
d = { 'text': 'hello world' }
d['created_at']
'''

########################################
# NameError/UnboundLocalError:
# Whenever a variable is used that has not been defined

'''
example
'''

'''
#text = 'text'
d = { 'created_at': 'hello world' }
d[text]
'''
'''
#new_example += 1
# new_example = new_example + 1
def foo():
    new_example += 1
    return new_example
d = { 'created_at': 'hello world' }
d['text']
foo()
'''

# UnboundLocalError: like NameError but inside functions
# differences between the two are subtle, you are not responsible for knowing the differences



########################################
# TypeError:
# There are several potential causes of this exception.

# 1. math operations are used on incompatible types

'''
x = 35
s = 'My age is ' + x
print('s=', s)
'''
'''
def foo(s):
    if len(s) > 10:
        return 'hello'
    if len(s) > 5:
        return 'goodbye'
s = foo('hel') + 'test'
print('s=', s)
None + 'test' # fix this error by finding the source of None, and figure out why it is None
'''
'''
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
x[1]
'''

'''
xs = [1, 2, 3]
xs['text'] # type error
xs[100]    # index error
'''

# 4. parens are used on non-functions

'''
x = 5
x()
'''

'''
def foo():
    return 5
foo()
# bar = foo + 10
foo = 5
foo()
'''

'''
xs = [1,2,3]
length = str(len(xs))
print('length=',length)
len(xs)
'''

# 5. a function is called with the wrong number of arguments

'''
len()

xs = []
ys = []
len(xs, ys)
xs_len = len(xs)
ys_len = len(ys)
'''

'''
import math
math.sqrt(5)
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

    What is the maximum of []?  That doesn't make sense, so we raise an error.
    '''
    assert(len(xs) > 0)
    maximum = xs[0]
    for x in xs:
        if x > maximum:
            maximum = x
    return maximum

maximum_value([1,2,3])
#maximum_value([])  # AssertionError
#maximum_value() # TypeError
#maximum_value(6) # TypeError

########################################
# ValueError:
# indicates that a "bad" value was passed to a function
# it's like assert, but allows for more user-friendly messages

'''
import math
math.sqrt(-1)
'''

'''
# valid:
int(2.3)
int('2')

# raises ValueError
int('2.3')
int('test')
'''

def maximum_value2(xs):
    '''
    Computes the maximum value of the list xs.
    '''
    if len(xs) == 0:
        raise ValueError('the input list cannot be empty')
    maximum = xs[0]
    for x in xs:
        if x > maximum:
            maximum = x
    return maximum

def foo(i):
    return maximum_value2(list(range(i)))

maximum_value2([1,2,3])
maximum_value2([1,2])
#maximum_value2([])
maximum_value2([2,3])
maximum_value2([2])

#foo(0)

########################################
# Any error can be "raised" from within a function


def example():
    raise ValueError('hello')
example()
