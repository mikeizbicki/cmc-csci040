'''
INSTRUCTIONS: Implement each function below so that the doctests all pass.
'''

import requests

def how_many_claremonts_in_url(url):
    '''
    returns the number of times the string 'Claremont' appears in the webpage specified by url

    HINT:
    use the requests library and the how_many_claremonts_in_str function from the previous lab

        >>> how_many_claremonts_in_url('https://www.cmc.edu')
        13
        >>> how_many_claremonts_in_url('https://www.hmc.edu')
        2
        >>> how_many_claremonts_in_url('https://www.pitzer.edu')
        6
        >>> how_many_claremonts_in_url('https://www.pomona.edu')
        5
        >>> how_many_claremonts_in_url('https://www.scripps.edu')
        0
    '''

################################################################################
# DO NOT MODIFY BELOW THIS LINE
################################################################################

import doctest
doctest.testmod(verbose=True)
