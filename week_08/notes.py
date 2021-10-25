
################################################################################
# PART I: loading text
################################################################################

# So far, we've seen 2 methods to get text into our python programs:

# Method 1: String literals
text1 = '<title>The Project Gutenberg eBook of Dracula, by Bram Stoker</title>'

# Method 2: Files
filename = 'dracula.html'
with open(filename, 'r', encoding='utf-8') as f:
    text2 = f.read()

# Method 3: Requests
import requests
url = 'https://www.gutenberg.org/files/345/345-h/345-h.htm'
r = requests.get(url)
text3 = r.text

# Method 4: Argparse
# No sample code since it won't make sense for this example

################################################################################
# PART II: processing text
################################################################################

# Specify which data source we're going to work with
text = text2

# So far, we've seen 2 methods of processing text:

# Method I: str functions
# for example, 
#   str.replace()
#   str.lower()
#   str.find()
#   slices
#   indexing
text = text.replace('Dracula', 'Izbicki')

# Method II: json.loads
# It should be "obvious" why the following code doesn't work.
'''
data = json.loads(text)
'''

# Today, we are going to learn a 3rd way: the `bs4` library.
# This library makes html strings searchable using css selectors.
# `bs4` is not built-in to python, and you must pip install it.
from bs4 import BeautifulSoup
soup = BeautifulSoup(text, 'html.parser')
a_tags = soup.select('a')

################################################################################
# IMPORTANT:
################################################################################

# Which loading method you choose depends only on where your data is located,
# and not what you want to do with the data.
# Which processing method you choose depends only on what you want to do with that data,
# and not where that data is located.

# Why?
# Each loading gives you a `str` object in python.
# Once you have that `str`,
# you can do any type of processing on it no matter where it came from.

