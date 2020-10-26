'''
INSTRUCTIONS: Implement each function below so that the doctests all pass.
'''


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


def how_many_claremonts_in_url(url):
    '''
    returns the number of times the string 'Claremont' appears in the webpage specified by url

    HINT:
    use the requests library and the how_many_claremonts_in_str function

    WARNING:
    these values can change over time as the webpages get updated;
    the current values listed are correct for Monday, 26 October;
    I will update these values for the lab on the day of the lab

        >>> how_many_claremonts_in_url('https://www.cmc.edu')
        29
        >>> how_many_claremonts_in_url('https://www.hmc.edu')
        4
        >>> how_many_claremonts_in_url('https://www.pitzer.edu')
        12
        >>> how_many_claremonts_in_url('https://www.pomona.edu')
        7
        >>> how_many_claremonts_in_url('https://www.scripps.edu')
        0
    '''
