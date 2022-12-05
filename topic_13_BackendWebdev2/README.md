# Week 14: Flask II

<center>
<img width=400px src=lkiuta60nio31.jpg />
</center>

We'll be creating a login/logout system for our Twitter clone project.
The references for this week are the same as last week.

There's 3 topics we'll need to cover:

**Topic 1:** HTML Forms

1. pass key/value pairs to ONE route
1. two methods:
    1. GET: key/value pairs in the URL
    1. POST: key/value pairs not in the URL

**Topic 2:** Cookies

1. pass key/value pairs to ALL routes
1. key/value pairs not in the URL

**Topic 3:** SQL Injection

1. Common method for breaking poorly designed sites

<img src=exploits_of_a_mom.png width=600px>

## Lab

**About:**

This is an optional lab worth +5pts EC.
It's hard, but fun :)

**Due:**

Friday 16 Dec (same day as the project)

**Background:**

[Stripe](https://stripe.com/) is a famous company that provides an easy-to-use library for processing credit card payments on webpages.
Because they process billions of dollars in payments,
they need great security.

The standard way to improve the security of web applications is through "bug bounties."
In stripe's bug bounty program (you can find [the rules here](https://hackerone.com/stripe?type=team)),
they invite everyone in the world to hack into their system.
If you find a bug that let's you break something,
they'll pay you $25000,
then fix the bug so that their system is more secure in the future.
These bug bounty programs provide a legal avenue for "ethical hackers" to make money by breaking into computer systems,
and [hundreds of millions of dollars](https://www.zdnet.com/article/hackerones-2020-top-10-public-bug-bounty-programs/) have been payed out by companies via these programs.

Stripe also tries to teach new programmers about security and how to find bugs that will qualify for these bounties through Capture the Flag (CTF) competitions.
These CTFs typically have many levels:
1. Each level has a webpage that you need to break into.
2. When you successfully break into one level, you are given access to the next level.
CTFs are extremely popular, and you can find a list of expert-level CTFs at https://ctftime.org/

**What to do:**

The Level 3 website from Stripe's 2012 CTF uses Flask and has a SQL injection vulnerability.
For this lab, you should:
1. Download [level 3](https://github.com/stripe-ctf/stripe-ctf-2.0/tree/master/levels/3) and follow the instructions for running the level.
   (Note that this CTF uses python version 2 instead of version 3, so you'll have to download the older version to get it to run.)
1. Successfully login as the `bob` user using SQL injection.
1. Meet with me and explain how your exploit works.

> **NOTE:**
>
> It is considered unseemly in CTF competitions to share the secrets of a level with someone else.
> Therefore, in this lab, you should also not just share the secrets with someone else.
> If you work with other people on this lab (which is still 100% okay),
> you'll all need to meet with me at the same time to walk through your solution.

<!--
## Closing remarks

Main takeaways from this class:

1. Hackers build stuff, they don't break it

   Hacker mantra:
    1. Laziness is good
    1. Boredom is evil
    1. So automate the boring stuff

1. Hackers get paid a lot of money

    1. What they do is hard
        1. If code isn't basically perfect, then it's basically worthless
        1. But it's not TOO hard:
           
           You can all learn to do it if you're willing to put in the effort

    1. What they do impacts everything in society
        1. Build webpages (HW0 / HW5)
        1. Monitor foreign governments (lab)
        1. Scrape webpages for business information (HW3)
        1. Build cool visualizations (HW2)
        1. Unicode => not just English speakers

    1. Good hackers (as in high-quality, not righteous) know how to break stuff, because strong defense requires knowing offense
        1. SQL injection (HW5)
            - always validate your inputs
        1. Password cracking (lab)
            - use good passwords
            - don't reuse passwords between sensitive accounts
        1. Fake news bots (HW4)
            - legal defenses require a deep understanding of the good bots so that you don't make those illegal as well
            - CSCI145/MATH166 Data Mining covers techniquess for finding and stopping the bad bots
        1. **If you see someone talking about computer security, but they don't know how to code, they're a fraud.**
           This applies to basically all government/defense workers/contractors...
           To see why, compare the salaries for Google employees to government employees.

I'd love to see you all in future CS classes :)
-->
