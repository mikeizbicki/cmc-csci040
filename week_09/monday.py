import requests
import time
import bs4
from bs4 import BeautifulSoup

url = 'https://google.com'
url = 'https://raw.githubusercontent.com/mikeizbicki/cmc-csci040/2020fall/README.md'
url = 'https://raw.githubusercontent.com/mikeizbicki/cmc-csci040/2020fall/READ'
#url = 'https://github.com/mikeizbicki/cmc-csci040/blob/2020fall/READ'
url = 'githubasdhgvhjgvjgjgccjvcjcj.com/mikeizbicki/cmc-csci040/blob/2020fall/READ'
url = 'https://github.com/ytdl-org/youtube-dl/'
url = 'https://www.reddit.com/r/csci040temp/.json'
url = 'https://izbicki.me'

# reddit can temporarily ban people based on their "user agent"
# the user agent is like the "name" of your web browser

headers = {
    'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
}

try:
    r = requests.get(url, headers=headers)
    r.status_code       # debugging information
    r.text              # contains the actual text of the webpage; 

    print('r.status_code=',r.status_code)
    print('r.text=',r.text[:20])

    if r.status_code==200:
        with open('webpage.html','wt') as f:
            f.write(r.text)

        soup = BeautifulSoup(r.text, 'html.parser')

        a_tags = soup.select('a')
        for a_tag in a_tags:
            print('a_tag=',a_tag)
        '''
        if 'izbicki' in r.text.lower():
            print('contains izbicki')
        else:
            print('does not contain izbicki')
        # know that r.text contains the webpage's information
        '''
    else:
        if r.status_code==429: # try again l ater
            time.sleep(500)
            r = requests.get(url)
        # handle whatever bad thing happened

    # if r.status_code == 200, then everything worked correctly
    # every other status code means something "bad" happened

except requests.exceptions.ConnectionError:
    print('bad url, url=',url)

except requests.exceptions.InvalidSchema:
    print('invalid shema in url, url=',url)

except requests.exceptions.MissingSchema:
    print('the url needs a schema, url=',url)