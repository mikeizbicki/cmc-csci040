import praw

# praw is a "lazy" library;
# this is actually a good thing
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
    )

# default limit=100
for submission in reddit.subreddit('learnpython').top(time_filter='month',limit=1):
    print('submission=',submission)
    print('score=',submission.score,'title=',submission.title)
    for comment in submission.comments:
        print('  author=',comment.author,'  comment=',comment.body)

    '''
    if 'biden' in submission.title.lower()
        submission.upvote()
    elif 'trump' in submission.title.lower()
        submission.downvote()
    '''

# programs that run continuously are called daemons

