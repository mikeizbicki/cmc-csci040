# 'r' = read, default
# 'w' = write, create file
#     = DANGER: erase file
# 'a' = append, create file
#       does not erase file
#       SAFER option
# 'x' = exclusive write
#       generates error if file already exists
#       SAFEST option
'''
with open('test','x') as f:
    f.write('hello world!\n')
'''
try:
    with open('test','w') as f:
        f.write('hello world!\n')
    this_variable_does_not_exist
except FileExistsError:
    print('file already exists')
except NameError:
    print('I had a typo in the code.')

import requests
#requests.get('google.com')

def safe_get(url):
    try:
        r=requests.get(url)
    except requests.exceptions.MissingSchema:
        url='http://'+url
        r=requests.get(url)
    return r
r=safe_get('http://google.com')
print('r=',r)

def copy_file(src,dest):
    try:
        with open(src,'r') as f_src:
            with open(dest,'x') as f_dest:
                f_dest.write(f_src.read())
    except FileNotFoundError:
        print('src file does not exist')
    except FileExistsError:
        print('dest file already exists')


print('I printed this.')

'''
f=open('test')
f.read()
f.readlines()
f.close()

with open('test') as f:
    f.read()
    f.readlines()
# f is automatically closed
'''
