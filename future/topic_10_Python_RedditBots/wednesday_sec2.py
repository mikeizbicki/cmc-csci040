import praw
reddit = praw.Reddit('bot') # some people need: , user_agent='cs40')

url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
submission = reddit.submission(url=url)

# DON'T DO THIS WHILE YOUR DEBUGGING
#submission.comments.replace_more(limit=None)

for top_level_comment in submission.comments:
    #if type(top_level_comment) == praw.models.reddit.comment.Comment:
    #    print(top_level_comment.body)


    #try:
    #    print(top_level_comment.body)
    #except AttributeError:
    #    pass
    
    print('type(top_level_comment)=',type(top_level_comment))


# list(submission.comments) # list of all top level comments
# submission.comments.list() # is a list of all comments, including replies