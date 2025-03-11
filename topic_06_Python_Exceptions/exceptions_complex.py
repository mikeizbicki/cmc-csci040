# You will not be quizzed on the exceptions described in this file.
# Instead, you will encounter these exceptions while programming.
# (And probably already have encountered them!) 
# The purpose of this discussion is to help you debug your programs.

########################################
# Files
########################################

# Opening a file that doesn't exist results in an exception
"""
with open('file') as f:
    text = f.read()
"""

# There are two ways to fix this problem.

# Method 1: "Ask for permission"
'''
import os
if os.path.exists('file'):
    with open('file') as f:
        text = f.read()
else:
    print('bad file')
'''

# Method 2: "Ask for forgiveness"
'''
try:
    with open('does not exist') as f:
        text = f.read()
    print('text=', text)
except FileNotFoundError:
    print('file not found')
'''

########################################
# bare except clauses
########################################

'''
try:
    with open('does not exist') as f:
        text = f.read()
    print('text=', text)
except:
    print('file not found')
'''
