import json
import matplotlib.pyplot as plt
import os

# loads the tweets from json files into a list
filenames = sorted(os.listdir('data'))
tweets = []
for filename in filenames:
    with open('data/'+filename, 'r') as f:
        file_tweets = json.loads(f.read())
        tweets += file_tweets

print('len(tweets)=',len(tweets))

# count the number of times obama is used per year
obama_counts = {} # keys = year, values = number of tweets per year
for year in [2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]:
    obama_counts[year]=0
for tweet in tweets:
    year = tweet['created_at'][-4:]
    #print('year=',year)
    if 'house' in tweet['text'].lower():
        obama_counts[int(year)] += 1

print('obama_counts=',obama_counts)

# sort the data for plotting
xs = sorted(obama_counts.keys())
ys = []
for x in xs:
    ys.append(obama_counts[x])

# generate the plots
fig,ax = plt.subplots()
ax.plot(xs, ys)
plt.show()