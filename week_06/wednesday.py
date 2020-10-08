import praw

# first topic: securely logging into reddit
# how can we login without including the credentials in the file?

# NEVER HAVE PASSWORDS IN A PYTHON FILE
# If there is a password in any file you submit from now on:
#  not only will you get a zero on the assignment, 
#  you will get a NEGATIVE score (-20%)
'''
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
    )
'''

# https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html
reddit = praw.Reddit('bot')

submission = reddit.submission(url='https://www.reddit.com/r/csci040/comments/dw53wt/political_discussion_thread/')
#for submission in reddit.subreddit('learnpython').top(time_filter='month',limit=1):
print('submission=',submission)
print('len(submission.comments)=',len(submission.comments))                 # gives us only top-level comments
print('type(submission.comments)=',type(submission.comments))
print('len(submission.comments.list())=',len(submission.comments.list()))   # gives us all comments (including replies)

# This is the way I always call replace_more if I'm going to call it:
# submission.comments.replace_more(limit=None)
print('len(submission.comments)=',len(submission.comments))                 # gives us only top-level comments
print('len(submission.comments.list())=',len(submission.comments.list()))   # gives us all comments (including replies)

for comment in submission.comments:
    if type(comment) is praw.models.reddit.comment.Comment:
        print('comment.author=',comment.author)
        print('type(comment)=',type(comment))
        for reply in comment.replies: # comment.replies is a CommentForest
            #if type(reply) is # type of a comment
            if type(reply) is praw.models.reddit.comment.Comment:
                print('  reply.author=',reply.author)

'''
# in order to check whether a comment is deleted
if comment.author is None:
    pass # then the post is deleted
else:
    pass # the post is not deleted
'''

'''
for comment in submission.comments:
    #print('  type(comment)=',type(comment))
    print('  author=',comment.author)
'''
#for comment in submission.comments:
#    print('comment=',comment)

#print(len(submission.comments))

#comments = submission.comments

#print('comments=',comments)