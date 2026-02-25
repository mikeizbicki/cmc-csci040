
################################################################################
# PART I: loading text1
################################################################################

# So far, we've seen 2 methods to get text1 into our python programs:

# Method 1: String literals
text1 = '<div><b>this is HTML</b> inside a <em>Python String!</em></div>'

# **Important:**
# HTML/Markdown/Python files are all just text.
# The contents of these files can always be stored in a string!

# Method 2: Files
filename = 'README.md'
with open(filename, 'r', encoding='utf-8') as f:
    text2 = f.read()

# Today we will learn 2 more methods:

# Method 3: From the command-line with argparse
#
# argparse is built-in module;
# there is no need to install anything to use it
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--text')
parser.add_argument('--example')
parser.add_argument('--hello')
args = parser.parse_args()
text3 = args.text

# Method 4: From the internet with `requests`
#
# `requests` is not a built-in module, so you must install it:
# ```
# $ pip3 install requests
# ```
import requests
url = 'https://www.gutenberg.org/files/345/345-h/345-h.htm'
response = requests.get(url)
text4 = response.text

################################################################################
# PART II: processing text
################################################################################

# So far, we've seen lots of string functions for processing text
# for example:
#   str.replace()
#   str.lower()
#   str.find()
#   slices
#   indexing

# Today we will learn 2 more methods:

# Method 1: working with JSON files
# JSON is like python lists/dictionaries only
jsontext = """
[
    { "text": "hello", "username": "Trump" },
    { "text": "world", "username": "Obama" },
    { "text": "hola", "username": "Obama" },
    { "text": "mundo", "username": "Trump" }
]
"""
import json # built-in to python
data = json.loads(jsontext)

# Method 2:
# This library makes html strings searchable using css selectors.
# `bs4` is not built-in to python, and you must pip install it:
# ```
# $ pip3 install bs4
# ```
text1 = '<div><b>this is HTML</b> inside a <em>Python <b>String!</b></em></div>'
from bs4 import BeautifulSoup
soup = BeautifulSoup(text1, 'html.parser')
tags = soup.select('b')

# It is technically allowed to import bs4 like below,
# but nobody does it in practice.
# Very "unpythonic"!
import bs4
soup = bs4.BeautifulSoup(text1, 'html.parser')

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

