# Week 10: Reddit Bots I

<center>
<img width='50%' src=duty_calls.png />
</center>

**Monday/Wednesday:**
We will be covering how to use the PRAW library this week for making reddit bots.
The textbook does not cover this topic,
but you can find the library's (excellent) documentation here:
https://praw.readthedocs.io/

Readings about bots online:

* [Reddit Bots Are Hunting Down Racists, One Post at a Time](https://www.wired.com/story/reddit-bots-are-hunting-down-racists-one-post-at-a-time/)

* [Who’s a Bot? Who’s Not?](https://www.nytimes.com/2020/06/16/science/social-media-bots-kazemi.html)

* [Social Media Bots are Damaging our Democracy](https://www.engadget.com/2019-08-15-social-media-bots-are-damaging-our-democracy.html)

Example useful reddit bots:

* https://www.reddit.com/r/Christianity/comments/irsxys/biblequotebot_is_beta/

* https://www.reddit.com/r/OutOfTheLoop/comments/9gv9xs/what_is_going_with_locationbot_and_what_does_it/

* https://www.reddit.com/user/stabbot

* https://www.reddit.com/user/GoodBot_BadBot

* https://www.reddit.com/user/autotldr

* https://www.reddit.com/r/tippr/wiki/reddit-usage

* https://www.reddit.com/r/RemindMeBot/

<!--
* https://www.reddit.com/r/botwatch/comments/9zjqfx/the_best_bot/

* https://www.reddit.com/r/botwatch/top/
-->

<!--
AI written text:

* https://www.reddit.com/r/aigeneratedmemes/top/

* https://www.reddit.com/r/talkwithgpt2bots/comments/gc26tf/make_your_own_gpt2_bot_tutorial_and_script/

* https://bonkerfield.org/2020/04/twenty-minute-gpt2-reply-bot/

* https://play.aidungeon.io

Bots talking to each other:

* https://www.reddit.com/r/SubredditSimulator/

Twitter bots

* https://botwiki.org/bots/twitterbots/
-->


## Lab

TBA

<!--
1. Create a reddit account for your bot.
   If you already have a reddit account, you must create a new one.
   Your bot name can be whatever you like, but it must contain the word `bot` somewhere in the account name.
   Acceptable examples include: `cs40-bot` and `BottyMcBotterson`.

1. Visit https://www.reddit.com/prefs/apps to register your bot with reddit and generate a client id and client secret.
   (Remember that bots in this class are what reddit refers to as **script** apps.)

1. Create a folder on your computer that you will use for your bot's code.
   Inside this folder, create a file called `praw.ini` that includes the login credentials for your user account and bot.
   Also create a file `bot_stats.py` that will have the first version of your bot's code.
   We will be creating more bot files later on.

1. Modify the `bot_stats.py` file so that it:

    1. Logs on to reddit
    
    1. Loads the submission https://www.reddit.com/r/csci040/comments/dw53wt/political_discussion_thread/

    1. Loops through every *top level* comment in the submission,
       calculating the total number of *top level* comments,
       the total number of deleted *top level* comments,
       and the total number of *top level* comments posted by each user.

    1. Repeats the above procedure for all comments instead of just top level comments.

    1. You should print out the numbers you calculate.
       For reference, the statistics I calculate are shown below:

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
If you include any credential information in your submission, you will receive NEGATIVE POINTS on the lab!!!
-->
