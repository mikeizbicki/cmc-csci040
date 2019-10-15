# ctrl+d leaves python
# pip3 install requests

import requests

# pip3 install bs4
#import bs4
from bs4 import BeautifulSoup

html='''
<title>example</title>
<p>this is an example.
<p>also an example.
<ol>
<li><a href='ur1'>elem1</a></li>
<li><a href='ur2'>elem2</a></li>
<li><a href='ur3'>elem3</a></li>
</ol>
'''

bs=BeautifulSoup(html)

for a in bs.find_all('a'):
    print('a.attrs=',a.attrs)
