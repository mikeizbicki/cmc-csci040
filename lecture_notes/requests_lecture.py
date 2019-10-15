print('hello world')

import requests

webpage=requests.get('https://en.wikipedia.org/wiki/Guido_van_Rossum')

from bs4 import BeautifulSoup

bs=BeautifulSoup(webpage.text)
print('text=',bs.text)
