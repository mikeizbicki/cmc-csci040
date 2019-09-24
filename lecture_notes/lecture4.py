print('good morning!')

x = 45

if x > 60 or x > 0:
    print('x is big')
    print('x is big')
    print('x is big')
    print('x is big')
    print('x is big')
else:
    print('x is small')
    print('x is small')
    print('x is small')
    print('x is small')
    print('x is small')
print('not indented')

# causes an error:
# print(math.sqrt(15))

import math

print(math.sqrt(15))
print(math.sin(90))
print(math.pi)

# duck typing
# is if walks like a duck and quacks like a duck,
# then we should treat it like a duck
def simple(a,b,c):
    return a+b+c

def quadratic(a,b,c,x):
    return a*x**2 + b*x + c

def solve_quadratic(a,b,c):
    return (-b+math.sqrt(b**2-4*a*c))/(2*a)

# comments
# this
# is
# a
# multiline
# comment

# underscores in variables is called snake_case
# camel case thisIsCamelCase
# different than thisiscamelcase
def is_odd(n):
    '''
    This is the docstring.
    Docstring describe what a function does.

    Example: Returns True if n is odd.

    >>> is_odd(5)
    True
    >>> is_odd(4)
    False
    >>> is_odd(7)
    False
    '''
    if n%2 == 1:
        return True
    else:
        return False
      
import doctest
doctest.testmod()










