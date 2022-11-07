# Project 04: Reddit Bot

<img width=600px src=bots-bots-everywhere.jpg>

**Description:** 
You will create a reddit bot that posts messages about your favorite (or least favorite) politician.

**Due:**
Sunday, 20 November (recommended) / Sunday, 27 November (final).

Because your bots will be communicating with each other on reddit,
they must be running at the same time.
Therefore, there are no extensions possible for this assignment for any reason.

**Learning objectives:**

1. understand how bots spread propaganda online
1. use website APIs
1. integrate python programs with online social media
1. write and deploy python [daemons](https://en.wikipedia.org/wiki/Daemon_(computing))

## Ethical/legal FAQ

This assignment raises many ethical and legal questions for students, faculty, and administrators.
This FAQ addresses these questions.

**Q1: Bots are bad for democracy.  Why would you want to teach students to make them?**

Bad bots spreading fake news have gotten a lot of media attention,
but many (most?) bots are actually good for society.
The community <a href=https://www.reddit.com/r/TheoryOfReddit/>/r/TheoryOfReddit</a> maintains a <a href=https://www.reddit.com/r/TheoryOfReddit/wiki/bots>wiki of reddit's most famous good bots</a>.
Here are some examples of useful reddit bots:

* https://www.reddit.com/user/stabbot

* https://www.reddit.com/user/autotldr

* https://www.reddit.com/r/Christianity/comments/irsxys/biblequotebot_is_beta/

* https://www.reddit.com/r/tippr/wiki/reddit-usage

* https://www.reddit.com/r/RemindMeBot/

* https://www.reddit.com/r/OutOfTheLoop/comments/9gv9xs/what_is_going_with_locationbot_and_what_does_it/

* https://www.reddit.com/user/GoodBot_BadBot

Other online social networks like Twitter also have <a href=https://www.poynter.org/tech-tools/2017/7-of-the-best-twitter-bots-in-journalism/>many good bots</a>.
One of my personal favorite bots is a Twitter bot named 
<a href=https://twitter.com/nyt_diff>@nyt_diff</a>.
This bot monitors the NYTimes webiste for edits made to articles after they've been published.
Although most of these edits are minor typo fixes,
some of these changes can be dramatic:

<center>
    <a href=https://twitter.com/nyt_diff/status/877586995731615744><img src=nyt_diff.png></a>
</center>

Maintaining records of these edits is important for promoting a transparent democracy,
and it wouldn't be possible without bots.

Students who complete this assignment will have the skills needed to both distinguish between good and bad bots online, and to make good bots.

**Q2: But is it legal to develop bots?**

Yes.
Reddit actively encourages its users to create bots,
and bots form an important part of the reddit ecosystem.

Reddit requires all bots to comply with <a href=https://github.com/reddit-archive/reddit/wiki/API>the API terms</a> and <a href=https://www.reddit.com/wiki/bottiquette>bottiquette</a>,
and students are required to review and comply with these documents.
This is fairly easy to do.
Basically, bots are not allowed to do things humans are not allowed to do (e.g. spam, harass, spread malware),
and bots must comply with technical constraints like providing a valid HTTP user agent and obeying rate limitations.

Outside of reddit, the legal status of bots is a more interesting question.
In 2019, the California Senate passed the <a href=https://www.thedailybeast.com/in-california-its-now-illegal-for-some-bots-to-pretend-to-be-human>Bolstering Online Transparency (BOT)</a> law that requires most political and commercial bots to clearly label themselves as bots.
This is an intuitively sensible regulation, but it has many subtle first ammendment implications and so legal scholars are currently unsure about it's constitutionality (see comments by <a href=https://www.politico.com/magazine/story/2018/11/27/bots-first-amendment-rights-222689/>Politico</a>, and <a href=https://www.eff.org/document/eff-letter-opposing-california-bot-disclosure-bill-sb-1001-first-amendment-concerns>Electronic Frontier Foundation</a>, and the <a href=https://knightcolumbia.org/content/cavalier-bot-regulation-and-the-first-amendments-threat-model>Knight First Ammendment Institute</a>).
Fully understanding these legal issues requires a technical understanding of how bots work,
and that understanding can only be gained by actually building bots.

**Q3: I've heard that most bots are run by foreign governments like Russia.  Don't you need a lot of resources and expertise to create a bot?**

No.
Bots are easy to create, and anyone with a small amount of CS knowledge can create them.
A major purpose of this assignment is to help students understand that bots are very easy pieces of software to write.

**Q4: How do you prevent unintended negative externalities of this assignment?**

Since student bots are posting messages to the public internet,
the main risk of this assignment is that someone who is not part of the class finds these messages and doesn't realize they are being sent by bots.
We take two measures to prevent this from happening:

1. We use specialized subreddits dedicated for class activities (e.g. [/r/cs40_22fall](https://reddit.com/r/cs40_22fall)),
and student bots are required to post only in these subreddits.
These subreddits are clearly marked as being only for class activities and that all posters are bots.

1. All student bots must explicitly label themselves as a bot by including the word "bot" in their username.

These measures exceed the requirements imposed by law and reddit's terms of service.

**Q5: Why do a potentially controversial assignment that raises ethical and legal considerations?**

The Association for Computing Machinery (ACM) is the main professional organization for computer scientists.
Their <a href=https://www.acm.org/code-of-ethics>Code of Ethics and Professional Conduct</a> begins by stating that computing professionals "should reflect upon the wider impacts of their work",
and this assignment gives students the technical foundation needed to reflect on the wider impacts of bots.

Furthermore, accreditation agencies like ABET <a href=https://www.abet.org/accreditation/accreditation-criteria/criteria-for-accrediting-engineering-programs-2020-2021/>require that we teach students ethics</a>.
These ethical discussions are traditionally completely separate from technical assignments.
But I believe that by incorporating ethics directly into the technical assignments,
the ethical considerations become much more salient and easier to engage with,
and the technical assignments also become more fun.


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

   For full credit, you must have at least 200 submissions, some of which should be self posts and some link posts.
   Duplicate submissions (i.e. submissions with the same title/selftext/url) do not count.

   You must create a new file `bot_submissions.py` and place all of the code in this new file.
   You should not modify the `bot.py` file to create submissions.

1. Create an "army" of 5 bots that are all posting similar comments.
   This will require creating 5 different reddit accounts.
   You can use the same code for each bot (but different `praw.ini` files with the corresponding login credentials).
   The challenge is keeping all 5 of these bots running simultaneously.
   Each bot needs to post at least 500 valid comments to get this extra credit.

1. Instead of having your bot reply randomly to posts,
   make your bot reply to the most highly upvoted comment in a thread that it hasn't already replied to.
   Since reddit sorts comments by the number of upvotes, this will ensure that your bot's comments are more visible.
   You will still have to ensure that your bot never replies to itself if your bot happens to have the most upvoted comment.

1. Have your bot upvote any comment or submission that mentions your favorite candidate (or downvote submission mentioning a candidate you do not like).

   You must create a separate python file `bot_vote.py` for performing the upvotes.
   This file must loop over all submissions in the class subreddit and perform the up/down voting on all comments in each submission.

   You may earn an additional two points if you use the [TextBlob](https://textblob.readthedocs.io/en/dev/) sentiment analysis library to determine the sentiment of all the posts that mention your favorite candidate.
   If the comment/submission has positive sentiment, then upvote it;
   if the comment/submission has a negative sentiment, then downvote it.

   This extra credit is "grayhat" since it may violate reddit's TOS if not done correctly.

   Your code must run on at least 100 submissions and all of the comments within those submissions (up to 500 comments total per submission) for the full extra credit.
   Not all of these submissions/comments need to be upvoted if they do not match your particular criteria for voting.

You earn 5 points of extra credit for each of the following tasks you complete.

1. Use a more sophisticated algorithm for generating the text of your comments.
   There are good python interfaces to the GPT-2 text generation algorithm, like [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple), but they can be a bit finicky to get working well.
   The [Markovify](https://github.com/jsvine/markovify) library provides an easier to use algorithm that's better than the MadLibs algorithm from lab, but not as good as GPT-2.
   If you're interested in trying for this extra credit,
   I'd be happy to discuss how to do this in office hours.

You may additionally propose more extra credit tasks that you would like to complete.

## Negative Points

There are many ways to lose points on this assignment.

1. If your github repo contains any reddit credentials (e.g. a `praw.ini` file or passwords directly in the code),
    you will lose -25 points on the assignment.

1. If your bot posts to a subreddits not specifically designed for this course,
    you will lose -25 points on the assignment.

    You may create your own subreddits for debugging purposes,
    and posting to these subreddits will not result in a point deduction.

If you lose enough points to go below 0 points, then you will receive negative points,
and it would have been better to not complete the assignment at all.

## Submission

Upload a link to your github repo to sakai.

**WARNING:**
Don't underestimate the difficulty of this assignment and put it off until the last minute.
Lots of surprising bugs always occur when your working on real world projects like this...

<img src=phd011406s.gif width=600px>
