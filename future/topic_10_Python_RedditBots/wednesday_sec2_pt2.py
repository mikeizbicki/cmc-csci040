import time
import praw
reddit = praw.Reddit('bot') # some people need: , user_agent='cs40')

submission = reddit.submission('qr9qj1')

for i in range(1000000):
    text = 'message i='+str(i)
    print(text)
    submission.reply(text)
    time.sleep(5)