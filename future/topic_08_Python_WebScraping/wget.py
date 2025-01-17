'''
A wget program is a program that "get"s information from the "w"eb.
'''

# Get the url to download from the command line
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--url')
parser.add_argument('--filename') #, default='downloaded_webpage.html')
# "default" default = None; if you don't specify a default and no filename on the command line
# then the value None will be in args.filename
args = parser.parse_args()
url = args.url

print('url=', url)

# Download the URL
import requests
response = requests.get(url)
text = response.text

# Save the file
# 'w' = write
# 'r' = read
# 't' = text => automatically apply the encoding
# 'b' = binary/bytes => don't apply the encoding
# 'x' = write, but if the file already exists throw an error
if not args.filename:
    filename = args.url.split('/')[-1]
else:
    filename = args.filename
with open(filename, mode='xb') as f:
    f.write(text.encode('utf-8'))

