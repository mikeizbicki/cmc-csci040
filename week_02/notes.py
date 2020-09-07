#print('hello world')
#print('goodbye world')
#print('hello friends')
#print('goodbye friends')
#print('hello world')

#x = 5
#print(x + 10)

# (a^2 +- sqrt(b - 4*a*c)) / (2*a)

a = 5
b = 10
c = 0

# not multiplication 4 x 5, a c
import math
#math.sqrt

# whenever you're doing math, pay careful attention to order of operations

quadratic = (a**2 - math.sqrt(b - 4*a*c)) / (2 * a)
print('quadratic=',quadratic)

# functions next

a = 5
b = 1000
c = 2

quadratic = (a**2 - math.sqrt(b - 4*a*c)) / (2 * a)
print('quadratic=',quadratic)

# functions let us group code together so we don't have to replicate it

def calculate_quadratic(a,b,c):
    # python is an indentation sensitive language or a whitespace sensative language
    result = (a**2 - math.sqrt(b - 4*a*c)) / (2 * a)
    return result


function_result = calculate_quadratic(5,10,0)
print('function_result=',function_result)
function_result = calculate_quadratic(5,1000,2)
print('function_result=',function_result)



# docstrings and doctests
def is_odd(n):
    '''
    returns True if n is odd, otherwise returns False

    if you use only 1 ', the docstring is only 1 line
    if you use three ', the docstring is multiple lines

        >>> is_odd(22)
        False
        >>> is_odd(23)
        True
    '''
    if n % 2 == 0:
        return False
    if n % 2 == 1:
        return True

x = 5 % 2  # = 1
y = 6 % 2  # = 0
print('x=',x)
print('y=',y)

# if keyword
# boolean operators

z = not 5 == 6 # not x == y      same as     x != y
print('z=',z)


q = is_odd(22)
print('q=',q)
print('is_odd(23)=',is_odd(23))