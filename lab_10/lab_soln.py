#!/bin/env python3

with open('dracula.html','r') as f:
    text=f.read()

text=text.replace('Dracula','<strong>Izbicki</strong>')
text=text.replace('dracula','<strong>izbicki</strong>')
text=text.replace('DRACULA','<strong>IZBICKI</strong>')
text=text.replace('D&nbsp;R&nbsp;A&nbsp;C&nbsp;U&nbsp;L&nbsp;A','<strong>I&nbsp;Z&nbsp;B&nbsp;I&nbsp;C&nbsp;K&nbsp;I</strong>')
text=text.replace(' count ',' <strong>professor</strong> ')
text=text.replace(' count.',' <strong>professor</strong>,')
text=text.replace(' count,',' <strong>professor</strong>.')
text=text.replace('\ncount ','\n<strong>professor</strong> ')
text=text.replace('\ncount.','\n<strong>professor</strong>,')
text=text.replace('\ncount,','\n<strong>professor</strong>.')
text=text.replace('Count ','<strong>professor</strong> ')
text=text.replace('Count.','<strong>professor</strong>,')
text=text.replace('Count,','<strong>professor</strong>.')
text=text.replace('Bram Stoker','Mike Izbicki')
text=text.replace('Bram &nbsp; Stoker','Mike &nbsp; Izbicki')

with open('izbicki.html','w') as f:
    f.write(text)
