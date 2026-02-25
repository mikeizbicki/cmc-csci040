'''
Beautiful Soup Quiz
===================
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
tags = soup.select('div li.bold')
problem1 = len(tags)
print("problem1=", problem1)



########################################
tags = soup.select('div>h2+p,h2')
problem2 = len(tags)
print("problem2=", problem2)



########################################
tags = soup.select('div')
accumulator = []
for tag in tags:
    accumulator += tag.select('img')
problem3 = len(accumulator)
print("problem3=", problem3)



########################################
tags1 = soup.select('span')
tags2 = soup.select('.bold')
tags = tags1 + tags2
problem4 = len(tags)
print("problem4=", problem4)
