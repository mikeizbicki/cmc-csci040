# Week 06: Files (for real this time!) + JSON + Matplotlib

<img width=600px src=programming.jpg>

**Monday:**
We will cover [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/2e/chapter9/) of the book,
but we will also talk about the interaction between files and Unicode.

Prelecture videos:

1. Corey Schafer's [Reading and Writing to Files](https://www.youtube.com/watch?v=Uh2ebFW8OYM)

1. Corey Schafer's [Error Handling Try/Except](https://www.youtube.com/watch?v=NIWwJbo-9_8)

Minimal required knowledge:

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

Prelecture videos:

1. Corey Schafer's [Working with JSON Data using the json Module](https://www.youtube.com/watch?v=9N6a-VLBa2I)

We will cover the matplotlib library.
The textbook does not have a chapter on using the matplotlib library,
but the library itself has a great set of tutorials that you can use as a reference:
https://matplotlib.org/3.3.1/tutorials/index.html

<img width=600px src=programming-libraries-comic.png />

Prelecture videos:

1. Corey Schafer has a [full set of tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_) that covers everything about matplotlib.
   You don't need to watch all of these videos,
   but I recommend watching at least the first one.

<img width=600px src=google.png />

## Lab

TBA
