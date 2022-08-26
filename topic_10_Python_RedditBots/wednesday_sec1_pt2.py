import praw
reddit = praw.Reddit('bot')

import time

url = "https://old.reddit.com/r/BotTown/comments/qr05je/practice_posting_messages_here/"
submission = reddit.submission(url=url)

for i in range(1000000):
    print('made a comment, i=',i)
    submission.comments[0].reply('this is a reply to a comment')
    time.sleep(5)