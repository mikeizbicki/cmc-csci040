
################################################################################
# PART I: loading text1
################################################################################

# So far, we've seen 2 methods to get text1 into our python programs:

# Method 1: String literals
text1 = '<title>The Project Gutenberg eBook of Dracula, by Bram Stoker</title>'

# Method 2: Files
filename = 'dracula.html'
with open(filename, 'r', encoding='utf-8') as f:
    text2 = f.read()

# Today we will learn 2 more:

# Method 3: From the internet with `requests`
# `requests` is not a built-in module, so you must install it:
# ```
# $ pip3 install requests
# ```
import requests
url = 'https://www.gutenberg.org/files/345/345-h/345-h.htm'
response = requests.get(url)
text3 = response.text

# Method 4: From the command-line with argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--text')
parser.add_argument('--example')
parser.add_argument('--hello')
args = parser.parse_args()
text4 = args.text

print('text4=',text4)
print('args.example=',args.example)

################################################################################
# PART II: processing text
################################################################################

# So far, we've seen 2 methods of processing text:

# Method 1: str functions
# for example, 
#   str.replace()
#   str.lower()
#   str.find()
#   slices
#   indexing
text1 = text1.replace('Dracula', 'Izbicki')

# Method 2: json.loads
# It should be "obvious" why the following code doesn't work.
'''
import json
data = json.loads(text1)
'''

# Today, we are going to learn a 3rd way: the `bs4` library.
# This library makes html strings searchable using css selectors.
# `bs4` is not built-in to python, and you must pip install it:
# ```
# $ pip3 install bs4
# ```
from bs4 import BeautifulSoup
#import bs4
soup = BeautifulSoup(text1, 'html.parser')
tags = soup.select('title')

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

