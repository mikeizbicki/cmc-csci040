#!/bin/python

'''
Lab instructions: 
Complete each function below so that all doctests pass.
You can run the doctess with the command

$ python3 -m doctest --verbose lab.py

Once all doctests pass, upload the output of the above command to sakai.
'''


def hypotenuse(a,b):
    '''
    Returns c = square root of a squared plus b squared

        >>> hypotenuse(3.0,4.0)
        5.0
        >>> hypotenuse(12.0,5.0)
        13.0
    '''


def is_even(n):
    '''
    Returns True if n is even and False if n is odd

    HINT: Use the modulus operator %

        >>> is_even(0)
        True
        >>> is_even(1)
        False
        >>> is_even(2000)
        True
        >>> is_even(-8)
        True
        >>> is_even(-9)
        False
    '''


def absolute_value(n):
    '''
    Returns the absolute value of n

        >>> absolute_value(5)
        5
        >>> absolute_value(-5)
        5
        >>> absolute_value(5.5)
        5.5
        >>> absolute_value(-5.5)
        5.5
    '''
    

def max_num(a,b):
    '''
    Returns the maximum of a and b

        >>> max_num(4,5)
        5
        >>> max_num(5,4)
        5
        >>> max_num(-4,-5)
        -4
        >>> max_num(4,4)
        4
    '''
    

def max_num_4(a,b,c,d):
    '''
    Returns the maximum of a, b, c, and d

    HINT:
    use the `max_num` function to find the maximum of a and b;
    use the `max_num` function to find the maximum of c and d;
    then use the `max_num` function to find the maximum of the results

        >>> max_num_4(1,2,3,4)
        4
        >>> max_num_4(2,3,4,1)
        4
        >>> max_num_4(3,4,1,2)
        4
        >>> max_num_4(4,1,2,3)
        4
        >>> max_num_4(10,1,2,3)
        10
    '''
    

def max_num_abs(a,b):
    '''
    Returns the number with the highest absolute value

        >>> max_num_abs(4,5)
        5
        >>> max_num_abs(4,5)
        5
        >>> max_num_abs(-4,-5)
        -5
        >>> max_num_abs(4,4)
        4
    '''


def num_digits(n):
    '''
    Returns the number of digits in the input n.
    Note that a negative sign does not count as a digit,
    only numbers do.

        >>> num_digits(5)
        1
        >>> num_digits(10)
        2
        >>> num_digits(45678)
        5
        >>> num_digits(123456789012345678901234567890)
        30
        >>> num_digits(-5)
        1
        >>> num_digits(-10)
        2

    HINT: convert the number into a string and use the length of the string
    '''
    

def is_leap_year(n):
    '''
    Returns True if n is a leap year and False otherwise.

    HINT: You can find the formula to calculate leap years here at 
    https://www.mathsisfun.com/leap-years.html

        >>> is_leap_year(1582)
        False
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(2018)
        False
        >>> is_leap_year(2019)
        False
        >>> is_leap_year(2020)
        True
        >>> is_leap_year(2200)
        False
        >>> is_leap_year(2400)
        True
    '''


def factorial(n):
    '''
    Returns the factorial of n.
    Recall that the factorial of n is defined to be: 1*2*3*...*(n-1)*n 

    HINT: 
    Use a for loop from 1 to n.
    On each iteration, multiple the current result by the current iteration number.

        >>> factorial(1)
        1
        >>> factorial(2)
        2
        >>> factorial(3)
        6
        >>> factorial(4)
        24
        >>> factorial(10)
        3628800
        >>> factorial(100)
        93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    '''


def is_prime(n):
    '''
    Returns true if n is prime, and false otherwise.
    Recall that a prime number is divisible only by itself and 1,
    and by convention 1 is not considered to be a prime number.

    HINT: 
    Use a for loop to check if every number between 2 and n-1 divides n

        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(4)
        False
        >>> is_prime(97)
        True
        >>> is_prime(99)
        False
    '''


def is_perfect_square(n):
    '''
    Returns true if n is is the product of two integers.

    HINT: 
    Use a for loop

        >>> is_perfect_square(1)
        True
        >>> is_perfect_square(2)
        False
        >>> is_perfect_square(4)
        True
        >>> is_perfect_square(97)
        False
        >>> is_perfect_square(0)
        True
        >>> is_perfect_square(-144)
        False
    '''


def fibonacci(n):
    '''
    Recall that the fibonacci numbers are calculated by the following formula:

    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

    This function computes the fibonacci numbers.

        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(2)
        1
        >>> fibonacci(3)
        2
        >>> fibonacci(4)
        3
        >>> fibonacci(5)
        5
        >>> fibonacci(6)
        8
        >>> fibonacci(7)
        13
        >>> fibonacci(1000)
        43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875

    HINT:
    Use a for loop from 0 to n, and store the values of the last two iterations in variables.
    '''
