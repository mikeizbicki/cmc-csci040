#!/usr/bin/python3

'''
A wget program is a program that "gets" something from the "w"eb,
and saves it to the local computer.
It is the "hello world" of web programming.
'''

import requests

url = 'https://www.gutenberg.org/files/345/345-h/345-h.htm'
filename = 'dracula.html'

# download the url
r = requests.get(url)
text = r.text

# save the file
with open(filename, 'w', encoding='utf-8') as f:
    f.write(text)
