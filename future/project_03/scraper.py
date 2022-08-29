import requests
from bs4 import BeautifulSoup

# selenium

keyword='drill'
page_number='5'
results = []

headers = {
    'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
}

for i in range(10):
    #r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword, headers=headers)
    r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn='+str(i+1), headers=headers)
    print('r.status_code=',r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')

    #print('r.text=',r.text)

    '''
    #items = soup.select('.a-text-normal.a-color-base.a-size-base-plus')
    items = soup.select('li.s-item--watch-at-corner.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__link > .s-item__title')
    #items = soup.select('a')
    for item in items:
        print('item=',item.text)

    prices = soup.select('.s-item__price')
    for price in prices:
        print('price=',price.text)
    '''

    # extract the "item boxes" rather than just the titles/prices
    boxes = soup.select('li.s-item--watch-at-corner.s-item')
    for box in boxes:
        #print('---')
        result = {}
        titles = box.select('li.s-item--watch-at-corner.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__link > .s-item__title')
        for title in titles:
            #print('title=',title.text)
            result['title'] = title.text
        prices = box.select('.s-item__price')
        for price in prices:
            #print('price=',price.text)
            result['price'] = price.text
        #print('result=',result)
        results.append(result)


    print('len(results)=',len(results))

# 3 last steps:
# 1) not just 1 webpage, but the top 10 results pages
# 2) not just the item title and price, but also it's "status"
# 3) output to a json file



import json
j = json.dumps(results)
with open('items.json','w') as f:
    f.write(j)
#print('j=',j)