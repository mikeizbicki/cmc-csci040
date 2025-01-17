# Homework 1: Markdown to HTML Compiler

![wtf_comic](wtf.jpg)

**Description:** 
HTML is almost never written by hand these days.
Instead, we write programs that write the HTML for us.
In this homework, you will write a Python program that generates HTML from a Markdown document.

Markdown is a simpler language than HTML and is widely used.
Social media websites like [reddit](https://www.reddit.com/wiki/markdown) use markdown;
if you take the CS36: Fundamentals of Data Science, then all your homeworks will be completed in [R-Markdown](https://rmarkdown.rstudio.com/);
and for my own personal blog at [izbicki.me](https://izbicki.me),
I use Markdown to write all my posts.
GitHub uses [GitHub flavored markdown](https://guides.github.com/features/mastering-markdown/) for all `README.md` files and for all issues.

**Financial Aside:**
Let's consider Github's implementation of the Markdown-HTML compiler:
1. How much did it cost GitHub?
    1. I would assign an entry-level engineer to implement this task and expect it to take about 1 week.
    1. Entry-level engineers at Github [make $148k/year](https://www.levels.fyi/company/GitHub/salaries/Software-Engineer/), 
       so about $3000/week.
    1. Therefore, GitHub paid someone $3000 to implement what you're doing for homework.
1. Was this a good investment by GitHub?
    1. GitHub has [>60 million active users](https://github.com/search?q=type:user&type=Users)
    1. So GitHub spent 0.005 cents per user on this feature (one time fee!)
    1. GitHub makes on average about $4/user/month
        1. (mostly by selling compute time, something that we don't use in this class)
    1. This discrepancy between how much users pay and how much it costs "per user" to pay an engineer is why software engineers make so much money
    1. This is a simplified analysis.
        1. The field of "software engineering" studies actually making these project timeline estimates and accounting details.

**Due:** 
~~Sunday, 02 October, midnight~~
Sunday, 09 October, midnight

> **NOTE:**
> We will still have more labs/quizzes/etc next week,
> so I strongly recommend trying to complete it by this coming Sunday.

**Learning objectives:**

1. understand the markdown language
1. understand string manipulation in python
1. understand how compilers convert from one programming language into another

## Instructions

Complete the `markdown_compiler.py` file so that all doctests pass.
Recall that you can run the doctests with the command
```
$ python3 -m doctest --verbose markdown_compiler.py
```

Also run the commands
```
$ python3 markdown_compiler.py --input_file=README.md
$ python3 markdown_compiler.py --input_file=README.md --add_css
```
each of these commands will generate a new file called `README.html`.
Open this file in firefox and take a screenshot.
Notice that adding the `--add_css` flag to the command line adds css code to the webpage that modifies how the page gets rendered.
This is one advantage of using markdown over straight HTML for webpage generation:
we can easily generate many different looking webpages from the same markdown content.

> **HINT:**
> Do not wait to run your the `--input_file` commands until you've completed all of the doctests.
> You should run these commands continuously as you complete each function and verify that the output works.

## Submission

Upload to sakai
1. the output of running the doctests with the `--verbose` flag,
1. your 2 screenshots,
1. a short 1 sentence statement of your collaboration if you want the 48 hour extension, and
1. a short 1 sentence statement of what your grade should be according to the rubric below.

## Grading Rubric

This assignment is worth a total of 18 points.

There are 11 functions that have failing doctests.
Each function is worth 1.5 points for a total of 16.5 points.
You must have all doctests passing in order to get the points for the function.

The remaining 1.5 points are for your screenshots.
These points test that you understand how to run your python program from the command line with different parameters and view the results in firefox.

### Extra Credit

There are two options for extra credit on this assignment,
each worth 1.5 points.
So you may earn up to 21/18 on this assignment if you complete both extra credits.

**Option 1:**
Escape Characters

Currently, there is no way to "escape" the markdown commands.
For example, the markdown text
```
\*not italic\*
```
will get converted into
```
\<i>not italic\</i>
```

To get this extra credit, you will have to:
1. Add 3 doctests to the `compile_italic_star` function that contain escaped markdown commands (i.e. the backslash star '\*').
1. Modify your code so that these doctests pass.

**Option 2:**
(hard)
Lists

Currently, there is no support for converting markdown lists into html lists.
For example, the markdown text
```
1. this
2. is
3. a
4. list
```
will get converted into
```
1. this 2. is 3. a 4. list
```
instead of
```
<ol><li>this</li><li>is</li><li>a</li><li>list</li></ol>
```

To get this extra credit, you will have to:
1. Add 3 doctests to the `compile_lines` function that contain markdown lists.
   These should be "good" doctests that reasonably test that the list functionality works; feel free to chat 1-1 with me about this.
1. Modify your code so that these doctests pass.
