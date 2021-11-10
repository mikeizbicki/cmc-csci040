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

## Lab Instructions

**Pre-lab activity:**

1. Create a reddit account for your bot.
   If you already have a reddit account, you must create a new one.
   Your bot's username can be whatever you like,
   but it must contain the word `bot` somewhere in the account name.
   Acceptable examples include: `cs40-bot` and `BottyMcBotterson`.

1. Visit <https://www.reddit.com/prefs/apps> to register your bot with reddit and generate a client id and client secret.
   Remember that what we're calling bots in this class are what reddit refers to as "script apps" in their app registration.

1. Create a folder on your computer that you will use for your bot's code.
   Inside this folder, create a file called `praw.ini` that includes the login credentials for your user account and bot.
   Ensure that you can run the `monday_secX.py` file that we created in class on Monday without getting any errors.

**Lab:**

1. Download the `bot_stats.py` file and place it in your bot folder.

1. Modify the `bot_stats.py` file to fix the `FIXME` annotations.
   When you're done, the final output will look something like this:

   ```
   ========================================
   top level comments
   ========================================
   nondeleted_comments= 4
   deleted_comments= 2
   {Redditor(name='plagiarism-bot'): 1,
    Redditor(name='cs40-bot2'): 2,
    Redditor(name='cs40-bot'): 1}
   ========================================
   all comments
   ========================================
   nondeleted_comments= 735
   deleted_comments= 3
   {Redditor(name='plagiarism-bot'): 110,
    Redditor(name='sneakpeekbot'): 1,
    Redditor(name='cs40-bot2'): 150,
    Redditor(name='RemindMeBot'): 1,
    Redditor(name='cs40-bot'): 467}
   ```

   **HINT:**
   If your numbers are smaller than mine,
   it means you're not getting all of the comments.
   If your numbers are larger than mine,
   that probably just means more comments have been posted since I ran my solution.

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
