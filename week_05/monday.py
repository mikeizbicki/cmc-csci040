with open('monday.json','r') as input_file:
    text = input_file.read()

text = '''
[
    {   "source": "Twitter Web Client", 
        "id_str": "6312794445", 
        "text": "Trump International Tower in Chicago ranked 6th tallest building in world by Council on Tall Buildings & Urban Habitat http://bit.ly/sqvQq", 
        "created_at": "Thu Dec 03 19:39:09 +0000 2009", 
        "retweet_count": 33,
        "favorite_count": 6, 
        "is_retweet": false
    },
    {   "source": "Twitter Web Client", 
        "id_str": "6971079756", 
        "is_retweet": false,
        "text": "From DONALD Trump: Wishing everyone a wonderful holiday & a happy, healthy, prosperous New Year. Let's think like champions in 2010!", 
        "created_at": "Wed Dec 23 17:38:18 +0000 2009",
        "retweet_count": 28,
        "favorite_count": 12
        
    }
]
'''

#print('text=',text)

import json
tweets = json.loads(text)



#print('retweets = ', text[0])

terms = ['donald', 'trump', 'obama', 'syria']

term_counts = {}
for term in terms:
    term_counts[term] = 0

num_donalds = 0
num_trumps = 0

for tweet in tweets:
    print('retweet_count =', tweet['text'])
    if 'donald' in tweet['text'].lower():
        num_donalds += 1
    if 'trump' in tweet['text'].lower():
        num_trumps += 1

    for term in terms:
        if term in tweet['text'].lower():
            term_counts[term] += 1

print('num_donalds = ', num_donalds)
print('num_trumps = ', num_trumps)

for term in terms:
    print('num',term,'=',term_counts[term])

#print('retweets = ', tweets[1]['retweet_count'])
