# CSCI040: Computing for the Web

## About the Instructor

|||
|-|-|
| Name | Mike Izbicki (you can call me either Mike or Prof Izbicki) |
| Email | mizbicki@cmc.edu |
| Office | Adams 216 | 
| Office Hours | Tuesday/Thursday 2:40-4:10 or by appointment ([see my schedule](https://outlook.office365.com/owa/calendar/45eb28fd4e4f45f4b0d120d17676d937@ClaremontMcKenna.edu/a46ebec5e46b4328abcb964af38795935165582125062542146/calendar.html));<br/> if my door is open, feel free to come in |
| Webpage | [izbicki.me](https://izbicki.me) |
| Research | Machine Learning (see [izbicki.me/research.html](https://izbicki.me/research.html) for some past projects) |
| Fun Facts | grew up in San Clemente, 7 years in the navy, phd/postdoc at UC Riverside, taught in DPRK |

I like having lunch with students and getting to know you better.
If you want to get lunch, use [my bookings page](https://outlook.office365.com/owa/calendar/MeetwithMike@claremontmckenna.onmicrosoft.com/bookings/) to schedule a time.

## About the Course

This course is a first course in computer programming,
and is similar to [CS5 at Harvey Mudd](https://www.cs.hmc.edu/twiki/bin/view/CS5) or [CSCI 051 at Pomona](http://www.cs.pomona.edu/~tzuyi/Classes/sp18/cs051p/).
The difference is that CS40 is designed specifically for the computer science and data science sequences at CMC,
but **is not suitable for computer science majors**.
The focus of those courses is to teach computer science theory,
the focus of this course is much more practical.

**Primary Learning Objectives:**

1. **Automate boring tasks**
1. Create static and dynamic web pages
1. Understand the basics of HTML, CSS, JavaScript, and Python
<!--1. Understand the basics of procedural and object oriented programming-->

**Secondary Learning Objectives:**

1. Understand basic:
    1. ["front end" and "back end" development](https://www.coursereport.com/blog/front-end-development-vs-back-end-development-where-to-start)
    1. [test driven development](https://streamhacker.com/2009/02/05/test-driven-development-in-python/)
    1. [accessible development](https://www.w3.org/standards/webdesign/accessibility)
    1. internet infrastructure
    1. web security
    1. [search engine optimization](https://moz.com/beginners-guide-to-seo)
1. Use Python libraries
1. Be able to "talk" with computer scientists

**Textbook:**

1. Shay Howe's *Learn to Code HTML & CSS*, which is [freely available online here](https://learn.shayhowe.com/html-css/).
1. Al Sweigart's *Automate the Boring Stuff with Python*, which is [freely available online here](https://automatetheboringstuff.com/).
1. Other online resources as listed in the schedule below.

**Grades:**

| Category          | Percent |
| ----------------- | ------- |
| Homework          | 50      |
| Labs              | 30      |
| Quizzes (online)  | 10      |
| Quizzes (class)   | 10      |

<!--
| If your grade satisfies          | then you earn |
| -------------------------------- | ------------- |
| 93 &le; grade                    | A             |
| 90 &le; grade < 93               | A-            |
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
-->

**Late Work Policy:**

You lose 10% on the assignment for each day late.
If you have extenuating circumstances, contact me in advance of the due date and I may extend the due date for you.

## Schedule
<!--Reading: 

Tim Berner's Lee https://www.w3.org/People/Berners-Lee/

How the internet works: https://thesquareplanet.com/blog/how-the-internet-works/

Web architecture 101: https://engineering.videoblocks.com/web-architecture-101-a3224e126947

OPSEC: https://www.telegraph.co.uk/news/worldnews/northamerica/usa/11229241/FBIs-most-wanted-cyber-criminal-caught-out-by-pet-cat-password.html

reddit jsonp: https://www.reddit.com/r/programming/comments/cxh3a/we_just_added_jsonp_to_reddits_json_api/

jsfiddle

|-->

<!-- Cheat Sheet: https://perso.limsi.fr/pointal/python:memento -->

| Week | Date | Topic | Assignment |
| --- | --- | --- | --- |
| 1  | Tues, 3 Sept  | Introduction | |
| 1  | Thur, 5 Sept  | HTML: Basics ([Howe](https://learn.shayhowe.com/html-css/), Lesson 1/2)<br/>CSS: Basics ([Howe](https://learn.shayhowe.com/html-css/), Lesson 3/4/5)  | HW 1<br/>Lab 1 |
| 2  | Tues, 10 Sept | HTML: google analytics / chrome dev console <br/>SEO: [backlinks](https://moz.com/learn/seo/backlinks), [Google SEO Page](https://support.google.com/webmasters/answer/7451184)<br/>Python: Basics/Flow Control/Functions ([Sweigart](https://automatetheboringstuff.com/), Chapters 1-3)  | |
| 2  | Thur, 12 Sept | Python: Basics/Flow Control/Functions ([Sweigart](https://automatetheboringstuff.com/), Chapters 1-3) | Lab 2|
| 3  | Tues, 17 Sept | **NO CLASS** (Mike at [ECML-PKDD](http://ecmlpkdd2019.org/)) | |
| 3  | Thur, 19 Sept | **NO CLASS** (Mike at [ECML-PKDD](http://ecmlpkdd2019.org/)) | |
| 4  | Tues, 24 Sept | Python: Basics/Flow Control/Functions ([Sweigart](https://automatetheboringstuff.com/), Chapters 1-3) | Lab 3 <br/>[Quiz: data types](https://realpython.com/quizzes/python-data-types/) |
| 4  | Thur, 26 Sept | Python: Basics/Flow Control/Functions ([Sweigart](https://automatetheboringstuff.com/), Chapters 1-3) | Lab 4 <br/>[Quiz: variables](https://realpython.com/quizzes/python-variables/)<br/>[Quiz: if](https://realpython.com/quizzes/python-conditional-statements/)<!--<br/>[Quiz: operators](https://realpython.com/quizzes/python-operators-expressions/)-->  |
| 5  | Tues, 1 Oct   | Python: Lists ([Sweigart](https://automatetheboringstuff.com/), Chapter 4) | Lab 5<br/>[Quiz: loops](https://realpython.com/quizzes/python-while-loop/)<br/>[Quiz: lists](https://realpython.com/quizzes/python-lists-tuples/) |
| 5  | Thur, 3 Oct   | Python: Dictionaries ([Sweigart](https://automatetheboringstuff.com/), Chapter 5) | Lab 6<br/>HW 2<br/>[Quiz: dicts](https://realpython.com/quizzes/python-dicts/) |
| 6  | Tues, 8 Oct   | Python: Strings ([Sweigart](https://automatetheboringstuff.com/), Chapter 6) | Lab 7<br/>[Quiz: strings](https://realpython.com/quizzes/python-strings/) | 
| 6  | Thur, 10 Oct  | Python: Regular Expressions ([Sweigart](https://automatetheboringstuff.com/), Chapter 7) | Lab 8<br/>[Quiz: sets](https://realpython.com/quizzes/python-sets/) |
| 7  | Tues, 15 Oct  | Python: Files ([Sweigart](https://automatetheboringstuff.com/), Chapter 8) | Lab 9<br/>[Quiz: files](https://realpython.com/quizzes/read-write-files-python/)<br/>HW 3 |
| 7  | Thur, 17 Oct  | Python: Files 2 ([Sweigart](https://automatetheboringstuff.com/), Chapter 9) | Lab 10 <br/>[Quiz: lexical](https://realpython.com/quizzes/python-program-structure/)|
| 8  | Tues, 22 Oct  | **NO CLASS** (Fall Break) |
| 8  | Thur, 24 Oct  | Python: Debugging ([Sweigart](https://automatetheboringstuff.com/), Chapter 10) | | 
| 9  | Tues, 29 Oct  | Python: Web Scraping ([Sweigart](https://automatetheboringstuff.com/), Chapter 11) | HW 4 |
| 9  | Thur, 31 Oct  | Python: Time ([Sweigart](https://automatetheboringstuff.com/), Chapter 15) | |
| 10 | Tues, 5 Nov   | **NO CLASS** (Mike at [CIKM](http://www.cikm2019.net/)) | |
| 10 | Thur, 7 Nov   | **NO CLASS** (Mike at [CIKM](http://www.cikm2019.net/)) | |
| 11 | Tues, 12 Nov  | Python: Email/SMS ([Sweigart](https://automatetheboringstuff.com/), Chapter 16) | HW 5 |
| 11 | Thur, 14 Nov  | Python: Unicode (Python docs, [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)) | |
| 12 | Tues, 19 Nov  | Javascript: Basics ([w3schools, JavaScript](https://www.w3schools.com/js/default.asp) | HW 6 |
| 12 | Thur, 21 Nov  | Javascript: DOM ([w3schools, DOM](https://www.w3schools.com/js/js_htmldom.asp)) |
| 13 | Tues, 26 Nov  | Javascript: BOM ([w3schools, BOM](https://www.w3schools.com/js/js_window.asp)) | |
| 13 | Thur, 28 Nov  | **NO CLASS** (Thanksgiving) |  |
| 14 | Tues, 3 Dec   | Javascript: AJAX ([w3schools, AJAX](https://www.w3schools.com/js/js_ajax_intro.asp)) | |
| 14 | Thur, 5 Dec   | Python: Flask ([Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)) | HW 7 |
| 15 | Tues, 10 Dec  | Python: Flask ([Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world))| |
| 15 | Thur, 12 Dec  | Python: Flask ([Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world))| |

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

## Collaboration Policy

You are encouraged to discuss all labs, homeworks, and online quizzes with other students,
subject to the following constraints:

1. you must be the person typing in all code for your assignments, and
1. you must not copy another student's code.

You may use any online resources you like as references.

<!--
## Self Grading

[An outlook on self-assessment of homework assignments in higher mathematics education](https://link.springer.com/article/10.1186/s40594-018-0146-z)

Also *Your* Job to Learn! Helping Students Reflect on their Learning Progress

Should you Allow your Students to Grade their own Homework?

Peer and Self Assessment in Massive Online Classes
-->

## Accommodations for Disabilities

I want you to succeed and I'll make every effort to ensure that you can.
If you need any accommodations, please ask.

If you have already established accommodations with Disability Services at CMC, please communicate your approved accommodations to me at your earliest convenience so we can discuss your needs in this course. You can start this conversation by forwarding me your accommodation letter. If you have not yet established accommodations through Disability Services, but have a temporary health condition or permanent disability (conditions include but are not limited to: mental health, attention-related, learning, vision, hearing, physical or health), you are encouraged to contact Assistant Dean for Disability Services & Academic Success, Kari Rood, at disabilityservices@cmc.edu to ask questions and/or begin the process. General information and the Request for Accommodations form can be found at the CMC DOS Disability Service’s website. Please note that arrangements must be made with advance notice in order to access the reasonable accommodations. You are able to request accommodations from CMC Disability Services at any point in the semester. Be mindful that this process may take some time to complete and accommodations are not retroactive. It is important to Claremont McKenna College to create inclusive and accessible learning environments consistent with federal and state law. If you are not a CMC student, please connect with the Disability Services Coordinator on your campus regarding a similar process.

