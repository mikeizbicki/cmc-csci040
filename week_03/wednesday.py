
tweet1 = { "id_str": "947592785519173637", 
          "text": "As our Country rapidly grows stronger and smarter, I want to wish all of my friends, supporters, enemies, haters, and even the very dishonest Fake News Media, a Happy and Healthy New Year. 2018 will be a great year for America!", 
          "created_at": "Sun Dec 31 22:18:20 +0000 2017", 
          "retweet_count": 3969893, 
          "user":{
            "name":"Donald J. Trump",
            "screen_name":"realdonaldtrump",
            "location":"Washington, DC",
            },
          } 
tweet2 = { "id_str": "947592785519173637", 
          "text": "I am Trump", 
          "created_at": "Sun Dec 31 22:18:20 +0000 2017", 
          "retweet_count": 3969893, 
          "user":{
            "name":"Donald J. Trump",
            "screen_name":"realdonaldtrump",
            "location":"Washington, DC",
            },
          }

tweets = [tweet1, tweet2, tweet1, tweet2]

new_tweets = []
for tweet in tweets:
  if tweet meets whatever condition:
    new_tweets.append(tweet)


#print('tweet[text]=',tweet['text'])

for k,v in tweet1.items():
  print('k=',k,'v=',v)
#for k,v in tweet2.items():
#  print('k=',k,'v=',v)

for k in tweet1:
  print('k=',k, 'tweet1[k]=',tweet1[k])

# .keys(), .values(), .items()