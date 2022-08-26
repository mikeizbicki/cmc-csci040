# PRINCIPLE 1: know your working directory
# PRINCIPLE 2: know your file encoding

'''
# these two lines are the same on a mac
with open('/home/user/proj/cmc-csci040/week_06/data/blurb') as f:
with open('/home/user/proj/cmc-csci040/week_06/data/blurb', encoding='utf8') as f:

# if you're on windows, the default encoding depends on many different factors
'''
'''
# for this class, if you use the open function, you must specify the encoding
with open('data/blurb', encoding='utf8') as f:
    text = f.read()

with open('data/blurb_new', 'w', encoding='utf16') as f:
    f.write(text)

print(text)
'''

# these two "paragraphs" are exactly the same
with open('data/blurb', 'tr') as f:  # mode contains a b => get a bytes; mode contains a t => get a string
    text = f.read()

with open('data/blurb', 'br') as f:
    byte = f.read()
    text = byte.decode('utf-8')

#import os
#print(os.getcwd())

#import math
#math.sqrt

#print('hello world')

# /home/user/proj/cmc-csci040/week_06/monday_sec1.py is an absolute path
# absolute path is a path that works anywhere; it always references the same file no matter where you are located

# a relative path is a reference to a file that is not an absolute path


# the computer always converts relative paths into absolute paths to access a file
# how does it do that?

# working directory is "where you are located"

# pwd = print working directory; directory = folder

# put the working directory at the beginning of the relative path to make an absolute path

# cd = change working directory