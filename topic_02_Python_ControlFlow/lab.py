#!/bin/python

'''
Lab instructions:
Complete each function below so that all doctests pass.
Recall that you can run the doctests with the command

$ python3 -m doctest --verbose lab.py

Once all doctests pass, upload the output of the above command to sakai.
You do not need to upload your python file.

NOTE:
Each problem should be relatively straightforward and take less than 10 minutes.
If you're spending more than 10 minutes on a problem,
then you should stop and seek help.
The QCL has mentors available over the weekend for help.

NOTE:
If you do not fully understand the material in this lab,
then you will not be able to complete the remainder of this course.
I strongly encourage you to collaborate with other students,
but make sure you are doing it in a way that is helping you understand the material.
Don't just copy another students' solution.

NOTE:
You are allowed to use LLMs like chatgpt for any programming assignments in this course.
LLMs are generally good at the type of problems in this lab,
and can answer most/all of these problems correctly by themselves.
I encourage you, however, to not just blindly use LLMs and copy/paste their solutions.
A good rule of thumb is to only ask an LLM for help after you've tried working on the problem by yourself for at least 10 minutes.

NOTE:
There is no partial credit on this lab.
In order to get credit, your functions must pass all of the test cases.
'''


def hypotenuse(a, b):
    '''
    Return the square root of a squared plus b squared.

    >>> hypotenuse(3.0, 4.0)
    5.0
    >>> hypotenuse(12.0, 5.0)
    13.0
    >>> hypotenuse(12, 5)
    13.0
    >>> type(hypotenuse(12.0, 5.0))
    <class 'float'>
    '''


def is_even(n):
    '''
    Return True if n is even and False if n is odd.

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
    >>> type(is_even(0))
    <class 'bool'>
    '''


def is_odd(n):
    '''
    Return True if n is odd and False if n is even.

    >>> is_odd(0)
    False
    >>> is_odd(1)
    True
    >>> is_odd(2000)
    False
    >>> is_odd(-8)
    False
    >>> is_odd(-9)
    True
    >>> type(is_odd(0))
    <class 'bool'>
    '''


def absolute_value(n):
    '''
    Return the absolute value of n.

    HINT:
    Use an if statement.

    >>> absolute_value(5)
    5
    >>> absolute_value(-5)
    5
    >>> absolute_value(5.5)
    5.5
    >>> absolute_value(-5.5)
    5.5
    '''


def max_num(a, b):
    '''
    Return the maximum of a and b.

    HINT:
    Use an if statement.

    >>> max_num(4, 5)
    5
    >>> max_num(5, 4)
    5
    >>> max_num(-4, -5)
    -4
    >>> max_num(4, 4)
    4
    '''


def max_num_4(a, b, c, d):
    '''
    Return the maximum of a, b, c, and d.

    HINT:
    Use many if statements.

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


def max_num_abs(a, b):
    '''
    Return the number with the highest absolute value.

    HINT:
    Use an if statement, but be careful about the condition.

    >>> max_num_abs(4,5)
    5
    >>> max_num_abs(4,5)
    5
    >>> max_num_abs(-4,-5)
    -5
    >>> max_num_abs(4,4)
    4
    '''


def is_leap_year(n):
    '''
    Return True if n is a leap year and False otherwise.

    HINT:
    The formula for calculating leap years is more complicated than you might think.
    You can find the formula at <https://www.mathsisfun.com/leap-years.html>.

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


def num_digits(n):
    '''
    Return the number of digits in the input n.

    NOTE:
    A negative sign does not count as a digit,
    only numbers do.

    HINT:
    Use a while loop.
    In each iteration, divide the number by 10 to reduce the number of digits by 1.

    HINT:
    This function is implemented in one of your quiz practice problems.

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
    '''


def factorial(n):
    '''
    Return the factorial of n.
    Recall that the factorial of n is defined to be: 1*2*3*...*(n-1)*n

    HINT:
    Use a for loop from 1 to n.
    On each iteration, multiply the current result by the current iteration number.

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
    Return True if n is prime, and False otherwise.
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
    Return True if n is is the product of two integers.
    That is, return True if there exists an integer i such that i*i==n.

    HINT:
    Use a for loop to check each number i between 0 and n.

    >>> is_perfect_square(1)
    True
    >>> is_perfect_square(2)
    False
    >>> is_perfect_square(4)
    True
    >>> is_perfect_square(81)
    True
    >>> is_perfect_square(97)
    False
    >>> is_perfect_square(0)
    True
    >>> is_perfect_square(-144)
    False
    >>> is_perfect_square(144)
    True
    '''


