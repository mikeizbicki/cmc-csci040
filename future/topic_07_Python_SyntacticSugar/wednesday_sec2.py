import json
import matplotlib.pyplot as plt
import os

# load the tweets from json files into a list
filenames = sorted(os.listdir('data'))
tweets = []
for filename in filenames:
    with open('data/'+filename, 'r', encoding='ascii') as f:
        file_tweets = json.loads(f.read())
        tweets += file_tweets

# count the number of times obama is used per year
obama_counts = {} # keys = year, values = number of tweets in that year
for year in range(2009,2019):
    obama_counts[str(year)]=0
for tweet in tweets:
    year = tweet['created_at'][-4:]
    if 'obama' in tweet['text'].lower():
        obama_counts[year] += 1
        #obama_counts[int(year)] = obama_counts[int(year)] + 1
print('obama_counts=', obama_counts)

# get the plot data
xs = sorted(obama_counts.keys())
ys = [ obama_counts[x] for x in xs ]
#ys = obama_counts.values()

print('xs=',xs)

# plot the data
fig, ax = plt.subplots()
ax.plot(xs, ys)
plt.show()