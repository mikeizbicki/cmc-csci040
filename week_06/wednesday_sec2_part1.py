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

import json
import pprint
with open('data/master_2018.json', encoding='ascii') as f:
    text = f.read()
    tweets = json.loads(text)

pprint.pprint(tweets[0])

'''
import json
tweets = []
files = ['data/condensed_2016.json', 'data/condensed_2017.json', 'data/condensed_2018.json']
for file in files:
    with open(file, encoding='ascii') as f:
        text = f.read()    
        tweets += json.loads(text)
'''

#with open('data/condensed_2016.json', encoding='ascii') as f:
#    tweets_str = f.read()


#tweets = json.loads(tweets_str)

# how many tweets does Trump mention himself in?
num_trumps = 0
for tweet in tweets:
    # if Trump is talking about Trump:
    #if 'TRUMP' in tweet['text'] or 'trump' in tweet['text'] or 'Trump' in tweet['text']:
    if 'trump' in tweet['text'].lower():
        num_trumps += 1

print('num_trumps =',num_trumps)
print('percent=', num_trumps/len(tweets))

import pprint  # pretty print