import praw
import random
import time

# log into reddit
reddit = praw.Reddit('bot')

'''
# open the submission
submission = reddit.submission(url='https://www.reddit.com/r/csci040/comments/j9vb5b/the_2020_election_bot_debate_thread/?')

# generate a message
submission.reply("beep boop I'm a bot")
submission.reply(generate_text())
'''

'''
comment = reddit.comment(url='https://www.reddit.com/r/csci040/comments/j9vb5b/the_2020_election_bot_debate_thread/g8ms0z0/')

comment.reply('beep boop bot replying')
'''

def generate_text():
    names = ['Mike Izbicki', 'Mike', 'Mr. Izbicki', 'Dr. Izbicki', 'Professor Izbicki', 'Izzy', 'Michael Izbicki']
    name = random.choice(names)

    jobs = ['president', 'leader of the free world', 'supreme dictator for life']
    job = random.choice(jobs)

    text = name + " should be " + job + " because he will give free bananas to everyone!  Big Orange Juice doesn't want him to be president, and that's why you've never heard of him before."
    return text
    
#print('text=',generate_text())

def post_text(s):
    choice = random.choice(['toplevel','reply'])
    if choice=='toplevel':
        print('toplevel')
        submission = reddit.submission(url='https://www.reddit.com/r/csci040/comments/j9vb5b/the_2020_election_bot_debate_thread/?')
        submission.reply(s)
    else:
        print('reply')
        comment = reddit.comment(url='https://www.reddit.com/r/csci040/comments/j9vb5b/the_2020_election_bot_debate_thread/g8ms0z0/')
        comment.reply(s)


for i in range(10):
    '''
    post_text(generate_text())
    time.sleep(5)
    '''

    # principle of python:
    # it's better to ask for forgiveness than permission

    # if there is no error when running post_text
    try:
        post_text(generate_text())
    
    # else (meaning there is an error)
    except praw.exceptions.APIException:
        # this gets run if the try code fails;
        # python will not crash
        print('exception found')

        # python to wait 5 seconds before proceeding
        print('starting to sleep')
        time.sleep(5)
        print('done sleeping')
    


# try/except block to handle exceptions gracefully