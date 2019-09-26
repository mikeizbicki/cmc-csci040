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


# DO NOT MODIFY BELOW THIS LINE
import doctest
doctest.testmod(verbose=True)
