# Topic 14: Last Day of Class :)

<center>
<img width=400px src=lkiuta60nio31.jpg />
</center>

**Announcements (6 May 2026)**


- Project demos: <https://github.com/mikeizbicki/cmc-csci040/tree/2026spring/project_05_twitter_clone>

- Coding help:

    - I will be in my office most of Thursday/Friday.  Feel free to drop in or post an issue to schedule a concrete time.

## Notes

Beware of SQL injection in your project.

<img src=exploits_of_a_mom.png width=600px>

1. These attacks happen in the real world, all the time.
    1. There is a [company in the UK](https://www.schneier.com/blog/archives/2017/01/an_sql_injectio.html) whose legal name is a SQL injection vulnerability.
        So even just loading official UK government documents can break your programs if they're not designed carefully.

1. **To prevent SQL injection:** always use sqlite's binding syntax (`?`) for inserting information into the database

## Lab

**About:**

This is an optional lab worth +4pts EC.
It's hard, but fun :)

**Due:**

Whenever you demo the project.

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

## Closing remarks

Main takeaways from this class:

1. Hackers build stuff, they don't break it

   Hacker mantra:
    1. Laziness is good
    1. Boredom is evil
    1. So automate the boring stuff

1. Hackers get paid a lot of money

    1. <https://www.levels.fyi>

    1. What they do is hard
        1. If code isn't basically perfect, then it's basically worthless

            <img src=img/debugging.png width=400px />

        1. But it's not TOO hard:
           
           You can all learn to do it if you're willing to put in the effort

    1. Good hackers (as in high-quality, not righteous) know how to break stuff, because strong defense requires knowing offense
        1. SQL injection
            - always validate your inputs
        1. Password cracking (lab)
            - use good passwords
            - don't reuse passwords between sensitive accounts
        1. **If you see someone talking about computer security, but they don't know how to code, they're a fraud.**

           This applies to basically all government/defense workers/contractors...
           To see why, compare the salaries for Google employees to government employees.

1. We haven't yet studied "real computer science"

    1. "real CS" studies
        1. how to prove code is correct?
        1. what can AI never do?
        1. it's basically all math

            <img src=alwayshasbeen.jpg width=400px />

    1. I'd love to see you all in future CS classes :)

**Course Evals**

Please submit them!

The following specific feedback is particularly useful:
- which assignments were fun/hard/useful/etc
- where you found the best help (AI/QCL/classmates/office hours/etc)
