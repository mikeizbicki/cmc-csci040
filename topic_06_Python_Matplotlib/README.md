# Week 06: Files (for real this time!) + JSON + Matplotlib

<img width=600px src=programming.jpg>

**Monday:**
We will cover [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/2e/chapter9/) of the book,
but we will also talk about the interaction between files and Unicode.

Prelecture videos:

1. Corey Schafer's [Reading and Writing to Files](https://www.youtube.com/watch?v=Uh2ebFW8OYM)

1. Corey Schafer's [Error Handling Try/Except](https://www.youtube.com/watch?v=NIWwJbo-9_8)

Minimal required knowledge (in addition to the cheatsheet):

1. paths are how we specify the location of files

    1. there are two types of paths: relative and absolute

       if you need to use a path, then you may always use either type of path depending on which is more convenient

    1. absolute paths specify the exact location of a file

       on windows machines:
       1. absolute paths start with a drive letter, e.g. `c:/`, `d:/`, `e:/`
       1. example: `C:/Program Files/Zoom/video.mp4`
       1. older windows machines use backslash `\` to separate directories, newer windows machines use forwardslash `/`

       on everything else:
       1. absolute paths start with `/`
       1. example: `/Users/Mike/Zoom/video.mp4`
       1. always use a forwardslash to separate directories

    1. a relative path is any path that does not match the rules above

       1. they are the same on all computers (with the exception that some windows machines use `\` instead of `/`)
       1. example:
          1. `video.mp4`
          1. `Zoom/video.mp4`
          1. `Mike/../Mike/Zoom/video.mp4`

       1. relative paths are always converted to absolute paths by prepending the "working directory"
          
          if the working directory is `/Users/Mike/Zoom`, and the relative path is `video.mp4`, then the absolute path is `/Users/Mike/Zoom/video.mp4`

       1. in python, we get the working directory with the commands
          ```
          >>> import os
          >>> os.getcwd()       # cwd = current working directory
          ```

          in the terminal, we get the working directory with the command
          ```
          $ pwd                 # pwd = print working directory
          ```

          you can also change the working directory with the terminal command
          ```
          $ cd PATH             # cd = change directory; PATH = new working directory
          ```

          you can list the files in the working directory with the terminal command
          ```
          $ ls
          ```

1. `..` is a special directory that means "go up one level"

   for example:
   ```
   $ pwd
   /Users/Mike
   $ cd ..
   $ pwd
   /Users
   $ cd Mike
   $ pwd
   /Users/Mike
   ```

<img width=600px src=states-of-a-programmer.png>

**Wednesday:**
We will cover [Chapter 16 - Working with CSV Files and JSON Data](http://automatetheboringstuff.com/2e/chapter16/) of the book.

<img src=json.jpg width=600px>

Prelecture videos:

1. Corey Schafer's [Working with JSON Data using the json Module](https://www.youtube.com/watch?v=9N6a-VLBa2I)

We will cover the matplotlib library.
The textbook does not have a chapter on using the matplotlib library,
but the library itself has a great set of tutorials that you can use as a reference:
https://matplotlib.org/3.3.1/tutorials/index.html

<img width=800px src=programming-libraries-comic.png />

Prelecture videos:

1. Corey Schafer has a [full set of tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_) that covers everything about matplotlib.
   You don't need to watch all of these videos,
   but I recommend watching at least the first one.

<img width=600px src=google.png />

## Lab

There are two lab assignments this week,
each with their own submission on sakai.
The first is mandatory, but has an extra credit option so you may earn 6/5 on the lab.
The second is optional and worth 2 points of extra credit.

Because of Fall Break, the lab date for both labs is NOT Sunday, but Tuesday at midnight.
If you collaborate, you can have an extension until Thursday.

### Lab 1

In this lab, you will extend the tweets analysis you did in week 03's lab to work with ALL of Trump's tweets. 
Follow the instructions in the `lab_part1.py` file.

You may also be interested in reading [this analysis of Trump's tweets](http://varianceexplained.org/r/trump-tweets/) which exploits metainformation in the tweet JSON object to determine which tweets were sent by Trump and which by his staff.

### Lab 2

This lab is worth 2 points of extra credit.
To earn the extra credit, complete the doctests in `lab_part2.py` just like normal.
You must pass all of the doctests to earn the extra credit,
and no partial credit will be awarded.
