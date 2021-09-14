''' this is a tripple quote
# python comments begin with #
# print is how we output to the screen
print('hello world')
print('goodbye world')
print("step 3")

# the thing to the left of = is the "name" of the variable and to the right is the "Value"
var1 = 'hello'
var2 = 'world' # things in quotations are called "string literals"
print(var1)
print(var2)
print(var1 + ' ' + var2)
print('#')
print('var1')
'''

'''
print('test')

# integers do not have a decimal place
# integers are exact, and all integers can be stored on your computer
x = 5**999
y = 7
z = x + y
print(z)

# if it has a decimal, we call it a "floating point number" or "float" for short
x = 0.1 + 0.1 + 0.1 # redefinition of the variable x
print(x)

# python is an untyped language
# each variable is not assigned a particular "type": int, float, str
x = 'x is a str'
print(x)
'''

'''
# quadritic formula
# "pseudocode" like code; shows the recipe; but maybe has some errors
# (a**2 +- sqrt(b - 4*a*c))/(2*a)
import math # anything in purple is a keyword; math is a package/library
a =  5
b = 1000
c = 3
formula = (a**2 + math.sqrt(b - 4*a*c)/(2*a))
print(formula)

a = 10
#formula = (a**2 + math.sqrt(b - 4*a*c)/(2*a))
print(formula)
'''
import math

# functions let us redo code without retyping the code
def quadratic_formula(a, b, c):
    result = (a**2 + math.sqrt(b - 4*a*c)/(2*a))
    return result

# if you don't have a print statement, then you won't output to the screen
x = quadratic_formula(5,1000,3)
print(x + 1)
#print(x)

'''
print('quadratic_formula(5,100,3)=', quadratic_formula(5,1000,3))
print('',quadratic_formula(6,1000,3))
print('',quadratic_formula(7,1000,3))
'''

x = 5
print(x < 10)

print("that's a \"string literal\"")