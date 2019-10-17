'''
THIS LAB IS OPTIONAL.

If you complete this lab, you will receive 10 points of extra credit on your lab assignment category.
You must have all the test cases working to receive the extra credit.
'''

import re
import requests

def extract_emails(url):
    '''
    This function downloads a URL and returns a list containing the email addresses present within the HTML page.
    The list of URLs must be sorted alphabetically and not contain any duplicates.

    HINT:
    Use the requests library to download the url.
    Follow the instructions in this link to use regular expressions to extract email addresses from the returned text: https://www.tutorialspoint.com/Extracting-email-addresses-using-regular-expressions-in-Python

        >>> extract_emails('https://www.cmc.edu/math')
        ['pbarkley@cmc.edu', 'snelsom@cmc.edu', 'snelson@cmc.edu']
        >>> extract_emails('https://www.cmc.edu/robert-day-school')
        ['elizabeth.valadez@claremontmckenna.edu']
        >>> extract_emails('https://www.cmc.edu/government')
        []
    '''


################################################################################
# DO NOT MODIFY BELOW THIS LINE
################################################################################

import doctest
doctest.testmod(verbose=True)
