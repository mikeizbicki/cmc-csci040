import praw

################################################################################
# Step 1: Logging in
################################################################################

# There are two methods for logging into reddit with PRAW.

########################################
# Method I: Include the login details directly in your python file
reddit = praw.Reddit(
    client_id='client_id',
    client_secret='client_secret',
    user_agent='user_agent',
    username='username',
    password='password',
    )
# NEVER INCLUDE CREDENTIALS IN PYTHON FILES!!!

########################################
# Method II: Include the login details in a `praw.ini` file
# See: https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
reddit = praw.Reddit('bot')

# NOTE:
# For this class, you must ALWAYS use Method II.
# Why?
# The python file is something that you will have to post to github/share with other people.
# But you should never share login credentials with other people for any reason.
# One of the easiest ways for companies to get "hacked" (i.e. cracked) is to leak login credentials.
# See, for example:
# 1. https://qz.com/674520/companies-are-sharing-their-secret-access-codes-on-github-and-they-may-not-even-know-it/
# 1. https://securityboulevard.com/2021/03/solarwinds-intern-leaked-passwords-on-github/
#
# NOTE:
# If you submit your login credentials with any assignment in this class,
# YOU WILL RECEIVE NEGATIVE POINTS ON THE ASSIGNMENT.
# That is because giving someone your login credentials is worse than not completing the assignment at all.
# Companies have lost **b**illions of dollars due to improper handling of login credentials.

################################################################################
# Step 2: Reading data
################################################################################

# See the PRAW QuickStart Guide for instructions on how to use the library:
# https://praw.readthedocs.io/en/stable/getting_started/quick_start.html
'''
for submission in reddit.subreddit("programming").hot(limit=10):
    print('title:', submission.title, 'score:', submission.score, 'author:', submission.author)
'''
# A URL to a funny reddit submission
url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"

submission = reddit.submission(url=url)
print('title:', submission.title, 'score:', submission.score, 'author:', submission.author)

print('before .replace_more()')
submission.comments.replace_more(limit=None)
print('after .replace_more()')

# when you are debugging your code,
# you need fast feedback on what your code does;
# don't call the .replace_more() function
# once you think your code is working, and you want actually test it on everything,
# then you should include the replace_more() function call

# your final bot that is actually processessing EVERYTHING needs to have limit=None

# .replace_more does the replacement to all descendents and not just the top-level comments

for comment in submission.comments:
    #print('type(comment)=', type(comment))

    # submission.comments contained a `MoreComments` type;
    # the .replace_more() function deletes these `MoreComments` and 
    # inserts the actual comments

    # any time you are looping over comments
    # (coming from a submission.comments or comment.replies)
    # you can't assume that what you'll get is a comment
    try:
        print('comment.author=', comment.author, 'comment.body=', comment.body)
        # whenever .author is None, the user account has been deleted
    except AttributeError:
        print('not a comment')