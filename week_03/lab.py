#!/bin/python

'''
Lab instructions: 
Complete each function below so that all doctests pass.
You can run the doctess with the command

$ python3 -m doctest --verbose lab.py

Once all doctests pass, upload the output of the above command to sakai.
'''


################################################################################
# PART I:
# These functions review the control flow and math operations from last week
################################################################################

"""
def sum_of_digits(n):
    '''
    Calculates the sum of each of the digits in the input number n.
    I gave you the solution for this problem :)

        >>> sum_of_digits(5)
        5
        >>> sum_of_digits(15)
        6
        >>> sum_of_digits(51)
        6
        >>> sum_of_digits(1234567890)
        45
    '''
    total = 0
    while n>0:
        total += n%10
        n //= 10
    return total


def min_of_digits(n):
    '''
    Calculates the smallest digit in the input number n

    HINT: 
    The solution for this function follows a similar format to the solution for `sum_of_digits` above.
    Use a while loop with the `//` and `%` operators.
    The expression `n%10` will give the last digit of the number `n`,
    and the expression `n//10` removes the last digit from the number.

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
"""

################################################################################
# PART Ib:
# You can get 2 points of extra credit on the lab if you complete the 3 functions in this section.
# You must complete all 3 functions in order to get the extra credit.
################################################################################

"""
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
"""


################################################################################
# PART II:
# These functions require you to use python lists.
################################################################################

"""
def filter_even(lst):
    '''
    returns a list with all the even elements removed

        >>> filter_even([1,3,5])
        [1, 3, 5]
        >>> filter_even([2,4,6])
        []
        >>> filter_even([4,5,6,7])
        [5, 7]
        >>> filter_even([20,13,4,16,8,19,10])
        [13, 19]
    '''
"""

def print_list(lst):
    '''
    This function takes a list as input and prints the elements of the list separated by commas with the word 'and' between the second to last and last items.

    HINT:
    You will need to loop over the list and call the `print` function on each item;
    Recall that the `print` function accepts an optional keyword argument `end` that can be used to prevent `print` from printing newlines

        >>> print_list(['apples', 'bananas', 'tofu', 'cats'])
        'apples, bananas, tofu, and cats'
        >>> print_list([1,2,3])
        '1, 2, and 3'
        >>> print_list([True,False])
        'True, and False'
        >>> print_list(['test'])
        'test'
    '''

    """
    string = ''
    #for x in lst:
    for i in range(len(lst)):
        #string += str(x)
        string += str(lst[i])
        if i < len(lst)-1:
            string += ', '
        if i == len(lst)-2:
            string += 'and '
    return string
    """
    print("'", end='')
    for i in range(len(lst)):
        print(lst[i], end='')
        if i < len(lst)-1:
            print(', ', end='')
        if i == len(lst) - 2:
            print('and ', end='')
    print("'")
            

