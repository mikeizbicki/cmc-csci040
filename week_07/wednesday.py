
# get this library by running
# $ pip3 install textblob
from textblob import TextBlob

comments = [
    'Trump will keep America great.  Vote for trump!!!',                                        # pro trump
    'Trump is the worst president ever.',                                                       # anti-trump
    "Trump is okay I guess, I don't really care",                                               # neutral trump
    "Biden has a strong track record of successfully working for Americans.  Vote for Biden!",
    "Biden is an idiot who can't speak without a teleprompter.",
    "Biden is blah.  "
]

for comment in comments:

    blob = TextBlob(comment)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    print('comment=',comment)
    print('polarity=',polarity)             # -1 is bad , +1 is good
    print('subjectivity=',subjectivity)     # 0 is perfectly unbiased, 1 is totally subjective
    print()

    #if 'Trump' in comment and polarity > 0:
    #    print('comment=',comment)

    #if 'Trump' in comment and polarity < 0:
        # this is an anti trump comment