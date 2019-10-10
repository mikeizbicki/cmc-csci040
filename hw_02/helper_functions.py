'''
This file contains helper functions for the analyze_url.py script.
Breaking up the code into functions that accomplish small, specific tasks
makes programming large projects much easier and is a common design pattern.
'''

import string
import requests
from bs4 import BeautifulSoup

def get_h1_tag(html):
    '''
    This function takes as input a string containing html.
    It searches the html for the h1 tag,
    and returns the contents of the h1 tag.

    HINT: Use BeautifulSoup

        >>> get_h1_tag('<h1>example</h1>')
        'example'
        >>> get_h1_tag('<body><h1><b>example</b></h1></body>')
        'example'
    '''
    return ''

def download_html(url):
    '''
    This function takes a url as input and returns the html associated with the url.

    WARNING:
    The doctests for this function rely on both the download_html and get_h1_tag functions.
    Therefore, these doctests cannot pass until both functions are correctly implemented.
    Ideally, we would never have the doctests of a function depend on other functions also working correctly,
    but for some functions that have particularly complicated output,
    this is unavoidable.

    HINT: use the requests library to implement this function

        >>> get_h1_tag(download_html('https://en.wikipedia.org/wiki/Laika'))
        'Laika'
    '''
    return 'Sample output.'

def get_p_contents(html):
    r'''
    This function takes as input a string containing html. 
    It searches the html for all p tags,
    and returns the contents of all p tags concatenated into a single string.
    The newline character should be placed between the contents of all p tags.

    HINT: use BeautifulSoup

        >>> get_p_contents('<p>example</p>')
        'example'
        >>> get_p_contents('<p><a href=https://example.com>example</a></p>')
        'example'
        >>> get_p_contents('<p>example</p><div>blah blah blah</div><p>example</p>')
        'example\nexample'
    '''
    return html

def remove_punctuation(text):
    '''
    This function takes as input text and returns a modified version of the string 
    with all punctuation characters removed.

        >>> remove_punctuation('U.S.A.')
        'USA'
        >>> remove_punctuation('My advice: (1) get bigger; (2) get badder; (3) get ugly!')
        'My advice 1 get bigger 2 get badder 3 get ugly'
        >>> remove_punctuation(string.punctuation)
        ''
    '''
    return text

def remove_numbers(text):
    '''
    This function takes as input text and returns a modified version of the string 
    with all numbers removed.
    The function only removes arabic numerals, and does not remove spelled-out numbers.

        >>> remove_numbers('1234567890')
        ''
        >>> remove_numbers('one')
        'one'
        >>> remove_numbers('MMXIX')
        'MMXIX'
        >>> remove_numbers('p4ssw0rd')
        'psswrd'
    '''
    return text

def remove_newlines(text):
    r'''
    This function takes as input text and returns a modified version of the string 
    with all newline characters '\n' replaced with a space ' '.

        >>> remove_newlines('this\nis\na\ntest')
        'this is a test'
    '''
    return text


stop_words=['','i','me','my','myself','we','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now','could','would','how','many']

def remove_stop_words(text):
    '''
    This function takes as input text and returns a modified version of the string 
    with all stop words removed.
    Stop words are simple English words that appear very often in text no matter
    what the subject is,
    and so they would look like noise in our analysis.

        >>> remove_stop_words('How much wood would a woodchuck chuck if a woodchuck could chuck wood?')
        'much wood woodchuck chuck woodchuck chuck wood?'
        >>> remove_stop_words('If Peter Piper picked a peck of pickled peppers, how many pickled peppers did Peter Piper pick?')
        'Peter Piper picked peck pickled peppers, pickled peppers Peter Piper pick?'
    '''
    return text

def count_words(text):
    '''
    This function takes as input a string and returns a dictionary.
    The keys in the dictionary are the words in the input,
    and the values are the number of times the word appeared in the input.
    All keys are stored in lower case, 
    and the case of the words in the original text is ignored.

    WARNING: 
    Functions that output dictionaries need to be wrapped within the built-in pprint function for the doctests to work.
    This is because be default, python prints dictionaries in a non-deterministic ordering,
    but pprint ensures that the order is sorted alphabetically.
    For details, see https://stackoverflow.com/questions/15549429/how-do-i-test-dictionary-equality-with-pythons-doctest-package

        >>> pprint(count_words('a a B B B B c C a A a A ddDdd'))
        {'a': 6, 'b': 4, 'c': 2, 'ddddd': 1}
    '''
    return {}

def get_top_k_words(counts_dict,k):
    '''
    The counts_dict variable is a dictionary whose values are integers,
    and the k variable is an integer.
    The return value is another dictionary whose entries are the k entries
    of counts_dict with the largest values.

    HINT:
    Python has a built in function called nlargest within the heapq module.
    This function takes as input a list and returns the nth-largest value of the list.
    You can find detailed documentation at https://docs.python.org/2/library/heapq.html

    You can implement get_top_k_words by:
    Step 1: use heapq.nlargest to find the k-th largest value within counts_dict
    Step 2: remove all values in counts_dict less than the value from step 1

    WARNING:
    See the warning for count_words

        >>> pprint(get_top_k_words({'b': 4, 'c': 2, 'a': 6, 'ddddd': 1}, 1))
        {'a': 6}
        >>> pprint(get_top_k_words({'b': 4, 'c': 2, 'a': 6, 'ddddd': 1}, 2))
        {'a': 6, 'b': 4}
        >>> pprint(get_top_k_words({'b': 4, 'c': 2, 'a': 6, 'ddddd': 1}, 10))
        {'a': 6, 'b': 4, 'c': 2, 'ddddd': 1}
    '''
    return counts_dict
    
def print_dictionary(d):
    '''
    This function prints the keys and values of the dictionary with each key on its own line.

    EXTRA CREDIT:
    You can receive up to 5 points of extra credit on this problem by completing two tasks:
    First, print the keys sorted by value from highest to lowest.
    Second, ensure that all of the printed values are horizontally aligned.
    For example, the output like the following would earn the extra credit:

        laika      : 33
        space      : 21
        soviet     : 19
        dogs       : 16
        dog        : 12
        sputnik    : 12

    Output like the following is also acceptable for full credit, but would not earn extra credit:

        sputnik : 12
        space : 21
        dog : 12
        soviet : 19
        laika : 33
        dogs : 16
    '''

if __name__=='__main__':
    from pprint import pprint
    import doctest
    doctest.testmod(verbose=True)
