# Topic 02: Python

<img width=500px src=img/two-states-of-programmers.png />

**Announcements (Mon 2026-02-02):**

1. Quiz Wednesday on CSS selectors

    1. any physical notes allowed (both printed/handwritten)
    1. no electronic devices

1. Homework due Tuesday (or Thursday with collaboration)

1. Grades updated (still 4 students who need to submit/resubmit lab)

1. Today in class: prepare for python quiz

    1. quiz notes packet can be found at: <https://github.com/mikeizbicki/quiz/blob/master/quiz_python/topic02_basics.pdf>.

## Prelecture Tasks

<!--
NOTE:
    Need raw strings for homework doctests!
    Need \n \t \r
-->

1. Download and install the latest version of python for your system by following the [VSCode Python quickstart tutorial](https://code.visualstudio.com/docs/python/python-quick-start).

    If you can get to the step labeled [run](https://code.visualstudio.com/docs/python/python-quick-start#_run), then you have correctly installed python.

1. (optional) Python review:

    We will cover chapters 1-7 in [Al Sweigart's *Automate the Boring Stuff*](https://automatetheboringstuff.com/2e/).
    Al has made a series of videos that accompany his textbook.
    If you do not have prior python experience, you are encouraged to review the book and videos before class.
    The videos are less than 2 hours in length total.

    1. (okay to skip) [Lesson 1](https://www.youtube.com/watch?v=1F_OgqRuSdI&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW)

        Al Swigart uses a text editor called IDLE in his videos.
        You are welcome to install IDLE in order to more closely follow allong with Al's videos.

        We will continue to use VSCode in class.

    1. [Lesson 2](https://www.youtube.com/watch?v=7qHMXu99d88&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=2)

        Key terms you should know from the video:

        1. Expression

        1. Value

        1. Operator

        1. Order of operations

        1. Data type

        1. Ints

        1. Floats

        1. Strings

        1. Concatenation

        1. Replication

        1. Variable

        1. Evaluation

        1. Statement

    1. [Lesson 3](https://www.youtube.com/watch?v=buMTH6ICnqk&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=3)

        Key terms you should know from the video:

        1. comment

        1. functions

        1. arguments

        1. `print`

        1. `input`

        1. `len`

        1. `str`

        1. `int`

        1. `float`

    1. [Lesson 4](https://www.youtube.com/watch?v=4XA9CKJJbr4&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=4)

        Key terms you should know from the video:

        1. boolean values

        1. boolean operators

        1. comparison operators

        1. `True`, `False`

        1. `=`, `==`, `!=`, `<`, `<=`, `>`, `>=`

        1. `and`, `or`, `not`

    1. [Lesson 5](https://www.youtube.com/watch?v=buMTH6ICnqk&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=5)

        Key terms you should know from the video:

        1. condition

        1. `if`

        1. `else`

        1. block

        1. indentation

        1. clause

        1. truthy

        1. falsey

        What are the truthy/falsey values for `int`, `str`, and `float`?

    1. [Lesson 6](https://www.youtube.com/watch?v=885qKiiKisI&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=6)

        Key terms you should know from the video:

        1. `while` (what's the difference between `while` and `if`?)

        1. iteration

        1. input validation

        1. infinite loops

        1. CTRL-C

        1. `break`

        1. `continue`

    1. [Lesson 7](https://www.youtube.com/watch?v=885qKiiKisI&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=7)

        Key terms you should know from the video:

        1. `for`

        1. `range` (what's the difference between passing 1, 2, and 3 arguments?)


    1. [Lesson 8](https://www.youtube.com/watch?v=885qKiiKisI&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=8)
        
        Key terms you should know from the video:

        1. function

        1. `import random` vs `from random import *`

        1. `random.randint`

        1. `sys.exit`

        1. third-party modules

        1. `ImportError`

    1. [Lesson 9](https://www.youtube.com/watch?v=885qKiiKisI&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=9)
        
        Key terms you should know from the video:

        1. `def`

        1. de-duplicating code

        1. `return`

        1. `None`

        1. keyword arguments

        1. `print`'s `end` and `sep` keyword arguments

    1. (okay to skip) [Lesson 10](https://www.youtube.com/watch?v=M-CoVBK_bLE&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=10)

       <!--
       Key terms:

       1. local scope

       1. global scope

       1. local variable

       1. global variable

       How can you tell if a variable is local or global?
       -->

    1. (okay to skip) [Lesson 11](https://www.youtube.com/watch?v=qS0UkqaYmfU&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=11)

        <!--
        Key terms:

        1. `try`

        1. `except`

        1. input validation
        -->

     1. (okay to skip) [Lesson 12](https://www.youtube.com/watch?v=48WXHT0dfEY&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=12)

     1. [Lesson 13](https://www.youtube.com/watch?v=48WXHT0dfEY&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=13)

        Key terms:

        1. list

        1. item

        1. comma deliminated

        1. `[]`

        1. index

        1. negative indexes

        1. slice

        1. slice shortcuts

        1. `del`

        1. `list()`

        1. `in`

        1. `not in`

        <!-- len is polymorphic -->

    1. [Lesson 14](https://www.youtube.com/watch?v=umTnflPbYww&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=14)

       Key terms:

       1. list-like / sequences

       1. range object

       1. multiple assignment

       1. swapping variables

       1. augmented assignment operators

    1. [Lesson 15](https://www.youtube.com/watch?v=Z9IxxW7428A&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=15)

       Key terms:

       1. method vs function

       1. `.index`

       1. `.append` <-- important

       1. `.insert`

       1. `.remove`

       1. `.sort` <-- important

       1. ASCII-betical order

    1. [Dictionaries](https://www.youtube.com/watch?v=daefaLgNkw0)        

        Key Terms:

        1. dictionary, map, key-value pair

        1. key

        1. value

        1. `{}`

        1. `[]`

        1. `.get`

        1. `.update`

        1. `del`

        1. `.keys`

        1. `.values`

        1. `.items`

## Lecture Notes

1. About Python:

    1. HTML/CSS are **markup** languages;
        you specify WHAT you want done, and firefox figures out HOW.

       Python is a **procedural** language;
        you directly specify HOW to do something.

    1. Most people find python MUCH harder than HTML/CSS.
        If you don't have prior programming experience,
        expect the next 2 weeks to be very difficult.
        Make good use of the student tutors and office hours.

1. Important resources:

    1. You can use <https://pythontutor.com> to visualize what python is doing "step-by-step".

    1. I will distribute the [Python cheat sheet](https://perso.limsi.fr/pointal/python:memento) in class.
       I recommend having this paper with you at all of our lectures and whenever you are coding in python.

<!--
[Monte Python and the Holy Grail (Top 5 best scenes)](https://www.youtube.com/watch?v=886hNDgwfMk)

[The Story of Python, by Its Creator Guido van Rossum](https://www.youtube.com/watch?v=J0Aq44Pze-w)

[5 things I wish I knew before becoming a software engineer](https://www.youtube.com/watch?v=M_GVUj86VaY)

    1. (Optional) [Edward Snowden: How Your Cell Phone Spies on You](https://www.youtube.com/watch?v=VFns39RXPrU)

    [5 most dangerous hackers of all time](https://www.youtube.com/watch?v=7UaPL5PGywo)
    -->

<!--
## Memes

After this week, you should understand all the jokes in the following memes.

<img src=float2.jpg width=img/400px>

<hr>

<img src=float.jpg width=img/400px>

<hr>

<img src=if.jpg width=img/400px>

<hr>

<img src=not_equals.jpg width=img/400px>
-->

## Lab

TBA
<!--
Instructions for your lab are contained in the `lab.py` file.

The file `lab.py` contains several incomplete functions that you must write.
Each function has several test cases provided in the docstring,
and currently all of these test cases are failing.
Your job is to make them pass.

To submit your lab,
run the command
```
$ python3 -m doctest --verbose lab.py
```
and copy/paste the output into sakai.

> **NOTE:**
> Modifying the test cases in any way will result in a -2 on the assignment.
> (That is, you'll actually lose points for submitting it.)
> This is not an academic integrity punishment,
> because it's easy to accidentally modify these test cases.
> Instead, the purpose of this penalty is to help you internalize the importance of good test cases.
> Test cases are the only evidence we have that our program works correctly,
> and if we destroy that evidence on accident,
> then our program will do very bad things.
> Billions of dollars have been lost, and people have died due to accidentally deleted test cases.
> 
> **tl;dr**
> Don't be Scumbag Steve.
> 
> <img src=img/comment_tests.jpg width=400px>
-->
