import praw

username='cs40-bot2' # name of account
password='secure_password'
client_id='jkzLinzf4je2hQ'
client_secret='5cI9FqYoewZUmd72Cu2d-Rfsv7U'
user_agent='cs40-bot2'

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
    )

i=0
for submission in reddit.subreddit('learnpython').top(limit=10):
    i+=1
    print(i,': score=',submission.score,';',submission.title)
    if 'python' in submission.title.lower():
        print('upvoting')
        submission.upvote()

submission=reddit.submission(url='https://www.reddit.com/r/csci040/comments/dvb4zg/hello_cs40/')

submission.reply('This is an example from class.')



