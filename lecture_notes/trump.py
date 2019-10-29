import json

# load the files
filenames=[
    'condensed_2009.json',
    'condensed_2010.json',
    'condensed_2011.json',
    'condensed_2012.json',
    'condensed_2013.json',
    'condensed_2014.json',
    'condensed_2015.json',
    'condensed_2016.json',
    'condensed_2017.json',
    'condensed_2018.json',
    ]
tweets=[]
for filename in filenames:
    with open(filename,'r') as f:
        text=f.read()
        tweets+=json.loads(text)
print('len(tweets)=',len(tweets))

# count the occurrences of each tweet
counts={
    'obama':0,
    'trump':0,
    'daca':0,
    'wall':0,
    'russia':0,
    'mexico':0,
    'fake news':0,
    'mainstream media':0,
    }
for tweet in tweets:
    for phrase in counts.keys():
        if phrase in tweet['text'].lower():
            counts[phrase]+=1
print('counts=',counts)

# print the results
print('percentage of tweets using phrase:')
for k in sorted(counts.keys()):
    print(k.rjust(18), ':', '%05.2f'%(100*counts[k]/len(tweets)))
