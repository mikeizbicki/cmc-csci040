#!/bin/env python3

# load the files
import json
filenames=[
    'data/condensed_2009.json',
    'data/condensed_2010.json',
    'data/condensed_2011.json',
    'data/condensed_2012.json',
    'data/condensed_2013.json',
    'data/condensed_2014.json',
    'data/condensed_2015.json',
    'data/condensed_2016.json',
    'data/condensed_2017.json',
    'data/condensed_2018.json',
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
