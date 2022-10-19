# Week 07: Syntactic Sugar

"Syntactic Sugar" is a short way of writing common idioms in code.
Python is famous for having lots of syntactic sugar.

<img src=syntactic_sugar_everywhere.jpeg width=400px />

We've already seen some examples of syntactic sugar:

<img src=while_for.png width=400px />

List comprehensions are a famous and controversial form of syntactic sugar.
They can simplify your code a lot, or make it difficult to read.
Whether to use them or not is a matter of individual judgement and taste.

<img src=pooh.jpg width=300px />
<!--
<br>
<br>
<br>

<img src=hip.webp width=300px />
-->

In general: `while` loops > `for` loops > list comprehensions

    * where `>` should be read as "more powerful than"
    
References:

    1. list comprehensions: https://realpython.com/list-comprehension-python/

    1. (optional) dictionary comprehensions: https://www.datacamp.com/community/tutorials/python-dictionary-comprehension

    1. (video) Corey Shafer's comprehension tutorial: https://www.youtube.com/watch?v=3dt4OGnU5sM

## Lab

TBA

<!--
**Overview:**

To celebrate Halloween, you will practice file and string operations by editing the book *Dracula*.

**Due date:**

Halloween, Oct 31

If you submit the lab by Sunday 24 October (or Tuesday 26 October if you collaborate), then you will get +1 point of extra credit.


**Instructions:**

1. The copyright on the book *Dracula* has expired, and the book is now in the public domain.
    Project Gutenberg (https://gutenberg.org) is a website that makes all public domain books easily downloadable.
    *Dracula* is located at http://www.gutenberg.org/files/345/345-h/345-h.htm .
    Visit this webpage and save it to your computer in a file called `dracula.html` (use: right click -> save as).

1. Create a python file called `dracula.py` file that:
    1. Reads in the text from `dracula.html`.
    2. Replaces all occurrences of the word "Dracula" with "Izbicki".

       All occurrence of the word Izbicki should be in bold so that they are easy to see.

       Recall that the HTML to make a string of text bold is `<strong></strong>`.
       Also note that the title of the book is "D R A C U L A" and this should also change to "I Z B I C K I",
       and that occurrences of "DRACULA" should be replaced by "IZBICKI" maintaining the same capitalization scheme.

    3. Replaces all occurrences of the word "count" with the word "professor".
        Thus, all occurrences of the phrase "Count Dracula" will be replaced by the phrase "Professor Izbicki".

        Note that the word "count" is sometimes capitalized and sometimes lowercase;
        you should be able to replace both of these words with the correct case;
        this will sometimes lead to ungrammatical sentences like "Professor me in",
        but that's okay.
        Also note that words like "country"  and "accounting" should NOT be changed 
        to "professorry" and "acprofessoring";
        you must only replace the word "count" and not words where "count" appears as a substring.

    4. Replaces all occurrences of the phrase "Bram Stoker" with your name.

    5. Saves the resulting story to a file called `izbicki.html`.

       Note that your final saved file should still have all the html code that makes it a valid webpage.

3. Upload both your `dracula.py` code and `izbicki.html` output file to Sakai.
-->
