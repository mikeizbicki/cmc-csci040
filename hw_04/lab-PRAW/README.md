# Reddit Bot Lab I: PRAW

## Overview

Reddit explicitly encourages users to create bots,
and they provide a nice library called PRAW to do so.
The textbook does not cover this topic,
but you can find the library's (excellent) documentation here:
<https://praw.readthedocs.io/>

You should reference this documentaion regularly while working on this lab and your reddit bot homework assignment.
In class, we will cover the basic ideas of what you need to do,
but we won't be able to cover everything.
Learning to read documentation is an important programming skill,
and there's lots of programming memes about it:

<img width=400px src=doc-meme3.jpg>
<br>

<img width=400px src=doc-meme1.jpg>
<br>

<img width=400px src=doc-meme2.png>
<br>


**Required Reading:**

* [Reddit Bots Are Hunting Down Racists, One Post at a Time](https://www.wired.com/story/reddit-bots-are-hunting-down-racists-one-post-at-a-time/)

* [Who’s a Bot? Who’s Not?](https://www.nytimes.com/2020/06/16/science/social-media-bots-kazemi.html)

* [Social Media Bots are Damaging our Democracy](https://www.engadget.com/2019-08-15-social-media-bots-are-damaging-our-democracy.html)

<!--
Example reddit bots:

* https://www.reddit.com/r/Christianity/comments/irsxys/biblequotebot_is_beta/

* https://www.reddit.com/r/OutOfTheLoop/comments/9gv9xs/what_is_going_with_locationbot_and_what_does_it/

* https://www.reddit.com/user/stabbot

* https://www.reddit.com/user/GoodBot_BadBot

* https://www.reddit.com/user/autotldr

* https://www.reddit.com/r/tippr/wiki/reddit-usage

* https://www.reddit.com/r/RemindMeBot/

* https://www.reddit.com/r/botwatch/comments/9zjqfx/the_best_bot/

* https://www.reddit.com/r/botwatch/top/

* https://www.reddit.com/r/SubredditSimulator/

Example twitter bots:

* https://twitter.com/nyt_diff

* https://twitter.com/earthquakesLA

* https://www.gawker.com/5887697/how-i-found-the-human-being-behind-horseebooks-the-internets-favorite-spambot

* https://botwiki.org/bots/twitterbots/
-->

## Lab Instructions

1. Create a reddit account for your bot.
   If you already have a reddit account, you must create a new one.
   Your bot's username can be whatever you like,
   but it must contain the word `bot` somewhere in the account name.
   Acceptable examples include: `cs40-bot` and `BottyMcBotterson`.

1. Visit <https://www.reddit.com/prefs/apps> to register your bot with reddit and generate a client id and client secret.
   Remember that what we're calling bots in this class are what reddit refers to as "script apps" in their app registration.

1. Create a folder on your computer that you will use for your bot's code.
   Inside this folder, create a file called `praw.ini` that includes the login credentials for your user account and bot.
   Download the `bot_stats.py` file and place it in this folder.

1. Modify the `bot_stats.py` file to fix the `FIXME` annotations.
   When you're done, the final output will look something like this:

    ```
    ========================================
    top level comments
    ========================================
    Total comments = 617
    Deleted comments = 11
    Comments per user = 
    {'BotForCS': 9,
     'CS040_bot': 1,
     'FlakyJob': 1,
     'VROMERO23': 209,
     'anniecave': 2,
     'avaliao23': 1,
     'axel_sverker': 57,
     'cmccs40': 2,
     'cs040BOT': 2,
     'cs40-bot': 1,
     'cs40-bot2': 1,
     'danny63758': 100,
     'droman22cmc': 211,
     'emolyandmatolda': 1,
     'emor714': 4,
     'jhaughton': 2,
     'mornelas5': 1,
     'plagiarism-bot': 1}

    ========================================
    all comments
    ========================================
    Total comments = 4211
    Deleted comments = 218
    Comments per user = 
    {'BotForCS': 69,
     'CS040_bot': 2403,
     'CS40_BOTTY': 36,
     'FlakyJob': 143,
     'VROMERO23': 209,
     'anniecave': 44,
     'avaliao23': 3,
     'axel_sverker': 88,
     'cmccs40': 12,
     'cmoffatt21': 201,
     'cs040BOT': 235,
     'cs40-bot': 3,
     'cs40-bot2': 13,
     'danny63758': 101,
     'droman22cmc': 211,
     'emolyandmatolda': 15,
     'emor714': 9,
     'jhaughton': 61,
     'mornelas5': 44,
     'plagiarism-bot': 17,
     'richardnotspencer': 76}
    ```

### Submission

Upload **both** the `bot_stats.py` file and the output of running the file to sakai.

**WARNING:**
You cannot share your credential information with anyone,
including me.
If you include any credential information in your submission,
you will receive NEGATIVE POINTS on the lab!!!

One of the most common ways for companies to get hacked is for programmers to accidentally upload their login credentials to github.
For examples, see:
1. https://qz.com/674520/companies-are-sharing-their-secret-access-codes-on-github-and-they-may-not-even-know-it/
1. https://securityboulevard.com/2021/03/solarwinds-intern-leaked-passwords-on-github/
