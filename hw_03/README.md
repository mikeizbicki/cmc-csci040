# HW 3: Creating a reddit bot

![comic](phd011406s.gif)

**Description:** 
You will create a reddit bot for spreading political propaganda about your favorite (or least favorite) US presidential candidate.

**Due:**
Sunday, 25 October / Tuesday, 3 Nov

*There are no extensions possible for this assignment!!!*

**Learning objectives:**

1. understand how bots spread propaganda online
1. integrate python programs with online social media
1. write and deploy python [daemons](https://en.wikipedia.org/wiki/Daemon_(computing))

## Instructions

1. Download the `bot.py` file to you computer.  This file contains 6 tasks.  Complete each of these tasks.

1. Once all of these tasks are complete, let your bot run continuously starting on 25 October and ending 3 Nov.  It is okay to begin running your bot before 26 Nov.

1. Create a github repo for this project.  The repo should contain:

    1. your completed `bot.py` file (but not your `praw.ini` file!!!)
    1. a `README.md` file, properly formatted with markdown syntax, that:
        1. clearly states which candidate your bot is supporting or opposing.
        1. provides a link to your favorite thread involving your bot, an image screenshot of the thread, and a short description of what you like about it.  (Below each comment is a button labeled `permalink` that lets you link to a comment.)
        1. includes the output of running the `bot_counter.py` file on your bot to count how many comments you've created; the output of this command must be inside of a markdown code block (i.e. use the triple backticks notation)
        1. explains what you believe your score should be (clearly state which tasks you complete/don't complete).  

## Grading rubric

Each task is worth 2 points.  (6 tasks * 2 points/task = 12 points)

The github repo is worth 2 points.

Getting at least 100 comments posted is worth another 2 points.

NOTE: 
The assignment is worth a total of 20 points, but their are only 16 points assigned above.
Therefore, if you complete only the "required" parts of the assignment, you will receive a 16/20.
To earn a 20/20, you must complete some of the extra credit below.
There are 21 possible extra credit points you can earn,
and so the maximum possible score is 37/20.

## Extra credit

The following tasks are worth 1 point each:

1. Have your bot upvote any comment mentioning your favorite candidate.

1. Have your bot upvote any submission mentioning your favorite candidate.

1. Make your bot reply to highly upvoted comments before replying to lower upvoted comments.  (HINT: sort the `comments_without_replies` list by the score of the comment using the `key` parameter to the `sorted` function; [see the python docs for examples](https://docs.python.org/3/howto/sorting.html)) 

1. If your bot writes more than 500 comments, you get this extra credit

1. If your bot writes more than 1000 comments, you get this extra credit

The following tasks are worth 2 points each:

1. Have your bot post new submissions to the /r/csci040 subreddit.  These submissions should be from the top submissions of a political subreddit that supports your favorite presidential candidate (e.g. /r/politics or /r/conservative).  Your bot must post at least 20 of these submissions to receive the extra credit.

1. Create an army of at least 10 bots that all upvote posts according to the same criteria.  This will let you manipulate which posts/comments are the most upvoted, and therefore the most read.  If your bot army contains 30 bots you'll get an additional 2 points of extra credit.

1. Use the [textblob](https://textblob.readthedocs.io/en/dev/quickstart.html) library to measure the sentiment of every comment/submission.
   If it mentions your favorite candidate with a positive sentiment, then upvote it;
   if it mentions your favorite candidate with a negative sentiment, then downvote it.
   Conversely, if it mentions a candidate you don't like with positive sentiment, then downvote it;
   if it mentions a candidate you don't like with negative sentiment, then upvote it.
   **If you complete this extra credit, you also get both of the 1 point extra credits for upvoting.**

The following task is worth up to 5 points:

1. Have the responses of your bot somehow depend on what the comment you are replying to is saying.  For example, if you are writing a bot that supports Trump, you might detect if the previous comment talks about Biden.  If it does, you might reply `Biden sucks, Trump is better.`  Alternatively, you might detect that the previous comment mentioned Trump with a negative sentiment and reply `I disagree, Trump is actually really great.`  The amount of extra credit you get for this will vary depending on the creativity of your idea.

1. Use the GPT-2 model to generate complex political messages.  See these links for tutorials.

    * https://www.reddit.com/r/talkwithgpt2bots/comments/gc26tf/make_your_own_gpt2_bot_tutorial_and_script/

    * https://bonkerfield.org/2020/04/twenty-minute-gpt2-reply-bot/

**You can suggest other ways to get extra credit as well, and I'll almost certainly say yes.**

## Submission

Upload a link to your github repo to sakai.

**If your github repo contains any reddit credentials, you will lose -25 points on the assignment!!!**

