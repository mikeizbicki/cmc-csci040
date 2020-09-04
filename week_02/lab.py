#!/bin/python

'''
Lab instructions: complete each function so that all doctests pass.
'''


def absolute_value(n):
    '''
    this function returns the absolute value of n

        >>> absolute_value(5)
        5
        >>> absolute_value(-5)
        5
        >>> absolute_value(5.5)
        5.5
        >>> absolute_value(-5.5)
        5.5
    '''
    

def hypotenuse(a,b):
    '''
    returns c = square root of a squared plus b squared

        >>> hypotenuse(3.0,4.0)
        5.0
        >>> hypotenuse(12.0,5.0)
        13.0
    '''
    

def max_num(a,b):
    '''
    this function returns the maximum of a and b

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
    this function returns the maximum of a, b, c, and d

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
    this function returns the number with the highest absolute value

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
    Calculates the factorial of n.
    Recall that the factorial of n is defined to be: 1*2*3*...*(n-1)*n 

    HINT: use a for loop

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
    Returns true if n is prime, and false otherwise
    Recall that a prime number is divisible only by itself and 1,
    and by convention 1 is not considered to be a prime number.

    HINT: use a for loop

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


# DO NOT MODIFY BELOW THIS LINE
import doctest
doctest.testmod(verbose=True)
