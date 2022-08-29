import praw
reddit = praw.Reddit('bot')

url = "https://www.reddit.com/r/funny/comments/3g1jfi/buttons/"
submission = reddit.submission(url=url)

#submission.comments.replace_more(limit=None) #clicks all of the "more comments" buttons so you get more comments;

for top_level_comment in submission.comments:
    print('type(top_level_comment)=', type(top_level_comment))
    #if type(top_level_comment) == praw.models.reddit.comment.Comment:
    #    print(top_level_comment.body)
    
    try:
        print(top_level_comment.body)
    except AttributeError:
        pass

print('total comments=', len(submission.comments.list()))

# list(submission.comments) converts top level comments into a list
# submission.comments.list() gives you a list of all comments (including non-top level comments)