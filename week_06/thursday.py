import praw

# login to reddit with your bot's credentials;
# recall that this requires creating a praw.ini file
reddit = praw.Reddit('bot')

# connect to the reddit submission
submission = reddit.submission(url='https://www.reddit.com/r/csci040/comments/dw53wt/political_discussion_thread/')

# click the "view more comments" buttons in the reddit submission in order to download all comments;
# when debugging, I recommend setting this to a small value so that it runs faster;
# it takes reddit 1-3 seconds per click, and so it takes about 10 minutes to click all the buttons;
submission.comments.replace_more(limit=1)

# loop through all the top level comments
print('='*40)
print('top level comments')
print('='*40)
for comment in submission.comments:
    pass
    # FIXME: calculate comment statistics here

# loop through all the comments
print('='*40)
print('all comments')
print('='*40)
for comment in submission.comments.list():
    # FIXME: calculate comment statistics here
    pass