def fibonacci(n):
    '''
    Return the nth fibonacci number.
    Recall that the fibonacci numbers are calculated by the following formula:

        fibonacci(0) = 0
        fibonacci(1) = 1
        fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

    HINT:
    The following "pseudocode" describes how to calculate the nth fibonacci number:

    Let f0 = 0
    Let f1 = 1
    In a for loop from 0 to n,
        Let fn = f0 + f1
        Let f0 = f1
        Let f1 = fn


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
    '''


################################################################################
# The problems below use all the same techniques as the problems above.
# But they don't contain any hints about how to solve them.
# So you will have to figure out for yourself when to use if/for/while statements.
################################################################################


def cigar_party(cigars, is_weekend):
    '''
    When squirrels get together for a party, they like to have cigars.
    A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
    Unless it is the weekend, in which case there is no upper bound on the number of cigars.
    Return True if the party with the given values is successful, or False otherwise.

    >>> cigar_party(30, False)
    False
    >>> cigar_party(50, False)
    True
    >>> cigar_party(70, True)
    True
    >>> cigar_party(10, True)
    False
    >>> cigar_party(40, False)
    True
    '''


def speeding_fine(speed, birthday):
    '''
    The police department needs a function that computes the size of a fine to give to someone pulled over for speeding,
    and its your job to translate the law into code to implement this function.

    The law states that:
    if the speed was 60 or less, the fine is 0 dollars.
    If the speed is between 61-80 inclusive, the fine is 100 dollars.
    And if the speed is greater than 80, the fine is 2000 dollars.
    The law has a strange provision, however, that when it is someone's birthday they are allowed to drive 5 mph faster in all cases.

    >>> speeding_fine(60, False)
    0
    >>> speeding_fine(60, True)
    0
    >>> speeding_fine(61, False)
    100
    >>> speeding_fine(61, True)
    0
    >>> speeding_fine(65, True)
    0
    >>> speeding_fine(80, True)
    100
    >>> speeding_fine(81, True)
    100
    >>> speeding_fine(86, True)
    2000
    >>> speeding_fine(81, False)
    2000
    >>> speeding_fine(101, True)
    2000
    >>> speeding_fine(90, False)
    2000
    '''


def near_ten(x):
    '''
    Return True if num is within 2 of a multiple of 10.

    >>> near_ten(10)
    True
    >>> near_ten(6)
    False
    >>> near_ten(8)
    True
    >>> near_ten(19)
    True
    >>> near_ten(78921)
    True
    >>> near_ten(-43)
    False
    >>> near_ten(-42)
    True
    '''


def love6(a, b):
    '''
    The number 6 is a truly great number.
    Return True if:
    either input number equals 6 or their sum or difference is 6.

    >>> love6(6, 5)
    True
    >>> love6(4, 5)
    False
    >>> love6(3, 3)
    True
    >>> love6(3, 2)
    False
    >>> love6(-3, 3)
    True
    >>> love6(10, 4)
    True
    >>> love6(121, 5)
    False
    >>> love6(-3, -3)
    False
    >>> love6(123, 6)
    True
    '''


def funny_sum(a, b, c):
    '''
    Return the sum of the input values.
    However, if one of the values is the same as another of the values, it does not count towards the sum.

    >>> funny_sum(1, 2, 3)
    6
    >>> funny_sum(3, 2, 3)
    2
    >>> funny_sum(3, 3, 3)
    0
    >>> funny_sum(3, 2, -3)
    2
    >>> funny_sum(3, 3, -3)
    -3
    >>> funny_sum(1, 3, 3)
    1
    >>> funny_sum(3, 3, 2)
    2
    >>> funny_sum(3, 2, 1)
    6
    >>> funny_sum(5, 2, 6)
    13
    '''


def median(a, b, c):
    '''
    Given 3 int values, return the value in the middle.

    >>> median(1, 2, 3)
    2
    >>> median(2, 1, 3)
    2
    >>> median(3, 1, 2)
    2
    >>> median(2, 2, 1)
    2
    >>> median(5, 4, 4)
    4
    >>> median(-3, -2, 7)
    -2
    '''


def sum_between(a, b):
    '''
    Find the sum of all numbers between a and b inclusive.

    >>> sum_between(1, 2)
    3
    >>> sum_between(1, 3)
    6
    >>> sum_between(1, 5)
    15
    >>> sum_between(2, 1)
    3
    >>> sum_between(-5, 5)
    0
    >>> sum_between(5, 10)
    45
    >>> sum_between(1000, 10000)
    49505500
    >>> sum_between(10, -1000)
    -500445
    >>> sum_between(0, 123456)
    7620753696
    '''
