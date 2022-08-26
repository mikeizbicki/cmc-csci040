import os
if os.path.exists('file'):
    with open('file') as f:
        text = f.read()
# General Principle:
# It's better to ask for forgiveness than permission

try:
    with open('does not exist') as f:
        text = f.read()
    print('text=', text)
except FileNotFoundError:
    print('file not found')

'''
try:
    print('text=', text)
except NameError:
    pass
'''

import requests
url='https://google.comadasdasdas'
try:
    requests.get(url)
except requests.exceptions.MissingSchema:
    print('missing schema')
except requests.exceptions.ConnectionError:
    print('connection error')


'''
try:
    requests.get(url)
except requests.exceptions.MissingSchema:
    print('missing schema')
    '''