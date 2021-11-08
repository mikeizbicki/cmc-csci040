# HW 04: Reddit Bot

<img width=600px src=bots-bots-everywhere.jpg>

**Description:** 
You will create a reddit bot that posts messages about your favorite (or least favorite) politician.

**Due:**
Sunday, 21 November (recommended) / Sunday, 28 November (final).

Because your bots will be communicating with each other on reddit,
they must be running at the same time.
Therefore, there are no extensions possible for this assignment for any reason.

**Learning objectives:**

1. understand how bots spread propaganda online
1. integrate python programs with online social media
1. write and deploy python [daemons](https://en.wikipedia.org/wiki/Daemon_(computing))

## Instructions

1. Download the `bot.py` file to you computer.
   This file contains 6 tasks.
   Complete each of these tasks.

1. Once all of these tasks are complete,
   let your bot run continuously starting on 21 November until 28 November.
   It is okay to begin running your bot before 21 Nov.

1. Create a github repo for this project.
   The repo should contain:

    1. Your completed `bot.py` file (but not your `praw.ini` file!!!).
    1. A `README.md` file, properly formatted with markdown syntax, that:
        1. Clearly states which politician your bot is supporting or opposing.
        1. Provides a link to your favorite thread involving your bot, an image screenshot of the thread, and a short description of what you like about it.
           (Below each comment is a button labeled `permalink` that lets you link to a comment.)
        1. Includes the output of running the `bot_counter.py` file on your bot to count how many comments you've created.
           The output of this command must be inside of a markdown code block (i.e. use the triple backticks notation).
        1. Explains what you believe your score should be.
           Clearly state which tasks you complete/don't complete.

## Grading rubric

The assignment is worth 30 points total.

### Required Tasks

The following tasks are required, and total 20 points:

1. Each task in `bot.py` is worth 3 points.
   (6 tasks * 3 points/task = 18 points)

1. The github repo is worth 2 points.

### Optional Tasks

In order to earn full credit on the assignment,
you will have to complete some of the optional tasks.
There are many of these optional tasks,
and so it is possible to earn significant extra credit on this assignment.

You earn 2 points of extra credit for each of the following tasks you complete.

1. Getting at least 100 valid comments posted.

1. Getting at least 500 valid comments posted.

1. Getting at least 1000 valid comments posted.

1. Make your bot create new submission posts instead of just new comments.
   You can easily automate this process by scanning the top posts in your favorite sub (e.g. /r/liberal or /r/conservative) and posting them to the class sub.
   I recommend creating a separate python file for creating submissions and creating comments.

1. Create an "army" of 5 bots that are all posting similar comments.
   This will require creating 5 different reddit accounts.
   You can use the same code for each bot (but different `praw.ini` files with the corresponding login credentials).
   The challenge is keeping all 5 of these bots running simultaneously.
   Each bot needs to post at least 500 valid comments to get this extra credit.

1. Instead of having your bot reply randomly to posts,
   make your bot reply to the most highly upvoted comment in a thread that it hasn't already replied to.
   Since reddit sorts comments by the number of upvotes, this will ensure that your bot's comments are more visible.
   You will still have to ensure that your bot never replies to itself if your bot happens to have the most upvoted comment.

1. Have your bot upvote any comment or submission that mentions your favorite candidate.
   I recommend creating a separate python file for performing the upvotes,
   and you must be able to upvote comments contained within any submission in the class subreddit.

   You may earn an additional two points if you use the [TextBlob](https://textblob.readthedocs.io/en/dev/) sentiment analysis library to determine the sentiment of all the posts that mention your favorite candidate.
   If the comment/submission has positive sentiment, then upvote it;
   if the comment/submission has a negative sentiment, then downvote it.

   This extra credit is "grayhat" since it may violate reddit's TOS if not done correctly.

You earn 5 points of extra credit for each of the following tasks you complete.

1. Use a more sophisticated algorithm for generating the text of your comments.
   There are good python interfaces to the GPT-2 text generation algorithm, like [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple), but they can be a bit finicky to get working well.
   The [Markovify](https://github.com/jsvine/markovify) library provides an easier to use algorithm that's better than the MadLibs algorithm from lab, but not as good as GPT-2.
   If you're interested in trying for this extra credit,
   I'd be happy to discuss how to do this in office hours.

## Submission

Upload a link to your github repo to sakai.

**WARNING:**
If your github repo contains any reddit credentials,
you will lose -25 points on the assignment!!!
It is possible to get a negative score on this assignment.

**WARNING:**
Don't underestimate the difficulty of this assignment and put it off until the last minute.
Lots of surprising bugs always occur when your working on real world projects like this...

<img src=phd011406s.gif width=600px>
