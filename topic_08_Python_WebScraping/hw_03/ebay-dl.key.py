import argparse
import requests
from bs4 import BeautifulSoup
import json

def parse_itemssold(text):
    '''
    Takes as input a string and returns the number of items sold, as specified in the string.

    >>> parse_itemssold('38 sold')
    38
    >>> parse_itemssold('14 watchers')
    0
    >>> parse_itemssold('Almost gone')
    0
    '''
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return 0


def parse_price(text):
    '''
    Returns the price in the input text as an integer number of cents.
    If no price is present, returns 0.

    >>> parse_price('$37.95')
    3795
    >>> parse_price('$54.99 to $79.99')
    5499
    >>> parse_price('Free Shipping')
    0
    '''
    if '$' not in text:
        return 0

    i_dollar = text.find('$')
    i_space = text.find(' ')
    price_text = text[i_dollar:i_space] if i_space != -1 else text[i_dollar:]

    numbers = ''
    for char in price_text:
        if char in '1234567890':
            numbers += char
    return int(numbers)


# this if statement says only run the code below when the python file is run "normally"
# where normally means not in the doctests
if __name__ == '__main__':

    # get command line arguments
    parser = argparse.ArgumentParser(description='Download information from ebay and convert to JSON.')
    parser.add_argument('search_term')
    parser.add_argument('--num_pages', default=10)
    args = parser.parse_args()
    print('args.search_term=', args.search_term)

    # list of all items found in all ebay webpages
    items = []

    # loop over the ebay webpages
    for page_number in range(1,int(args.num_pages)+1):

        # build the url
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' 
        url += args.search_term
        url += '&_sacat=0&LH_TitleDesc=0&_pgn='
        url += str(page_number)
        url += '&rt=nc'
        print('url=',url)

        # download the html
        r = requests.get(url)
        status = r.status_code
        print('status=', status)
        html = r.text

        # process the html
        soup = BeautifulSoup(html, 'html.parser')

        # loop over the items in the page
        tags_items = soup.select('.s-item')
        for tag_item in tags_items:

            name = None
            tags_name = tag_item.select('.s-item__title')
            for tag in tags_name:
                name = tag.text

            status = False
            tags_status = tag_item.select('.SECONDARY_INFO')
            for tag in tags_status:
                status = tag.text

            freereturns = False
            tags_freereturns = tag_item.select('.s-item__free-returns')
            for tag in tags_freereturns:
                freereturns = True

            items_sold = None
            tags_itemssold = tag_item.select('.s-item__hotness')
            for tag in tags_itemssold:
                items_sold = parse_itemssold(tag.text)

            price = None
            tags_price = tag_item.select('.s-item__price')
            for tag in tags_price:
                price = parse_price(tag.text)

            shipping = 0
            tags_shipping = tag_item.select('.s-item__shipping')
            for tag in tags_shipping:
                shipping = parse_price(tag.text)

            item = {
                'name': name,
                'status': status,
                'free_returns': freereturns,
                'items_sold': items_sold,
                'shipping': shipping,
                'price': price,
            }
            items.append(item)
        
        print('len(tags_items)=',len(tags_items))
        print('len(items)=',len(items))

    # write the json to a file
    filename = args.search_term+'.json'
    with open(filename, 'w', encoding='ascii') as f:
        f.write(json.dumps(items))
