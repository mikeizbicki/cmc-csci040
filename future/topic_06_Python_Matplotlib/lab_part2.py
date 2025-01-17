#!/bin/python

'''
Lab instructions: 
Complete each function below so that all doctests pass.
You can run the doctess with the command

$ python3 -m doctest --verbose lab.py

Once all doctests pass, upload the output of the above command to sakai.
'''

def is_palindrome(s):
    '''
    returns True if a string is the same read forwards and backwards, False otherwise

    HINT:
    Use a specially crafted slice to reverse the string s,
    then check to see if s is equal to its reverse.

    >>> is_palindrome('asdsa')
    True
    >>> is_palindrome('asdasd')
    False
    >>> is_palindrome('taco cat')
    False
    >>> is_palindrome('qwertyuiopoiuytrewq')
    True
    >>> is_palindrome('')
    True
    '''


def is_palindrome_number(n):
    '''
    returns True if the digits of the input number form a palindrome

    HINT: 
    convert the number into a string and use your is_palindrome function

    >>> is_palindrome_number(12321)
    True
    >>> is_palindrome_number(123212321)
    True
    >>> is_palindrome_number(1232123)
    False
    '''


def string_contains_url(s):
    '''
    A URL is any string that starts with either "http://" or "https://",
    and the URL may be either uppercase or lowercase.
    This function returns whether the input string contains a url

    HINT: 
    use the `in` keyword and the lower() function

    >>> string_contains_url('I love computing for the web :)')
    False
    >>> string_contains_url('The course website is located at https://github.com/mikeizbicki/cmc-csci040')
    True
    >>> string_contains_url('The https protocol is more secure than the http protocol.')
    False
    >>> string_contains_url('My favorite website is http://purple.com')
    True
    >>> string_contains_url('HTTP://SIMPSONSWORLD.COM IS THE BEST. WEBSITE. EVER.')
    True
    >>> string_contains_url('HtTPs://SiMpSoNsWoRld.COM Is tHe BesT. WEBSITE. EVER.')
    True
    '''


def extract_TLD(domain):
    '''
    a domain name consists of a series of characters separated by periods;
    the series of letters after the last period is called the top level domain (TLD);
    this function returns the TLD of the input domain

    HINT:
    use the .split() function to "tokenize" the string on the periods

    >>> extract_TLD('www.google.com')
    'com'
    >>> extract_TLD('izbicki.me')
    'me'
    >>> extract_TLD('www.rodong.rep.kp')
    'kp'
    >>> extract_TLD('www.ci.claremont.ca.us')
    'us'
    >>> extract_TLD('research.pizza')
    'pizza'
    '''


def remove_duplicates_from_list(xs):
    '''
    This function is a "helper function" for the remove_duplicate_words function below;
    having helper functions is a common pattern in python programming.

    HINT:
    Use the accumulator pattern as follows:
    step 1: create an empty list;
    step 2: then use a for loop to loop over xs;
    step 3: on each iteration of the for loop, if the value is different than the previous value, then append it to the list you created in step 1

    >>> remove_duplicates_from_list([1,1,2,3,3,1,3,2])
    [1, 2, 3, 1, 3, 2]
    >>> remove_duplicates_from_list([4,2,2,2,2,2,2,3,1,2])
    [4, 2, 3, 1, 2]
    >>> remove_duplicates_from_list([1])
    [1]
    >>> remove_duplicates_from_list([1,1,1,1,1])
    [1]
    >>> remove_duplicates_from_list([])
    []
    '''


def remove_duplicate_words(s):
    '''
    This function performs a basic grammar check by removing duplicate words in a string.

    HINT:
    Don't use the accumulator pattern.
    (This is one of the rare times in class I'll say that.)
    Instead:
    1) use the `.split()` function to convert the string to a list
    2) call the `remove_duplicates_from_list` function
    3) use the `.join()` function to convert the list back to a string

    >>> remove_duplicate_words('please please please please work')
    'please work'
    >>> remove_duplicate_words('this is a a sentence')
    'this is a sentence'
    >>> remove_duplicate_words('if it walks like a duck and talks like a duck, then it is a duck')
    'if it walks like a duck and talks like a duck, then it is a duck'
    >>> remove_duplicate_words('nothing needs to change about this sentence')
    'nothing needs to change about this sentence'
    '''


def how_many_claremonts_in_str(s):
    '''
    returns the number of times the string 'Claremont' appears in s; it is not case sensitive

    HINT:
    there is a built in string function that already implements this method;
    you can find this method listed in the Python Cheatsheet under the section
    "Generic Operations on Containers"

    >>> how_many_claremonts_in_str('This sentence is about Montclair.')
    0
    >>> how_many_claremonts_in_str('This sentence is about Claremont.')
    1
    >>> how_many_claremonts_in_str('THIS SENTENCE IS ABOUT CLAREMONT!')
    1
    >>> how_many_claremonts_in_str('Claremont. Claremont. Claremont. Claremont!')
    4
    >>> how_many_claremonts_in_str('CLAREMONT. claremont. ClaREMonT. Claremont!')
    4
    '''
