# HW 5: Creating a reddit bot

**Description:** 
You will create a reddit bot for spreading political propaganda about your favorite (or least favorite) US presidential candidate.

**Due:** Tuesday, 26 November / Tuesday, 3 Dec

**Learning objectives:**

1. understand how bots spread propaganda online
1. integrate python programs with online social media
1. write and deploy python [daemons](https://en.wikipedia.org/wiki/Daemon_(computing))

## Instructions

1. Download the `bot.py` file to you computer.  This file contains 8 tasks.  Complete each of these tasks.

1. Once all of these tasks are complete, let your bot run continuously starting on 26 November and ending 3 Dec.  It is okay to begin running your bot before 26 Nov to begin testing it.

1. Create a simple html webpage for this project.  The webpage should:

    1. Clearly state which political candidate your bot is supporting or opposing.
    1. Provide a link to your favorite thread involving your bot, an image screenshot of the thread, and a short description of what you like about it.  (Below each comment is a button labeled `permalink` that lets you link to a comment.)
    1. Explain what you believe your score should be (clearly state which tasks you complete/don't complete).  

## Grading rubric

Each task is worth 10 points.

The webpage is worth 10 points.

NOTE: The assignment is worth a total of 100 points, but their are only 90 points assigned above.
Therefore, if you complete only the "required" parts of the assignment, you will receive a 90/100.
To earn a 100/100, you must complete some of the extra credit below.
There are 60 possible extra credit points you can earn,
and so the maximum possible score is 150/100.

## Extra credit

The following tasks are worth 5 points each:

1. Have your bot upvote any comment mentioning your favorite political candidate.

1. Make your bot reply to highly upvoted comments before replying to lower upvoted comments.  (HINT: sort the `comments_without_replies` list by the score of the comment using the `key` parameter to the `sorted` function; [see the python docs for examples](https://docs.python.org/3/howto/sorting.html)) 

1. If your bot writes more than 200 comments, you get this extra credit

The following tasks are worth 10 points each:

1. Have your bot post new submissions to the /r/csci040 subreddit.  These submissions should be from the top submissions of a political subreddit that supports your favorite presidential candidate.  Your bot must post at least 20 of these submissions.

1. Create an army of at least 10 bots that all upvote posts according to the same criteria.  This will let you manipulate which posts/comments are the most upvoted, and therefore the most read.  If your bot army contains 25 bots you'll get an additional 5 points of extra credit.

The following task is worth up to 25 points:

1. Have the responses of your bot somehow depend on what the comment you are replying to is saying.  For example, if you are writing a bot that supports Trump, you might detect if the previous comment talks about Bernie Sanders.  If it does, you might reply `Bernie sucks, Trump is better.`  Alternatively, you might detect that the previous comment mentioned Trump with a negative sentiment and reply `I disagree, Trump is actually really great.`  The amount of extra credit you get for this will vary depending on the creativity of your idea.

**You can suggest other ways to get extra credit as well, and I'll almost certainly say yes.**

## Submission

Upload your `bot.py` file to sakai and a link to your project webpage.
Be sure to remove your password information from the file before uploading.
**If you don't, you will lose -30 points.**

