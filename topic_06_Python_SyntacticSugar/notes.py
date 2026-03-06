
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


# Problem 21
names = ['alice', 'bob', 'charlie', 'dave', 'eve']
greetings = ['hello ' + name for name in names]
#greetings = []
#for name in names:
#    greetings.append('hello ' + name)
# anytime you see the keyword for inside of a list
# you have a "comprehension"
greeting = greetings[2]
print('21: greeting=', greeting)

# Problem 22
# range(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
xs = [ x*x for x in range(10) ]
num = xs[5]
print('22: num=', num)

########################################
# List Comprehensions (2)
########################################

# The following python code
# ```
# accumulator = [COMPUTATION for VARIABLE in LIST if CONDITION]
# ```
# desugars into
# ```
# accumulator = []
# for VARIABLE in LIST:
#     if CONDITION:
#         accumulator.append(COMPUTATION)
# ```


# Problem 25
# it will find the squares of all odd numbers
# 1, 9, 25, 49 ...
xs = [ x*x for x in range(10) if x%2 ]
xs = []
for x in range(10):
    # in python, 0 is falsey
    # everything else truthy
    if x%2:
        xs.append(x*x)
num = xs[3]
print('25: num=', num)

# Problem 26
sentence = 'This is an example sentence with a few words in it.'
small_words = [ word.lower() for word in sentence.split() if len(word) <= 2]
print('len(small_words)=', len(small_words))


########################################
# List Comprehensions (3)
########################################

# If you have nested comprehensions,
# repeat the desugaring steps above from outside to inside.

# Problem 35
xss = [[i for i in range(x)] for x in [2, 3, 4] if x%2 == 0]
x = xss[-1][-2]
print('x=', x)


########################################
# List Comprehensions (4)
########################################

# If you have a comprehension with multiple `for` statements,
# repeat the desugaring steps above from left to right.

# Problem 40
xss = [i for x in [2, 3, 4] if x%2 == 0 for i in range(x)]
#x = xss[-1][-2]
print('x=', x)

# list comp. inside list comp. gives me a list of lists as a result
# makes sense to have 2 [][] indexing

# two for loops in the same list comp.
# the result will always be just an individual list (not list of lists)

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

# Problem 21
# list comprehensions extremely common for transforming data
trump_tweets = [tweet for tweet in tweets if 'trump' in tweet['text'].lower()]
print('len(trump_tweets)=',len(trump_tweets))

