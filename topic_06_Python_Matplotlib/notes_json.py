tweets_str = '''[
    {   "source": "Twitter Web Client", 
        "id_str": "6312794445", 
        "text": "Trump International Tower in Chicago ranked 6th tallest building in world by Council on Tall Buildings & Urban Habitat http://bit.ly/sqvQq", 
        "created_at": "Thu Dec 03 19:39:09 +0000 2009", 
        "retweet_count": 33,
        "favorite_count": 6
    },
    {   "source": "Twitter Web Client", 
        "id_str": "6971079756",
        "text": "From DONALD Trump: Wishing everyone a wonderful holiday & a happy, healthy, prosperous New Year. Let's think like champions in 2010!", 
        "created_at": "Wed Dec 23 17:38:18 +0000 2009",
        "retweet_count": 28,
        "favorite_count": 12
        
    }
]'''

# why do we care?
# we know how to load strings from files
# special type of file called JSON files which contain python code that can be loaded 
# with the json.loads function

"""
files = ['data/condensed_2009.json', 'data/condensed_2010.json', 'data/condensed_2011.json' ]
text = ''
for file in files:
    with open(file, encoding='ascii') as f:
        text = f.read()
"""

with open('data/condensed_2016.json', encoding='ascii') as f:
    text = f.read()

import json
tweets = json.loads(text)

num_trumps = 0
for tweet in tweets:
    #if 'Trump' in tweet['text']:
    #if 'Trump' in tweet['text'] or 'trump' in tweet['text'] or 'TRUMP' in tweet['text']:
    #if 'trump' in tweet['text'].lower():
    if tweet['text'].find('trump') != -1:
        num_trumps += 1
print('num_trumps=', num_trumps)


