import praw

reddit = praw.Reddit('bot')

submission = reddit.submission(url='https://www.reddit.com/r/csci040/comments/dw53wt/political_discussion_thread/')

submission.comments.replace_more(limit=1)

for comment in submission.comments:
    print('comment.author=',comment.author)
