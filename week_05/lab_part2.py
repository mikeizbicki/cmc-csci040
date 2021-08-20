'''
INSTRUCTIONS: Implement each function below so that the doctests all pass.
'''

"""
def is_palindrome(s):
    '''
    returns True if a string is the same read forwards and backwards, False otherwise

    HINT:
    use the .reverse() method to reverse the input list s, and == to compare

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

"""
def remove_duplicate_words(s):
    '''
    This function performs a basic grammar check by removing duplicate words in a string.

    HINT:
    use the split function to "tokenize" the string into a list of words;
    then solve the problem on lists using the `remove_duplicates_from_list` function;
    finally, use the join function to convert the de-duplicated list back into a string

        >>> remove_duplicate_words('please please please please work')
        'please work'
        >>> remove_duplicate_words('this is a a sentence')
        'this is a sentence'
        >>> remove_duplicate_words('if it walks like a duck and talks like a duck, then it is a duck')
        'if it walks like a duck and talks like a duck, then it is a duck'
        >>> remove_duplicate_words('nothing needs to change about this sentence')
        'nothing needs to change about this sentence'
    '''
    a = s.split()
    b = remove_duplicates_from_list(a)
    return ' '.join(b)


def remove_duplicates_from_list(lst):
    '''
    This function is a "helper function" for the remove_duplicate_words function;
    having helper functions is a common pattern in python programming

    HINT:
    step 1: create an empty list;
    step 2: then use a for loop to loop over lst;
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

    new_list = []
    for i in range(len(lst)):
        if i < len(lst)-1:
            if lst[i] != lst[i+1]:
                string += 'a'
                new_list.append(lst[i])
        else:
            new_list.append(lst[i])
    return new_list

"""
def how_many_claremonts_in_str(s):
    '''
    returns the number of times the string 'Claremont' appears in s

    HINT:
    there is a built in string function that already implements this method;
    you can find this method listed in the Python Cheatsheet under the section
    "Generic Operations on Containers"

        >>> how_many_claremonts_in_str('This sentence is about Montclair.')
        0
        >>> how_many_claremonts_in_str('This sentence is about Claremont.')
        1
        >>> how_many_claremonts_in_str('Claremont. Claremont. Claremont. Claremont!')
        4
    '''
"""