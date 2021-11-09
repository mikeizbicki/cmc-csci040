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

# The `username`/`password` values are something that you select when creating your reddit account.
# The `client_id`/`client_secret` are like a username/password that reddit generates for your bot's account.
# Reddit will create these for you automatically, and the PRAW lab has instructions for getting them.
# `user_agent` should be set to `cs40bot` for everyone.

########################################
# Method II: Include the login details in a `praw.ini` file
# See: https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
reddit = praw.Reddit('bot', user_agent='cs40')

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


for submission in reddit.subreddit("learnpython").top(time_filter='day',limit=10):
    print('score=',submission.score,'title=',submission.title)
