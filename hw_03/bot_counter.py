import praw

# FIXME:
# edit this line to contain your bot's username
username = 'Li_bot_cs40'

# FIXME:
# the praw instance needs access to a valid praw.ini file 
# with a login credentials section called "bot"
reddit = praw.Reddit('bot')
redditor = reddit.redditor(name = username)

# calculate and print the total number of comments that username has created
comments = list(redditor.comments.new(limit=None))
print("len(comments)=",len(comments))

# calculate and print the total number of top level comments and the total number of replies
top_level_comments = []
replies = []
for comment in comments:
    try:
        if type(comment.parent()) is praw.models.Submission:
            top_level_comments.append(comment)
        else:
            replies.append(comment)
    except AttributeError:
        pass
print("len(top_level_comments)=",len(top_level_comments))
print("len(replies)=",len(replies))

# calculate the number of valid top level comments
parents = []
for reply in top_level_comments:
    parents.append(reply.parent().id)
valid_top_level_comments = []
for reply in top_level_comments:
    if parents.count(reply.parent().id) == 1:
        valid_top_level_comments.append(reply)
print("len(valid_top_level_comments)=",len(valid_top_level_comments))

# calculate the number of replies that are not replying to themselves
not_self_replies = []
for reply in replies:
    try:
        if reply.parent().author.name!=username:
            not_self_replies.append(reply)
    except AttributeError:
        pass
print("len(not_self_replies)=",len(not_self_replies))

# calculate the number of valid replies;
# that is, replies that are not replying to themselves,
# and that are not duplicate replies to the same parent comment
parents = []
for reply in not_self_replies:
    try:
        parents.append(reply.parent().id)
    except AttributeError:
        pass
valid_replies = []
for reply in not_self_replies:
    try:
        if parents.count(reply.parent().id) == 1:
            valid_replies.append(reply)
    except AttributeError:
        pass
print("len(valid_replies)=",len(valid_replies))

# the total number of valid comments is the number of valid top level comments 
# plus the number of valid replies
valid_comments = len(valid_replies) + len(valid_top_level_comments)
print('========================================')
print("valid_comments=",valid_comments)
print('========================================')
print('NOTE: the number valid_comments is what will be used to determine your extra credit')