"""
def bigger_than_10(lst):
    '''
    returns the number of elements in the list bigger than 10

        >>> bigger_than_10([])
        0
        >>> bigger_than_10([10])
        0
        >>> bigger_than_10([11,1,12,2,13,3,14,4,15,5])
        5
        >>> bigger_than_10([4,5,6,11])
        1
    '''


def second_largest(lst):
    '''
    returns the second largest element in a list,
    if the list has less than 2 elements, returns None

    HINT:
    Use a for loop;

        >>> second_largest([1,2,3])
        2
        >>> second_largest([99,-56,80,100,90])
        99
        >>> second_largest(list(range(0,100)))
        98
        >>> second_largest([10])
        >>> second_largest([])
    '''


def filter_flatten(lst_of_lst):
    '''
    This function takes as input a list of lists and returns a single list.
    The first element of the returned list is equal to the first element in the first nested list,
    the second element of the returned list is equal to the second element in the second nested list,
    and in general the n-th element of the returned list is equal to the n-th element in the n-th nested list.

    HINT:
    Use nested for loops.

        >>> filter_flatten([[True,False],[False,True]])
        [True, True]
        >>> filter_flatten([[1,2,3],[4,5,6],[7,8,9]])
        [1, 5, 9]
        >>> filter_flatten([['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']])
        ['a', 'f', 'k', 'p']
        >>> filter_flatten([[10]])
        [10]
    '''


def last_three(lst):
    '''
    returns a list containing the last three elements of the input list;
    if the list contains three or fewer elements, then return the entire list

    HINT: use list slices with negative indices

        >>> last_three([0,1,2,3,4,5,6,7,8,9])
        [7, 8, 9]
        >>> last_three(['a','b','c','d'])
        ['b', 'c', 'd']
        >>> last_three([0,1])
        [0, 1]
    '''


################################################################################
# PART III:
# These functions require you to use python dictionaries.
################################################################################


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

# implement the functions below

def get_number_of_students_in_class(d):
    '''
    returns the total number of entries in the dictionary

        >>> get_number_of_students_in_class(math_grades)
        8
        >>> get_number_of_students_in_class(english_grades)
        8
        >>> get_number_of_students_in_class(economics_grades)
        6
    '''
    return len(d)


def student_with_highest_grade(d):
    '''
    returns the key that has the greatest value

        >>> student_with_highest_grade(math_grades)
        'ada lovelace'
        >>> student_with_highest_grade(english_grades)
        'dorthy day'
        >>> student_with_highest_grade(economics_grades)
        'pierre-joseph proudhon'
    '''


def students_getting_an_a(d):
    '''
    returns a list of students whose grade is at least 90;
    that is, it returns all keys whose value is at least 90

    NOTE: 
    The returned list is required to be sorted,
    and this can be achieved by using the list.sort() method.

        >>> students_getting_an_a(math_grades)
        ['ada lovlace', 'alexander grothendieck', 'grigori perelman', 'leonhard euler']
        >>> students_getting_an_a(english_grades)
        ['dorthy day', 'emily dickenson']
        >>> students_getting_an_a(economics_grades)
        ['alan greenspan', 'karl marx', 'pierre-joseph proudhon']
    '''


################################################################################
# PART IV:
# These functions require you to combine both python dictionaries and lists.
################################################################################

# Twitter uses python dictionaries to store the information about each tweet.
# The following list contains real tweets sent by President Trump.
trump_tweets=[
        { "id_str": "947824196909961216", 
          "text": "Will be leaving Florida for Washington (D.C.) today at 4:00 P.M. Much work to be done, but it will be a great New Year!", 
          "created_at": "Mon Jan 01 13:37:52 +0000 2018",
          "retweet_count": 8656, 
          "user":{
            "name":"Donald J. Trump",
            "screen_name":"realdonaldtrump",
            "location":"Washington, DC",
            },
          },
        { "id_str": "947614110082043904", 
          "text": "HAPPY NEW YEAR! We are MAKING AMERICA GREAT AGAIN, and much faster than anyone thought possible!", 
          "created_at": "Sun Dec 31 23:43:04 +0000 2017", 
          "retweet_count": 35394, 
          "user":{
            "name":"Donald J. Trump",
            "screen_name":"realdonaldtrump",
            "location":"Washington, DC",
            },
          }, 
        { "id_str": "947810806430826496", 
          "text": "Iran is failing at every level despite the terrible deal made with them by the Obama Administration. The great Iranian people have been repressed for many years. They are hungry for food &amp; for freedom. Along with human rights, the wealth of Iran is being looted. TIME FOR CHANGE!", 
          "created_at": "Mon Jan 01 12:44:40 +0000 2018", 
          "retweet_count": 15176, 
          "user":{
            "name":"Donald J. Trump",
            "screen_name":"realdonaldtrump",
            "location":"Washington, DC",
            },
          }, 
        { "id_str": "947802588174577664", 
          "text": "The United States has foolishly given Pakistan more than 33 billion dollars in aid over the last 15 years, and they have given us nothing but lies &amp; deceit, thinking of our leaders as fools. They give safe haven to the terrorists we hunt in Afghanistan, with little help. No more!", 
          "created_at": "Mon Jan 01 12:12:00 +0000 2018", 
          "retweet_count": 51483, 
          "user":{
            "name":"Donald J. Trump",
            "screen_name":"realdonaldtrump",
            "location":"Washington, DC",
            },
          }, 
        { "id_str": "947592785519173637", 
          "text": "As our Country rapidly grows stronger and smarter, I want to wish all of my friends, supporters, enemies, haters, and even the very dishonest Fake News Media, a Happy and Healthy New Year. 2018 will be a great year for America!", 
          "created_at": "Sun Dec 31 22:18:20 +0000 2017", 
          "retweet_count": 3969893, 
          "user":{
            "name":"Donald J. Trump",
            "screen_name":"realdonaldtrump",
            "location":"Washington, DC",
            },
          }, 
        ]


def most_retweeted(lst):
    '''
    This function takes as input a list of tweets,
    it inspects these tweets to find the tweet with the highest "retweet_count",
    and returns the "id_str" of that tweet.

        >>> most_retweeted(trump_tweets[:1])
        '947824196909961216'
        >>> most_retweeted(trump_tweets[:2])
        '947614110082043904'
        >>> most_retweeted(trump_tweets[:3])
        '947614110082043904'
        >>> most_retweeted(trump_tweets[:4])
        '947802588174577664'
        >>> most_retweeted(trump_tweets[:5])
        '947592785519173637'
    '''
"""
