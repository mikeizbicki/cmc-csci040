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
#tweets = json.loads(tweets_str)
'''
with open('data/condensed_2009.json', 'rb') as f:
    text = f.read()
    text = text.decode('utf-8')
    tweets = json.loads(text)
'''

paths = ['data/condensed_2009.json', 'data/condensed_2010.json', 'data/condensed_2011.json']
tweets = []
for path in paths:
    with open(path, encoding='ascii') as f:
        text = f.read()
        tweets += json.loads(text)

num_tweets = 0
output_tweets = []
for tweet in tweets:
    #if 'Trump' in tweet['text'] or 'trump' in tweet['text'] or 'TRUMP' in tweet['text'] or 'TrUmP' in tweet['text']:
    if 'trump' in tweet['text'].lower() and 'chicago' in tweet['text'].lower():
    # INCORRECT: if 'chicago' and ('trump' in tweet['text'].lower()):
    #if ('chicago' and 'trump') in tweet['text'].lower():
        num_tweets += 1
        output_tweets.append(tweet)
    #else:
    #    print('tweet["text"]=',tweet['text'])
print('num_tweets=',num_tweets)
print('len(tweets)=', len(tweets))

#first_output_tweet = output_tweets[0]
#print('first_output_tweet=',first_output_tweet)