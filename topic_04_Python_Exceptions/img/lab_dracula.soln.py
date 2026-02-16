
import requests
r = requests.get('http://www.gutenberg.org/files/345/345-h/345-h.htm')
r.encoding = 'utf-8'
with open('dracula.html', 'w') as f:
    f.write(r.text)

# NOTE:
# The default encoding for requests.get is 'ISO-8859-1',
# which is like ASCII but for all Latin languages.
# In particular, it has accented Latin characters,
# but it does not have Greek/Russian/Chinese/etc characters
# or any fancy punctuation marks.
# You can change the encoding with
# >>> r.encoding = 'utf-8'

with open('dracula.html','r') as f:
    text=f.read()

text=text.replace('Dracula','<strong>Izbicki</strong>')
text=text.replace('dracula','<strong>izbicki</strong>')
text=text.replace('DRACULA','<strong>IZBICKI</strong>')
text=text.replace('D&nbsp;R&nbsp;A&nbsp;C&nbsp;U&nbsp;L&nbsp;A','<strong>I&nbsp;Z&nbsp;B&nbsp;I&nbsp;C&nbsp;K&nbsp;I</strong>')
text=text.replace(' count ',' <strong>professor</strong> ')
text=text.replace(' count.',' <strong>professor</strong>,')
text=text.replace(' count,',' <strong>professor</strong>.')
text=text.replace(" count'"," <strong>professor</strong>'")
text=text.replace('\ncount ','\n<strong>professor</strong> ')
text=text.replace('\ncount.','\n<strong>professor</strong>,')
text=text.replace('\ncount,','\n<strong>professor</strong>.')
text=text.replace("\ncount'"," <strong>professor</strong>'")
text=text.replace('Count ','<strong>Professor</strong> ')
text=text.replace('Count.','<strong>Professor</strong>,')
text=text.replace('Count,','<strong>Professor</strong>.')
text=text.replace("Count'","<strong>Professor</strong>'")
text=text.replace('Bram Stoker','Mike Izbicki')
text=text.replace('Bram &nbsp; Stoker','Mike &nbsp; Izbicki')

with open('izbicki.html','w') as f:
    f.write(text)
