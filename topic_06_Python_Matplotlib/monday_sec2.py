#print('hello world')

# macs (everything that's not windows), android, smart watch, default encoding = 'utf8'
# windows, the default encoding depends on your system settings
# always specify the encoding


with open('blurb', 'rb' ) as f:   # r = read; b = binary
    byte = f.read()  # returns a bytes object because the mode contains a "b"
    text = byte.decode('utf-8')

with open('blurb', 'r', encoding='utf8') as f: # the 'r' is optional
    text = f.read()  # returns a str directly because the mode does not contain a "b"
    # f.write() gives an error

with open('blurb_out', 'w', encoding='utf-8') as f:
    f.write(text.upper())
    # f.read() gives an error

# how does bytes fit into all of this?

print(text)