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
