#!/usr/bin/python3

'''
A wget program is a program that "gets" something from the "w"eb,
and saves it to the local computer.
It is the "hello world" of web programming.
'''

# if you want to use requests, you must run pip install
import requests

# schema://do.ma.in/path
url = 'https://www.gutenberg.org/files/345/345-h/345-h.htm'
filename = 'dracula.html'

# download the url
r = requests.get(url)
if r.status_code == 404:    # the URL is not found
    print('ERROR 404')
elif r.status_code == 503:  # you don't have permission to access the URL
    pass
elif r.status_code == 200:  # success
    text = r.text

    # when we open an incorrect file, python gave us an error message;
    # but when we open an incorrect url, python sometimes does and sometimes does not give us an error

    # save the file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
