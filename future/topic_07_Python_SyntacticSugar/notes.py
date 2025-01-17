
########################################
# List Comprehensions (1)
########################################

# The following python code
# ```
# accumulator = [ COMPUTATION for VARIABLE in LIST ]
# ```
# desugars into
# ```
# accumulator = []
# for VARIABLE in LIST:
#     accumulator.append(COMPUTATION)
# ```


# Problem 4
'''
names = ['alice', 'bob', 'charlie', 'dave', 'eve']
greetings = ['hello ' + name for name in names]
#greetings = []
#for name in names:
#    greetings.append('hello ' + name)
greeting = greetings[2]
print('greeting=', greeting)
'''

# Problem 5
'''
xs = [ x*x for x in range(10) ]
print('list(range(10)=',list(range(10)))
print('xs=',xs)
#xs = []
#for x in range(10):
#    xs.append(x*x)
num = xs[5]
print('num=', num)
'''

########################################
# List Comprehensions (2)
########################################

# The following python code
# ```
# accumulator = [ COMPUTATION for VARIABLE in LIST if CONDITION]
# ```
# desugars into
# ```
# accumulator = []
# for VARIABLE in LIST:
#     if CONDITION:
#         accumulator.append(COMPUTATION)
# ```
'''
# Problem 6
xs = [ x*x for x in range(10) if x%2 ]
print('list(range(10))=', list(range(10)))
#xs = []
#for x in range(10):
#    if x%2:
#        xs.append(x*x)
print('xs=', xs)

num = xs[3]
print('num=', num)
'''

# Problem 9
sentence = 'This is an example sentence with a few words in it.'
print('sentence.split()=', sentence.split())
small_words = [ word.lower() for word in sentence.split() if len(word) <= 2]
print('small_words=', small_words)
#small_words = []
#for word in sentence.split():
#    if len(word) <= 2:
#        small_words.append(word.lower())
print('len(small_words)=', len(small_words))


########################################
# List Comprehensions (3)
########################################

# If you have nested comprehensions,
# repeat the desugaring steps above from outside to inside.

# Problem 15
#xss = [[i for i in range(x)] for x in [2, 3, 4] if x%2 == 1]
'''
xss = []
for x in [2, 3, 4]:
    if x%2 == 1:
        xss.append([i for i in range(x)])
        #xs = []
        #for i in range(x):
        #    xs.append(i)
        #xss.append(xs)
print('xss=', xss)
#x = xss[-1][-2]
x = xss[0]
print('x=', x)
'''

########################################
# List Comprehensions (4)
########################################

# You will have at least one problem on the quiz based on the following `tweets` variable.

tweets = [
    { "source": "Twitter Web Client"
    , "text": "From Donald Trump: Wishing everyone a wonderful holiday & a happy, healthy, prosperous New Year. Let\u2019s think like champions in 2010!"
    , "retweet_count": 28
    }, 
    { "source": "Twitter Web Client"
    , "text": "Trump International Tower in Chicago ranked 6th tallest building in world by Council on Tall Buildings & Urban Habitat http://bit.ly/sqvQq"
    , "retweet_count": 33
    },
    { "source": "Twitter Web Client"
    , "text": "Wishing you and yours a very Happy and Bountiful Thanksgiving!"
    , "retweet_count": 13
    },
    { "source": "Twitter for iPhone"
    , "text": "RT @realDonaldTrump: Happy Birthday @DonaldJTrumpJr!\nhttps://t.co/uRxyCD3hBz"
    , "retweet_count": 9529
    },
    { "source": "Twitter for iPhone"
    , "text": "Happy Birthday @DonaldJTrumpJr!\nhttps://t.co/uRxyCD3hBz"
    , "retweet_count": 9529
    },
    { "source": "Twitter for Android"
    , "text": "Happy New Year to all, including to my many enemies and those who have fought me and lost so badly they just don't know what to do. Love!"
    , "retweet_count": 141853
    },
    { "source": "Twitter for Android"
    , "text": "Russians are playing @CNN and @NBCNews for such fools - funny to watch, they don't have a clue! @FoxNews totally gets it!"
    , "retweet_count": 23213
    },
    { "source": "Twitter for iPhone"
    , "text": "Join @AmerIcan32, founded by Hall of Fame legend @JimBrownNFL32 on 1/19/2017 in Washington, D.C.\u2026 https://t.co/9WJZ8iTCQV"
    , "retweet_count": 7366
    }]

# Problem 19
'''
text = tweets[-1]['text']
mentions = [word for word in text.split() if word[0] == '@']
print('text=', text)
print('mentions=', mentions)
'''

'''
mentions = [[word for word in tweet['text'].split() if word[0] == '@'] for tweet in tweets if len([word for word in tweet['text'].split() if word[0] == '@']) > 0]
print('mentions=',mentions)
'''

'''
popular_tweets = [tweet for tweet in tweets if tweet['retweet_count'] > 100]
#popular_tweets = []
#for tweet in tweets:
#    if tweet['retweet_count'] > 100:
#        popular_tweets.append(tweet)
print('len(popular_tweets)=',len(popular_tweets))
'''