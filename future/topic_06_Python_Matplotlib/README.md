# Week 06: More Files + CSV/JSON + Matplotlib

<img width=400px src=programming.jpg>

**Announcements:**

1. Download:

    1. The zip files at <https://github.com/bpb27/trump_tweet_data_archive>.
       You'll eventually need them all for lab,
       but any one of the files will be fine for lecture.

    1. The `notes_json.py` file.

1. No lab session/office hours this Friday.

   But you still have a lab for this week... it will be due Tuesday (or Thursday with the collaboration extension).

1. This week's quiz will be a review quiz.

   Expect harder questions than previous quizzes.
   (For example, more questions from the end of the practice packets.)
   The questions will also focus on concepts that I see students struggling with.

1. Next project posted.

**More about files and paths:**
<!--
We will cover [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/2e/chapter9/) of the book,
but we will also talk about the interaction between files and Unicode.

Prelecture videos:

1. Corey Schafer's [Reading and Writing to Files](https://www.youtube.com/watch?v=Uh2ebFW8OYM)

1. Corey Schafer's [Error Handling Try/Except](https://www.youtube.com/watch?v=NIWwJbo-9_8)

Minimal required knowledge (in addition to the cheatsheet):
-->

More information about files:

1. paths are how we specify the location of files

    1. there are two types of paths: relative and absolute

       if you need to use a path, then you may always use either type of path depending on which is more convenient

    1. absolute paths specify the exact location of a file

       on windows machines:
       1. absolute paths start with a drive letter, e.g. `c:/`, `d:/`, `e:/`
       1. example: `C:/Program Files/Zoom/video.mp4`
       1. older windows machines use backslash `\` to separate directories, newer windows machines use forwardslash `/`

       on non-windows machines:
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
          
          1. Example:

              if the working directory is `/Users/Mike/Zoom`,

              and the relative path is `video.mp4`,

              then the absolute path is `/Users/Mike/Zoom/video.mp4`

       1. in python, we get the working directory with the commands
          ```
          >>> import os
          >>> os.getcwd()       # cwd = current working directory
          ```
          this is the same for both windows and non-windows computers

      1.  in the terminal, we get the working directory with the command
          ```
          $ pwd                 # pwd = print working directory (non-Windows)
          $ cd                  # cd = current directory (windows)
          ```

          you can also change the working directory with the terminal command
          ```
          $ cd PATH             # cd = change directory; PATH = new working directory
          ```

          you can list the files in the working directory with the terminal command
          ```
          $ ls                  # (non-windows)
          $ dir                 # (windows)
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

<!--
<img width=600px src=states-of-a-programmer.png>
-->

**Data Analysis:**

We will cover [Chapter 16 - Working with CSV Files and JSON Data](http://automatetheboringstuff.com/2e/chapter16/) of the book.

<img src=json.jpg width=600px>

Reference videos:

1. Corey Schafer's [Working with JSON Data using the json Module](https://www.youtube.com/watch?v=9N6a-VLBa2I)

We will cover the matplotlib library.
The textbook does not have a chapter on using the matplotlib library,
but the library itself has a great set of tutorials that you can use as a reference:
<https://matplotlib.org/3.3.1/tutorials/index.html>

Reference videos:

1. Corey Schafer has a [full set of tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_) that covers everything about matplotlib.
   You don't need to watch all of these videos,
   but I recommend watching at least the first one.

The main takeaway from this week is that lots of programming is just:

1. Using other people's libraries

   <img width=800px src=programming-libraries-comic.png />


1. And googling how to use their libraries

   <img width=600px src=google.png />

## Lab

There are multiple parts to the lab assignments this week.
Each is worth 3 points and has its own submission on sakai.

Because of Fall Break, the due date for all parts is NOT Sunday, but Tuesday at midnight.
If you collaborate, you can have an extension until Thursday.

### Part 1

In this lab, you will extend the tweets analysis you did in week 03's lab to work with ALL of Trump's tweets. 
Follow the instructions in the `lab_part1.py` file.

You may also be interested in reading [this analysis of Trump's tweets](http://varianceexplained.org/r/trump-tweets/) which exploits metainformation in the tweet JSON object to determine which tweets were sent by Trump and which by his staff.

### Part 2

Complete the doctests in `lab_part2.py` like normal.
