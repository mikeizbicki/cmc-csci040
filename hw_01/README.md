# Homework 1: Markdown to HTML Compiler

![wtf_comic](wtf.jpg)

**Description:** 
HTML is almost never written by hand these days.
Instead, we write programs that write the HTML for us.
In this homework, you will write a Python program that generates HTML from a Markdown document.

Markdown is a simpler language than HTML and is widely used.
Social media websites like [reddit](https://www.reddit.com/wiki/markdown) use markdown;
if you take the CS36: Fundamentals of Data Science, then all your homeworks will be completed in [R-Markdown](https://rmarkdown.rstudio.com/);
and for my own personal blog at [izbicki.me](https://izbicki.me), I use Markdown to write all my posts.
GitHub uses [GitHub flavored markdown](https://guides.github.com/features/mastering-markdown/) for all `README.md` files and for all issues.

**Due:** 
~~Sunday, 26 September, midnight~~
Wednesday, 30 September, midnight

**Learning objectives:**

1. understand string manipulation in python
1. understand how compilers convert from one programming language into another
1. understand the markdown language

## Instructions

Complete the `markdown_compiler.py` file so that all doctests pass.

Run the command:
```
$ python3 -m doctest --verbose mardown_compiler.py
```
and upload the output into sakai.

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
Once you've generated your screenshots, upload both of them to sakai.

## Grading Rubric

There are 9 functions for you to implement with doctests.
Each function is worth 1.5 points.

The remaining 1.5 points are for your two screenshots.
This tests that you understand how to run the program from the command line with different parameters and view the results in firefox.

### Extra Credit: Multi-line markdown features

All of the markdown features that you implemented require inspecting only a single line at a time.
Some features of Markdown, however, require looking at multiple lines in order to convert them into HTML.
Examples include code blocks like:
```
for i in range(10):
    print('i=',i)
```
and ordered lists like:
1. item 1
1. item 2
1. item 3

You can earn up to 2 points of extra credit for implementing these features.
(You get 1 point per feature.)

Here's some hints on how to do this.
Recall that the HTML for code blocks uses the `<pre>` tag 
and the HTML for lists uses the `<ol>` 
and `<li>` tags,
so that's what you will have to insert into the HTML document.
In order to get some ideas on how to implement this feature,
you can look at how the  `compile_lines` function 
inside of `markdown_compiler.py` 
adds `<p>` tags.

**If you complete the extra credit, please clearly say so in your sakai submission so that I know to grade it.**
