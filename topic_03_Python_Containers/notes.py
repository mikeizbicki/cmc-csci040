def largest(xs):
    '''
    Return the largest element in a list.

    >>> largest([1,2,3])
    3
    >>> largest([99,-56,80,100,90])
    100
    >>> largest(list(range(0,100)))
    99
    >>> largest([10])
    10
    >>> largest([])
    '''


def largest3(xs):
    '''
    Return the largest 3 elements in a list in sorted order.

    >>> largest3([1,2,3])
    [1, 2, 3]
    >>> largest3([99,-56,80,100,90])
    [90, 99, 100]
    >>> largest3(list(range(0,100)))
    [97, 98, 99]
    >>> largest3([10])
    [10]
    >>> largest3([])
    []
    '''


def filter_odd(xs):
    '''
    Return a list with all the odd elements removed.

    HINT:
    Use the accumulator pattern with a for loop.

    >>> filter_odd([2,4,6])
    [2, 4, 6]
    >>> filter_odd([1,3,5])
    []
    >>> filter_odd([4,5,6,7])
    [4, 6]
    >>> filter_odd([20,13,4,16,8,19,10])
    [20, 4, 16, 8, 10]
    '''


def nested_filter_odd(xss):
    '''
    Convert a list of lists into a single list that contains only the even elements.

    >>> nested_filter_odd([[2, 4, 5], [1, 3, 6]])
    [2, 4, 6]
    >>> nested_filter_odd([[1, 3, 6]])
    [6]
    >>> nested_filter_odd([[4, 5], [6, 7]])
    [4, 6]
    >>> nested_filter_odd([[20],[13,4,16,8,19],[10], [15, 13, 1]])
    [20, 4, 16, 8, 10]
    '''


# These dictionaries store the grades of famous people in their math, english, and economics classes.
# You shouldn't modify these dictionaries,
# they are used in the doctests for the functions below.
math_grades={
        'donald knuth':85,
        'hypatia':75,
        'emmy noether':86,
        'leonhard euler':92,
        'grigori perelman':95,
        'alexander grothendieck':95,
        'shelton cooper':72,
        'ada lovelace':96,
        }

english_grades={
        'emily dickenson':92,
        'edgar allan poe':88,
        'william shakespeare':84,
        'robert frost':83,
        'dorthy day':95,
        'douglas adams':42,
        'maya angelou':89,
        'emma goldman':85,
        }

economics_grades={
        'christine lagarde':85,
        'alan greenspan':92,
        'adam smith':88,
        'kristalina georgieva':79,
        'karl marx':90,
        'pierre-joseph proudhon':95,
        }


def get_number_of_students_in_class(d):
    '''
    Return the total number of entries in the dictionary.

    >>> get_number_of_students_in_class(math_grades)
    8
    >>> get_number_of_students_in_class(english_grades)
    8
    >>> get_number_of_students_in_class(economics_grades)
    6
    '''


def highest_grade(d):
    '''
    Return the largest value.

    >>> highest_grade(math_grades)
    96
    >>> highest_grade(english_grades)
    95
    >>> highest_grade(economics_grades)
    95
    '''
