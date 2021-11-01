'''
Beautiful Soup Question Bank
============================

There may be more than 1 of each type of question listed below on the actual quiz.
'''

from bs4 import BeautifulSoup
html='''
<html>
    <head>
        <title>Lorem Ipsum</title>
    </head>
    <body>
        <div id=header>
            <h1 id=top>Lorem <span class=bold>Ipsum</span></h1>
            <img src=top-image.png>
        </div>
        <div id=body>
            <h2>Lorem</h2>
            <p class=bold>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            <p class=bold>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
            <h2>Ipsum</h2>
            <ol>
                <li><img class=bold src=ceasar.png></li>
                <li class=bold><em>Veni</em></li>
                <li class=bold><em>Vidi</em></li>
                <li class=bold><em>Vici</em></li>
            </ol>
        </div>
    </body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')

########################################
tags = soup.select('div > li')
problem1 = len(tags)
print("problem1=",problem1)

########################################
tags = soup.select('div li')
problem1a = len(tags)
print("problem1a=",problem1a)

########################################
tags = soup.select('img.bold')
problem1b = len(tags)
print("problem1b=",problem1b)

########################################
tags = soup.select('li.bold')
problem1c = len(tags)
print("problem1c=",problem1c)

########################################
tags = soup.select('li .bold')
problem1d = len(tags)
print("problem1d=",problem1d)

########################################
tags = soup.select('h2+p')
problem1e = len(tags)
print("problem1e=",problem1e)

########################################
tags = soup.select('div>h2+p,h2')
problem1f = len(tags)
print("problem1f=",problem1f)

########################################
tags = soup.select('ol')
accumulator = []
for tag in tags:
    accumulator += tag.select('img')
problem2 = len(accumulator)
print("problem2=",problem2)

########################################
tags = soup.select('div')
accumulator = []
for tag in tags:
    accumulator += tag.select('img')
problem2a = len(accumulator)
print("problem2a=",problem2a)

########################################
tags = soup.select('body')
accumulator = []
for tag in tags:
    accumulator += tag.select('title')
problem2b = len(accumulator)
print("problem2b=",problem2b)

########################################
tags = soup.select('html')
accumulator = []
for tag in tags:
    accumulator += tag.select('title')
problem2c = len(accumulator)
print("problem2c=",problem2c)

########################################
tags1 = soup.select('h1')
tags2 = soup.select('#top')
tags = tags1 + tags2
problem3 = len(tags)
print("problem3=",problem3)

########################################
tags1 = soup.select('p')
tags2 = soup.select('.bold')
tags = tags1 + tags2
problem3b = len(tags)
print("problem3b=",problem3b)


########################################
tags1 = soup.select('div')
tags2 = soup.select('.bold')
tags = tags1 + tags2
problem3c = len(tags)
print("problem3c=",problem3c)

