import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
}
r = requests.get('https://www.amazon.com/s?k=hammer&ref=nb_sb_noss_2',headers=headers)
#r = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=hammer&_sacat=0',headers=headers)
print("r.status_code=",r.status_code)
#print("r.text=",r.text)

soup = BeautifulSoup(r.text, 'html.parser')

items = soup.select('div.sg-col-4-of-32.sg-col-4-of-20.sg-col.sg-col-4-of-16.sg-col-4-of-28.s-asin.s-result-item.sg-col-4-of-36.sg-col-4-of-12.sg-col-4-of-24 > .sg-col-inner')

results = []

for item in items:

    print('---')
    titles = item.select('.a-text-normal.a-color-base.a-size-base-plus')

    result = {}

    for title in titles:
        result['title'] = title.text
        print('  title',title.text)
