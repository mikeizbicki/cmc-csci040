'''
Beautiful Soup Practice Quiz
============================
'''

from bs4 import BeautifulSoup
html='''
<html>
    <head>
        <title>Lorem Ipsum</title>
    </head>
    <body>
        <div id=header>
            <img src=top-image.png>
        </div>
        <h1 id=top>Lorem <span class=bold>Ipsum</span></h1>
        <p><span class=italic>Lorem ipsum</span> dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
        <blockquote><span class=bold>Ut enim</span> ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</blockquote>
        <p class=bold><a href=https://izbicki.me>Excepteur sint occaecat</a> cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        <br/>
        <a href=https://izbicki.me><img src=bottom-image.png></a>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

############################################################
tags = soup.select('a')
problem1 = len(tags)
print("problem1=",problem1)



############################################################
tags = soup.select('p span')
problem2 = len(tags)
print("problem2=",problem2)



############################################################
tags = soup.select('p,.bold') # remove duplicates
problem3 = len(tags)
print("problem3=",problem3)



############################################################
# equivalent to 'p a'
tags = soup.select('p')
accumulator = []
for tag in tags:
    accumulator += tag.select('a')
problem4 = len(accumulator)
print("problem4=",problem4)



############################################################
tags1 = soup.select('p')  # do not remove duplicates
tags2 = soup.select('.bold')
tags = tags1 + tags2
problem5 = len(tags)
print("problem5=",problem5)
