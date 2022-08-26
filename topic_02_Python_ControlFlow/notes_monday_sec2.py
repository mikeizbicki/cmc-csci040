''' this is a triple quote
# anything that begins with a # is a comment
# comments are code that doesn't get executed
print('hello world')
print("goodbye world")

var1 = 'hello'
var2 = 'world'
var3 = var1 + ' ' + var2
print(var3)
'''

'''
# for integers, python is always going to give you exact results;
# there are no size limits
# the type of a number with no period is called an int
x = 1
y = 5
z = 5**999 # 5 raised to the power of 999
print(x)

# non-integer numbers; (fractions, irrational numbers) are approximations
# type of a number with a period is called a float
x = 0.1
y = 0.1
z = 0.1
q = x + y + z
print(x)

# the last type is the str = "string" type, for strings

# python is an "untyped language" because we can change the type;
# java is a strongly typed language
x = 'this is a string'
print(x)
'''

# import=keyword; math=package/library that we are importing
import math
'''
# pseudocode for the quadratic formula
# (a**2 +- sqrt(b - 4ac)) / 2a
a = 5
b = 100
c = 2
quadratic1 = (a**2      + math.sqrt(b-4 *a * c)) / (2 * a)
quadratic2 = (a**2      - math.sqrt(b-4 *a * c)) / (2 * a)
print(quadratic1)
print(quadratic2)

a = 3
quadratic1 = (a**2      + math.sqrt(b-4 *a * c)) / (2 * a)
quadratic2 = (a**2      - math.sqrt(b-4 *a * c)) / (2 * a)
print(quadratic1)
print(quadratic2)
'''

# a*x**2 + b*x + c = 0

'''
# functions + variables are the key difference between Python and HTML/CSS;
# def = define a function
def quadratic(a, b, c):
    quadratic = (a**2      - math.sqrt(b-4 *a * c)) / (2 * a)
    # don't want to do this; doesn't let you use the value
    #print(result)
    return quadratic
    

x = quadratic(5, 100, 2)
y = quadratic(3, 100, 2)
print(x + y)
'''

x = 5
y = 26
print (y // x)
print (y % x) # percent is the "modulus operator"; which is the remainder

print(math.pi)

'''
quadratic_formula # this is called snake case
quadraticFormula # this is called camel case
'''