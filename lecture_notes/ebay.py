import requests

url='https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xtools.TRS0&_nkw=tools&_sacat=0'
r=requests.get(url)
html=r.text

from bs4 import BeautifulSoup
bs=BeautifulSoup(html)

spans=bs.find_all(
    'span',
    class_='s-item__price'
    )
for span in spans:
    print('span=',span.text)

titles=bs.find_all(
    'h3',
    class_='s-item__title'
    )
for title in titles:
    print('title=',title.text)

items=bs.find_all(
    'li',
    class_='s-item'
    )
for item in items:
    try:
        price=item.find('span',class_='s-item__price')
        title=item.find('h3',class_='s-item__title')
        print('title=',title.text.lower(),'price=',price.text)
    except:
        print('error parsing item')

print('len(items)=',len(items))
#bs.find_all
#bs.find

#print('html=',html)
