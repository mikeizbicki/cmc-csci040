# Topic 02: Python

<center>
<img width='100%' src=img/python.png />
</center>

## Prelecture Tasks

1. Download and install the latest version of python for your system from <https://python.org/downloads/>.

1. (optional) Prelecture videos:

    We will cover all of the material in these videos in class,
    but if you haven't done any programming before this class,
    you will probably find our in-class discussions to very fast and confusing.
    Watching these videos first will help.

    1. [Lesson 1](https://www.youtube.com/watch?v=1F_OgqRuSdI&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW)

        In this class, you are allowed to use either the IDLE editor or VSCode.
        I will use VSCode in lectures because most students find VSCode to be easier to work with than IDLE,
        but Al Sweigart uses IDLE in his videos.

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

## Lecture Notes

1. We will cover chapters 0-3 of Al Sweigart's [Automate the Borting Stuff](https://automatetheboringstuff.com/).

    1. HTML/CSS are **markup** languages;
        you specify WHAT you want done, and firefox figures out HOW.

       Python is a **procedural** language;
        you directly specify HOW to do something.

    1. Python is much more powerful.

    1. Most people find python MUCH harder than HTML/CSS.
        If you don't have prior programming experience,
        expect the next 2 weeks to be very difficult.
        Make good use of the student tutors and office hours.

1. Important resources:

    1. You can use https://pythontutor.com to visualize what python is doing "step-by-step".

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

Instructions for your lab are contained in the `lab.py` file.

<!--
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
