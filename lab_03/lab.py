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

def sum_of_digits(n):
    '''
    Calculates the sum of each of the digits in the input number n.

    HINT: use a while loop

        >>> sum_of_digits(5)
        5
        >>> sum_of_digits(15)
        6
        >>> sum_of_digits(51)
        6
        >>> sum_of_digits(1234567890)
        45
    '''

def min_of_digits(n):
    '''
    Calculates the smallest digit in the input number n

    HINT: use a while loop

        >>> min_of_digits(1)
        1
        >>> min_of_digits(57)
        5
        >>> min_of_digits(75)
        5
        >>> min_of_digits(571)
        1
        >>> min_of_digits(1234567890)
        0
        >>> min_of_digits(9999999949999)
        4
    '''

def box(n):
    '''
    prints an nxn box of *

    HINT: use nested for loops

        >>> box(0)
        >>> box(1)
        *
        >>> box(2)
        **
        **
        >>> box(5)
        *****
        *****
        *****
        *****
        *****
        >>> box(15)
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
        ***************
    '''

def checkers(n):
    '''
    prints a "checkers board," which is an nxn box where every other element is a space

    HINT: use nested for loops

        >>> checkers(0)
        >>> checkers(1)
        *
        >>> checkers(2)
        * 
         *
        >>> checkers(5)
        * * *
         * * 
        * * *
         * * 
        * * *
        >>> checkers(15)
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
         * * * * * * * 
        * * * * * * * *
    '''

def outline(n):
    '''
    prints the outline of a box, leaving the middle empty

    HINT: use nested for loops

        >>> outline(0)
        >>> outline(1)
        *
        >>> outline(2)
        **
        **
        >>> outline(5)
        *****
        *   *
        *   *
        *   *
        *****
        >>> outline(15)
        ***************
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        *             *
        ***************
    '''

def fizz_buzz(n):
    '''
    for each number between 1 and n:
        if the number is a multiple of 3, print 'Fizz',
        if the number is a multiple of 5, print 'Buzz',
        if the number is a multiple of both 3 and 5 print 'FizzBuzz',
        if the number is not a multiple of either 3 or 5, print the number

    This is a famous coding interview question inspired by this blog post:
    https://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/

    NOTE:
    Since this function has many outputs, you do not use the `return` statement to output your results.
    Instead, you should use the `print` function directly inside of a for loop.

        >>> fizz_buzz(50)
        1
        2
        Fizz
        4
        Buzz
        Fizz
        7
        8
        Fizz
        Buzz
        11
        Fizz
        13
        14
        FizzBuzz
        16
        17
        Fizz
        19
        Buzz
        Fizz
        22
        23
        Fizz
        Buzz
        26
        Fizz
        28
        29
        FizzBuzz
        31
        32
        Fizz
        34
        Buzz
        Fizz
        37
        38
        Fizz
        Buzz
        41
        Fizz
        43
        44
        FizzBuzz
        46
        47
        Fizz
        49
        Buzz
    '''


# DO NOT MODIFY BELOW THIS LINE
import doctest
doctest.testmod(verbose=True)
