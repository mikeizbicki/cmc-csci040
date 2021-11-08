# Week 10: Reddit Bots I

<center>
<img width=400px src=duty_calls.png />
</center>

**Monday/Wednesday:**
We will be covering how to use the PRAW library this week for making reddit bots.
The textbook does not cover this topic,
but you can find the library's (excellent) documentation here:
https://praw.readthedocs.io/

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

1. We use a specialized subreddit dedicated for class activities,
and student bots are required to post only in this subreddit.
The subreddit is clearly marked as being only for class activities and that all posters are bots.

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

## Lab

See [/hw_04/lab-PRAW](/hw_04/lab-PRAW).
