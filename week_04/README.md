# Week 04: Python strings, regular expressions, and files

<center>
<img width='80%' src=Strips-Le-dernier-des-vrais-codeurs-650-finalenglsih.jpg />
</center>

**Quiz:**
The completed `quiz.pdf` should be submitted to sakai by Friday at midnight.

**Monday:** We will cover [Chapter 6 - Strings](https://automatetheboringstuff.com/2e/chapter6/) and [Chapter 7 - Regular Expressions](https://automatetheboringstuff.com/2e/chapter7/) of the book.

Prelecture videos:

1. Corey Schafer's [Strings - Working with Textual Data](https://www.youtube.com/watch?v=k9TUPpGqYTo)

1. Corey Schafer's [F-Strings](https://www.youtube.com/watch?v=nghuHvKLhJA)

1. Corey Schafer's [String Formatting](https://www.youtube.com/watch?v=vTX3IwquFkc)

Regular expressions are an advanced topic that we're not going to cover in detail,
and you will never be required to write a regular expression in this class.
If you've done programming before, however,
I strongly recommend you try to learn regular expressions in detail,
as they can greatly simplify your code.
The following video provides a good tutorial.

1. Corey Schafer's [Regular Expressions Tutorial](https://www.youtube.com/watch?v=K8L6KVGG-7o)

**Wednesday:** We will cover [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/2e/chapter9/) of the book.

Prelecture videos:

1. Corey Schafer's [Reading and Writing to Files](https://www.youtube.com/watch?v=Uh2ebFW8OYM)

1. Corey Schafer's [Error Handling Try/Except](https://www.youtube.com/watch?v=NIWwJbo-9_8)

1. Johnny Metz's [Argparse Tutorial](https://www.youtube.com/watch?v=cdblJqEUDNo)

**Thursday:** Lab.

There is no prelab work.

## Lab

There are two parts for this lab.

### Part I: Markdown

*This part of the lab requires posting to github using markdown formatting.  The instructions will be posted on Thursday.*

### Part II: `youtube-dl`

One of the benefits of python is that it is easy to download and run programs (called scripts) that other people have written.
One such script is called `youtube-dl`,
which lets you easily download videos from youtube and other video sites onto your computer.
(The `-dl` stands for "download").

`pip3` is the program that installs these python scripts onto your computer.
To install `youtube-dl`, run the command
```
$ pip3 install youtube-dl
```
If this command doesn't work for you, then see [Appendix A](https://automatetheboringstuff.com/2e/appendixa/) of *Automate the Boring Stuff* for instructions on configuring `pip3` for your system.

Once you've successfully installed `youtube-dl`,
you can run the script with the command
```
$ python3 -m youtube_dl
```
Notice that the command above uses an underscore `_` instead of a dash `-`.
If everything is working correctly, you should get output that looks like
```
Usage: __main__.py [OPTIONS] URL [URL...]

__main__.py: error: You must provide at least one URL.
Type youtube-dl --help to see a list of all options.
```
In order to download a youtube file, simply paste the URL at the end of the command.
The URL https://www.youtube.com/watch?v=dQw4w9WgXcQ links to the WarGames movie (which is one of the movies to watch to get an A in the class),
and so if you run the command
```
$ python3 -m youtube_dl https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
then the script will download WarGames onto your computer.
If those links don't get WarGames vidoe for you, then [click here](#rickrolled) for debugging.

Scripts generally provide detailed help that tells you how to use the command if you pass the `--help` flag.
If you run
```
$ python3 -m youtube_dl --help
```
you can see that `youtube_dl` has many options for things like setting the audio/video quality of the download, downloading entire playlists, and using web proxies for the download.

###### Rickrolled

You've been [rickrolled](https://en.wikipedia.org/wiki/Rickrolling).
The actual WarGames movie is legally available on YouTube at this link: https://www.youtube.com/watch?v=HNLQ-O-Qx3Y .
If you visit this link with firefox and uBlock Origin enabled,
then you can watch the movie for free without ads.
If you download it with `youtube-dl`, then you can watch it locally on your own computer without ads.

<!--
1. Corey Schafer's [`if __name__ == '__main__'`](https://www.youtube.com/watch?v=sugvnHA7ElY)

## Lab

Complete the `lab.py` file and submit your doctests to sakai.
-->

### Lab Submission

Upload your rickroll video to sakai.
