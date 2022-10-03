filename = 'example_file'

################################################################################
# opening a file
################################################################################

with open(filename, 'br') as f:
    text = f.read()
print("text=",text)

with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()
print("text=",text)

################################################################################
# absolute vs relative paths
################################################################################

import os
os.getcwd()
