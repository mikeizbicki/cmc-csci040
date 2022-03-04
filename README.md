## CSCI040: ~Computing for the Web~ Introduction to Hacking
<!--
see: http://nifty.stanford.edu/2020/color-my-world/
-->

<center>
<img width='100%' src=hacker-way.jpg />
</center>

Important links:

1. [What Hackers get Paid](https://www.levels.fyi/comp.html?track=Data%20Scientist)

1. [Tech employers illegally collude to reduce salaries](https://en.wikipedia.org/wiki/High-Tech_Employee_Antitrust_Litigation)

## About the Instructor

|||
|-|-|
| Name | Mike Izbicki (call me Mike) |
| Email | mizbicki@cmc.edu |
| Office | Adams 216 |
| Office Hours | see [#85](https://github.com/mikeizbicki/cmc-csci040/issues/85) |
| Zoom Link | https://cmc-its.zoom.us/j/644800111 |
| Webpage | https://izbicki.me |
| Research | Machine Learning (see [izbicki.me/research.html](https://izbicki.me/research.html) for some past projects) |

Fun facts:
1. grew up in San Clemente (~1 hr south of Claremont)
1. 7 years in the navy
    1. nuclear submarine officer, personally converted >10g of uranium into pure energy
    1. worked at National Security Agency (NSA)
    1. left Navy as a [conscientious objector](https://www.nytimes.com/2011/02/23/nyregion/23objector.html)
1. phd/postdoc at UC Riverside
1. taught in [DPRK (i.e. North Korea)](https://pust.co)
1. currently on paternity leave

## About the Course

**General Information:**

1. There are no prerequisites for this course.

1. This course fulfills the math general ed requirements for CMC students.

   But, most students find it much harder than taking MATH030 (Calculus I).
   If you haven't taken calculus, expect that you will have to put in about twice the amount of work on this class than you would to take calculus and get the same grade.

1. This course is similar to [CS5 at Harvey Mudd](https://www.cs.hmc.edu/twiki/bin/view/CS5) or [CS51 at Pomona](http://www.cs.pomona.edu/~tzuyi/Classes/sp18/cs051p/).
    1. If you have already taken either of those courses,
       then you cannot take this course.
    1. If you are majoring in computer science at either of those schools,
       then you cannot take this course.
    1. This course is designed for CMC's 
        1. data science major,
        1. data science sequence,
        1. and computer science sequence.
    1. This course is more practical than the Mudd/Pomona courses.

       This course is especially designed to connect computer science to non-STEM subjects like
        1. economics,
        1. government,
        1. literature, and
        1. history.

1. This course cannot be taken CR/NC.

**Primary Learning Objectives:**

1. **Automate boring tasks** <-- this is a hacker's primary goal
1. Create static and dynamic web pages
1. Understand the basics of many programming languages:
    1. HTML
    1. CSS
    1. JavaScript
    1. Jinja
    1. SQL
    1. Markdown
    1. and **Python** <-- this is the main focus of the course
<!--1. Understand the basics of procedural and object oriented programming-->

**Secondary Learning Objectives:**

1. Introduction to [hacker culture](http://www.catb.org/esr/faqs/hacker-howto.html) and [open source software](https://opensource.com/resources/what-open-source)

1. Understand basic:
    1. internet infrastructure
    1. common programming jargon
        1. ["front end" versus "back end" development](https://www.coursereport.com/blog/front-end-development-vs-back-end-development-where-to-start)
        1. [test driven development](https://streamhacker.com/2009/02/05/test-driven-development-in-python/)
    1. [accessible development](https://www.w3.org/standards/webdesign/accessibility)
        1. allow blind people to use webpages
        1. allow non-English speaking / non-Americans to use your software
    1. web security
        1. technical details (you will learn to commit fraud in this class!)
        1. social implications
        1. government policy
        1. legal issues
    <!--
    1. [search engine optimization](https://moz.com/beginners-guide-to-seo)
    -->
1. Use real-world programming tools
    1. Python libraries actually in use at FAANG companies
    1. GitHub

**Textbook:**

All of our textbooks are [free as in beer](https://en.wiktionary.org/wiki/free_as_in_beer).
Some of them are [free as in speech](https://en.wiktionary.org/wiki/free_as_in_speech).

1. Shay Howe's [Learn to Code HTML & CSS](https://learn.shayhowe.com/html-css/).
1. Al Sweigart's [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/).
1. Other online resources as listed in the weekly schedule.

Hackers believe in the free exchange of information and often use the following websites to share textbooks and other knowledge:

1. https://b-ok.org
1. https://sci-hub.tw
1. https://thepiratebay.org

But most of the people who use these sites are [script kiddies](https://en.wikipedia.org/wiki/Script_kiddie).

**Grades:**

| category                      | points/assignment | approximate percentage |
| ----------------------------- | ----------------- | ---- |
| labs (weekly)                 | 5pts              | 20%  |
| quizzes (weekly)              | 10-20pts          | 40%  |
| projects (every 2-3 weeks)    | 10-40pts          | 40%  |

This will be a low-stress but very challenging class.

1. The course is low-stress because you have full control over what your grade will be.
    1. **No midterm/final exam.**
       Weekly quizzes ensure you don't fall behind on material, and if you bomb a quiz it's not a big deal.
    1. Weekly labs are automatically graded by Python.
       Keep working on them until you get 100%.
    1. Projects have TONs of extra credit opportunities.
       In the past, I've had students end the course with a 150%,
       and I've had other students choose not to complete certain projects because they would get an A without completing them.

1. The material is intrinsically *very* hard.
    1. That's why CS/DS majors get paid so much money... there's not many people willing to work hard enough to master these concepts.
    1. That's why we have an extra lab session each week (and so 50% more in-person instruction time).
       Also take advantage of office hours and the QCL.
    1. Historically, the average student needs to spend about 10 hours per week outside of class to get an A.
       About 50% of students will either:
       spend 15-20 hours per week and get an A-/A,
       or spend 10 hours per week and get a B/C.

1. The projects are designed to be fun, real-world projects:

    |     | Project                 | Due Date will be no earlier than |
    | --- | ----------------------- | ---------------- |
    | 0   | Building a Webpage      | Sunday, 12 Sep   |
    | 1   | Markdown compiler       | Sunday, 03 Oct   |
    | 2   | Data visualization      | Sunday, 10 Oct   |
    | 3   | Scraping ebay           | Sunday, 24 Oct   |
    | 4   | Reddit propaganda bot   | Sunday, 07 Nov   |
    | 5   | Twitter clone           | Sunday, 12 Dec   |

    There's also fewer projects than in CS5/CS51.
    Those courses have 1 project per week.

Your final grade will be computed according to the following table,
with one caveat.

| If your grade satisfies          | then you earn |
| -------------------------------- | ------------- |
| 95 &le; grade                    | A             |
| 90 &le; grade < 95               | A-            |
| 87 &le; grade < 90               | B+            |
| 83 &le; grade < 87               | B             |
| 80 &le; grade < 83               | B-            |
| 77 &le; grade < 80               | C+            |
| 73 &le; grade < 77               | C             |
| 70 &le; grade < 73               | C-            |
| 67 &le; grade < 70               | D+            |
| 63 &le; grade < 67               | D             |
| 60 &le; grade < 63               | D-            |
| 60 > grade                       | F             |

*CAVEAT:*
In order to earn an A/A- in the class, you must also complete one of the following tasks.

1. Read [Harry Potter and the Methods of Rationality](https://hpmor.com).
   This is a fanfic written by [Eliezer Yudkowsky](https://en.wikipedia.org/wiki/Eliezer_Yudkowsky),
   who is a famous [AI safety](https://futureoflife.org/ai-safety-research/) researcher.
   The premise is that Harry Potter's parents were both wizards and scientists,
   and the story introduces a lot of concepts important for AI safety and the philosophy of data science.

1. Watch the following shows/movies about hacking:

    1. Season 1 of Mr. Robot (available of [Amazon Prime](https://www.amazon.com/gp/video/detail/B00YBX664Q)).
       This is the most accurate portrayal of hacking in any movie, see for example [this article](https://www.pri.org/stories/how-realistic-are-hacks-mr-robot) and [this article](https://www.wired.com/2016/07/real-hackers-behind-mr-robot-get-right/).

    1. War Games (available on [Amazon Prime](https://www.amazon.com/Wargames-Matthew-Broderick/dp/B083FY4CDG/).
       This is a classic hacker movie and was quite realistic for what hacking looked like when the movie was released (1983).

    1. CitizenFour (available for free from the [Internet Archive](https://archive.org/details/Citizen.Four2014)).
       This is a documentary about Edward Snowden and the hacking that the NSA does.
       There's also a live-action movie called [Snowden](https://www.amazon.com/Snowden-Joseph-Gordon-Levitt/dp/B01LWYVHKV) that you could also choose to watch.

    1. Zero Days - Security Leaks for Sale (available for free on [youtube](https://www.youtube.com/watch?v=4BTTiWkdT8Q))

    <!--
    1. Season 1 of Hunted, [available online](https://www.channel4.com/programmes/hunted/on-demand/60136-001).
       This is a reality TV show about how your cellphones and web browsing traffic can let people track you.
    -->

See [Issue #79](https://github.com/mikeizbicki/cmc-csci040/issues/79) for instructions on how to get credit for completing these readings / viewings.

**Late Work Policy:**

You lose 20% on labs/projects for each day late.
It is still typically better to submit a correct assignment late than an incorrect one early.

If you have extenuating circumstances, contact me in advance of the due date and I may extend the due date for you.

If you collaborate with other students or visit the QCL for help with an assignment,
you get an automatic 2 day extension on any lab or project.

**Collaboration Policy:**

<!--
Harvard CS50:

> When asking for help, you may show your code to others, but you may not view theirs.

https://www.youtube.com/watch?v=r0z-yIp1PnE
-->

You are encouraged to discuss all labs and projects with other students,
subject to the following constraints:

1. you must be the person typing in all code for your assignments, and
1. you must not copy another student's code.

You may use any online resources you like as references.

Basically, I'm trusting you all to be adults.
You are ultimately responsible for ensuring you learn the material!
So do what will help you learn best.

*WARNING:*
All material in this class is cumulative.
If you work "too closely" with another student on an assignment,
you won't understand how to complete subsequent assignments,
and you will quickly fall behind.
You should view collaboration as a way to improve your understanding,
not as a way to do less work.

**COVID-19 Policy:**

I want to respect everyone's various comfort levels with COVID exposure.
Therefore:

1. you will be encouraged to work closely with other students in this class,
1. but you will not be required to work too closely (for example by sharing computers).

If you are quarantined and cannot come to class:

1. you are excused from the quizzes you miss and won't have to retake them;

1. you are still responsible for turning in labs/projects on time;

    1. unless you are also ill, then I will grant an appropriate extension
## Schedule

| Week | Date        | Topic                                                |
| ---- | ----------- | ---------------------------------------------------- |
| 0    | Mon, 30 Aug | Course intro                                         |
| 0    | Wed, 01 Sep | Web 1.0: HTML                                        |
| 0    | Fri, 03 Sep | *Lab:* GitHub                                        |
| 1    | Mon, 06 Sep | **NOCLASS: Labor Day**                               |
| 1    | Wed, 08 Sep | Web 1.0: CSS                                         |
| 1    | Fri, 10 Sep | *Lab:* Removing web ads                              |
| 2    | Mon, 13 Sep | Python: control flow                                 | <!-- last day to add -->
| 2    | Wed, 15 Sep | Python: control flow                                 |
| 2    | Fri, 17 Sep | *Lab:* SMS/Twilio                                    |
| 3    | Mon, 20 Sep | Python: lists                                        |
| 3    | Wed, 22 Sep | Python: dictionaries                                 |
| 3    | Fri, 24 Sep | *Lab:* basic algorithms/data structures              |
| 4    | Mon, 27 Sep | Python: strings                                      |
| 4    | Wed, 29 Sep | Python: files                                        |
| 4    | Fri, 01 Oct | *Lab:* markdown to html converter                    |
| 5    | Mon, 04 Oct | Python: JSON                                         |
| 5    | Wed, 06 Oct | Python: matplotlib                                   | <!-- low grade notice -->
| 5    | Fri, 08 Oct | *Lab:* Analyzing Trump's tweets                      |
| 6    | Mon, 11 Oct | Python: reddit                                       |
| 6    | Wed, 13 Oct | Python: reddit                                       |
| 6    | Fri, 15 Oct | *Lab:* Generating propaganda                         |
| 7    | Mon, 18 Oct | **NOCLASS: fall break**                              |
| 7    | Wed, 20 Oct | Python: reddit                                       |
| 7    | Fri, 22 Oct | *Lab:* RedditBots                                    |
| 8    | Mon, 25 Oct | Python: web scraping                                 |
| 8    | Wed, 27 Oct | Python: web scraping                                 |
| 8    | Fri, 29 Oct | *Lab:* Requests                                      | <!-- Halloween -->
| 9    | Mon, 01 Nov | Python: multilingual support (Unicode)               |
| 9    | Wed, 03 Nov | Python: multilingual support (Unicode)               |
| 9    | Fri, 05 Nov | *Lab:* machine translation                           |
| 10   | Mon, 08 Nov | Web 2.0: SQL                                         |
| 10   | Wed, 10 Nov | Web 2.0: SQL                                         |
| 10   | Fri, 12 Nov | *Lab:* SQL                                           |
| 11   | Mon, 15 Nov | Web 2.0: Flask                                       |
| 11   | Wed, 17 Nov | Web 2.0: Flask                                       |
| 11   | Fri, 19 Nov | *Lab:* Dynamic webpages                              | <!-- last day to withdraw with a W -->
| 12   | Mon, 22 Nov | Web 2.0: Flask                                       |
| 12   | Wed, 24 Nov | **NOCLASS: Thanksgiving**                            |
| 12   | Fri, 26 Nov | **NOCLASS: Thanksgiving**                            |
| 13   | Mon, 29 Nov | Web 2.0: Flask                                       |
| 13   | Wed, 01 Dec | Web 2.0: Flask                                       |
| 13   | Fri, 03 Dec | *Lab:*  AJAX                                         |
| 14   | Mon, 06 Dec | Web 2.0: Flask                                       |
| 14   | Wed, 08 Dec | Web 2.0: Flask                                       |
| 14   | Fri, 10 Dec | *Lab:* Final project                                 |

**No Final Exam.**
Final project will be due during exam week.

<!--Reading:

https://www.reddit.com/r/cscareerquestions/top/?sort=top&t=all

    1. [How a philosophy major from a liberal arts college with 2.4 GPA got jobs at Facebook and Uber making $300k as a data scientist](https://www.youtube.com/watch?v=YGflHj1SjA4&t=2m15s)

    1. [Data science expectations vs reality](https://www.youtube.com/watch?v=8LucP1wiX1g)

Tim Berner's Lee https://www.w3.org/People/Berners-Lee/

How the internet works: https://thesquareplanet.com/blog/how-the-internet-works/

Web architecture 101: https://engineering.videoblocks.com/web-architecture-101-a3224e126947

OPSEC: https://www.telegraph.co.uk/news/worldnews/northamerica/usa/11229241/FBIs-most-wanted-cyber-criminal-caught-out-by-pet-cat-password.html

reddit jsonp: https://www.reddit.com/r/programming/comments/cxh3a/we_just_added_jsonp_to_reddits_json_api/

jsfiddle

|-->


<!-- -->
<!--
[Quiz: if](https://realpython.com/quizzes/python-conditional-statements/)
[Quiz: operators](https://realpython.com/quizzes/python-operators-expressions/)
-->
<!--
| Week | Date | Topic | Assignment |
| --- | --- | --- | --- |
| 1  | Tues, 3 Sept  | Introduction | |
| 1  | Thur, 5 Sept  | HTML: Basics ([Howe](https://learn.shayhowe.com/html-css/), Lesson 1/2)<br/>CSS: Basics ([Howe](https://learn.shayhowe.com/html-css/), Lesson 3/4/5)  | HW 1<br/>Lab 1 |
| 2  | Tues, 10 Sept | HTML: google analytics / chrome dev console <br/>SEO: [backlinks](https://moz.com/learn/seo/backlinks), [Google SEO Page](https://support.google.com/webmasters/answer/7451184)<br/>Python: Basics/Flow Control/Functions ([Sweigart](https://automatetheboringstuff.com/), Chapters 1-3)  | |
| 2  | Thur, 12 Sept | Python: Basics/Flow Control/Functions ([Sweigart](https://automatetheboringstuff.com/), Chapters 1-3) | Lab 2|
| 3  | Tues, 17 Sept | **NO CLASS** (Mike at [ECML-PKDD](http://ecmlpkdd2019.org/)) | |
| 3  | Thur, 19 Sept | **NO CLASS** (Mike at [ECML-PKDD](http://ecmlpkdd2019.org/)) | |
| 4  | Tues, 24 Sept | Python: Basics/Flow Control/Functions ([Sweigart](https://automatetheboringstuff.com/), Chapters 1-3)<br/>[Python cheat sheet](https://perso.limsi.fr/pointal/python:memento) | Lab 3 <br/>[Quiz: data types](https://realpython.com/quizzes/python-data-types/) |
| 4  | Thur, 26 Sept | Python: Basics/Flow Control/Functions ([Sweigart](https://automatetheboringstuff.com/), Chapters 1-3) | Lab 4 <br/>[Quiz: variables](https://realpython.com/quizzes/python-variables/)  |
| 5  | Tues, 1 Oct   | Python: Lists ([Sweigart](https://automatetheboringstuff.com/), Chapter 4) | Lab 5<br/>In-class quiz: for loops<br/>[Quiz: lists](https://realpython.com/quizzes/python-lists-tuples/) |
| 5  | Thur, 3 Oct   | Python: Dictionaries ([Sweigart](https://automatetheboringstuff.com/), Chapter 5)<br/>Python: Libraries ([Appendix of Sweigart](https://automatetheboringstuff.com/appendixa/)) | Lab 6<br/>Lab 6b<br/>In-class quiz: while loops<br/>[Quiz: dicts](https://realpython.com/quizzes/python-dicts/) |
| 6  | Tues, 8 Oct   | Python: Strings ([Sweigart](https://automatetheboringstuff.com/), Chapter 6) | Lab 7<br/>[Quiz: strings](https://realpython.com/quizzes/python-strings/)<br/>In-class quiz: lists |
| 6  | Thur, 10 Oct  | [The beautiful soup library](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) | HW 2<br/>~~Quiz: Sets~~ |
| 7  | Tues, 15 Oct  | ~~Python: Regular Expressions ([Sweigart](https://automatetheboringstuff.com/), Chapter 7)~~<br/>[The requests library](https://realpython.com/python-requests/)<br/>Python: Files 1/2 ([Sweigart](https://automatetheboringstuff.com/), Chapter 8,9) | Lab 8<br/>Lab 9 (extra credit)<br/>[Quiz: files](https://realpython.com/quizzes/read-write-files-python/)<br/>~~HW 3~~ |
| 7  | Thur, 17 Oct  | Python: Files 1/2 ([Sweigart](https://automatetheboringstuff.com/), Chapter 8,9) | Lab 10 <br/>~~Quiz: lexical~~|
| 8  | Tues, 22 Oct  | **NO CLASS** (Fall Break) |
| 8  | Thur, 24 Oct  | ~~Python: Debugging ([Sweigart](https://automatetheboringstuff.com/), Chapter 10)~~<br/>[JSON Files](https://realpython.com/python-json/) | Lab 11 |
| 9  | Tues, 29 Oct  | [Matplotlib](https://realpython.com/python-matplotlib-guide/) | HW 4 |
| 9  | Thur, 31 Oct  | Python: Web Scraping ([Sweigart](https://automatetheboringstuff.com/), Chapter 11) | Lab 12 |
| 10 | Tues, 5 Nov   | **NO CLASS** (Mike at [CIKM](http://www.cikm2019.net/)) | |
| 10 | Thur, 7 Nov   | **NO CLASS** (Mike at [CIKM](http://www.cikm2019.net/)) | |
| 11 | Tues, 12 Nov  | Python: reddit ([praw tutorial](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html)) | |
| 11 | Thur, 14 Nov  | Python: reddit ([praw tutorial](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html))<br/>[madlib propaganda machines](https://hackernoon.com/more-than-a-million-pro-repeal-net-neutrality-comments-were-likely-faked-e9f0e3ed36a6) | HW 5<br/>Lab 13 |
| 12 | Tues, 19 Nov  | Python: other libraries ([awesome-python](https://github.com/vinta/awesome-python))| |
| 12 | Thur, 21 Nov  | Python: building CRUD webapps ([Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)) | |
| 13 | Tues, 26 Nov  | Python: building CRUD webapps ([Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)) | |
| 13 | Thur, 28 Nov  | **NO CLASS** (Thanksgiving) |  |
| 14 | Tues, 3 Dec   | Python: [database CRUD operations](https://www.tutorialsteacher.com/python/database-crud-operation-in-python) | HW 6 |
| 14 | Thur, 5 Dec   | Python: [database CRUD operations](https://www.tutorialsteacher.com/python/database-crud-operation-in-python) | Lab 14 |
| 15 | Tues, 10 Dec  | Python: building CRUD webapps ([Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world))| |
| 15 | Thur, 12 Dec  | Python: building CRUD webapps ([Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world))| |
-->

<!--
| 11 | Tues, 12 Nov  | Python: Email/SMS ([Sweigart](https://automatetheboringstuff.com/), Chapter 16) | HW 5 |
| 11 | Thur, 14 Nov  | Python: Unicode (Python docs, [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)) | |
| 12 | Tues, 19 Nov  | Javascript: Basics ([w3schools, JavaScript](https://www.w3schools.com/js/default.asp) | HW 6 |
| 12 | Thur, 21 Nov  | Javascript: DOM ([w3schools, DOM](https://www.w3schools.com/js/js_htmldom.asp)) |
| 13 | Tues, 26 Nov  | Javascript: BOM ([w3schools, BOM](https://www.w3schools.com/js/js_window.asp)) | |
-->
<!--
Python libraries:
* newspaper3k
* wikipedia
* googletrans
* twilio (SMS) + weather-api
* geopy
* langid.py
* https://github.com/vinta/awesome-python
Python libraries: newspaper3k, wikipedia, geopy, langid.py, googletrans | |
-->

<!--
Recursion
https://realpython.com/python-thinking-recursively/

Install Python: https://learnpythonthehardway.org/python3/ex0.html

Reddit bot: https://www.pythonforengineers.com/build-a-reddit-bot-part-1/

Twitter bot: https://realpython.com/twitter-bot-python-tweepy/

Traceback: https://realpython.com/python-traceback/

Classes: https://realpython.com/inheritance-composition-python/

Unicode Python3: https://realpython.com/python-encodings-guide/

Python tips: https://realpython.com/python-coding-interview-tips

Sorting: https://realpython.com/python-sort/

Command line interface: https://realpython.com/command-line-interfaces-python-argparse/

Basic IO: https://realpython.com/python-input-output/

PEP 20: https://www.python.org/dev/peps/pep-0020/
PEP 8: https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds

Use `doctest` for automatic grading: https://docs.python.org/3/library/doctest.html

Automate the boring stuff https://automatetheboringstuff.com/chapter2/

Scraping:
https://www.scrapehero.com/how-to-scrape-competitor-prices-from-ebay-com-using-python-and-lxml/
https://www.scrapehero.com/xpaths-and-their-relevance-in-web-scraping/
https://lxml.de/3.2/elementsoup.html

NSA:
https://www.reuters.com/article/us-usa-surveillance-watchdog-idUSBRE98Q14G20130927

Border agents checking social media:
https://news.ycombinator.com/item?id=20848359

South Africa surveillance:
https://news.ycombinator.com/item?id=20861729
https://www.iafrikan.com/2019/09/02/south-africa-mass-surveillance-spying-undersea-fiber-cables/
-->


<!--
## Self Grading

[An outlook on self-assessment of homework assignments in higher mathematics education](https://link.springer.com/article/10.1186/s40594-018-0146-z)

Also *Your* Job to Learn! Helping Students Reflect on their Learning Progress

Should you Allow your Students to Grade their own Homework?

Peer and Self Assessment in Massive Online Classes
-->

## Accommodations for Disabilities

I've tried to design the course to be as accessible as possible for people with disabilities.
(We'll talk a bit about how to design accessible software in class too!)
If you need any further accommodations, please ask.

I want you to succeed and I'll make every effort to ensure that you can.

<!--

make labs due during the lab session; -1 point penalty for submitting late

change the requirements of hw_00 to have:
- a legitimate title bar and consistent formatting between pages
- no broken links
- no inline styles/no style tags
- no broken html tags like "html>"

introduce pythontutor before doing python in vscode?

Trick questions:
 1. += vs =+
 1. while n:
        n //= 10
 1. for i in range(-5, 5):
        if i:
            do something

Functions:
1. Create functions with default valued arguments
1. Call functions with named arguments (in different orders)/variable number of arguments
1. Call functions from within functions, actually using the returned result (return vs print)

Exceptions:
1. Add ValueError to errors discussion
1. cover when the error happens midway through the try
1. when the error happens in the except clause
1. cover try/except within try/except

SQL:
1. More step-by-step lab instructions
1. Do lab with just SQL+Python before involving flask

================================================================================

More patterns:

students struggle with nested lists/dictionaries; do more examples early on

dictionary pattern where we have a list of items,
and we use dictionary keys as the items and values as the counts

dictionary/json pprint

wait for dictionaries with JSON?  students have a LOT of trouble with dictionary indexing

students don't understand functions and the difference of return/print

for loop flags; the reddit assignment looping to see if a comment has a reply needs a boolean flag; we should visit this patter earlier in the class

difference between pass vs continue

list like objects especially with praw not giving lists back

str(comment.author)

for comment in comments:
    do comment
comment

for word in string is wrong

if list == 0 instead of len(list)==0


for comment.reply in comments.reply


random.choice([])


blah(
    username=xxx
)
print(username) # generates an error


students don't understand the ? syntax in sql do quiz wth '?' vs ? and other insert syntax variations with python; last quiz was just sql, which wasn't enough; need for con.commit() and cur.fetchall()

insert into users (username,password) values (username=?,password=?);


students forget that you need parenthesis to call a function
con.commit
vs
con.commit()




request.form.get('message')
select message from messages;
message  <<-- students don't understand why you can't refer to just message in python

-->
