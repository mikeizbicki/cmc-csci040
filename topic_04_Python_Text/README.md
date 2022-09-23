# Week 04: Text data

<img src=4rules.jpg width=400px>

**Monday:**
We will cover [Chapter 6 - Strings](https://automatetheboringstuff.com/2e/chapter6/).

<!--
NOTE:
    Need raw strings for homework doctests!
    Need \n \t \r
-->

Recommended videos:

1. We've watched all of the textbook's premade videos now,
   but there's LOTs of other free resources for learning programming.
   Corey Schafer is one of the more famous youtube channels for learning python,
   and he has some great tutorials for learning about strings:

1. Corey Schafer's [Strings - Working with Textual Data](https://www.youtube.com/watch?v=k9TUPpGqYTo)

1. Corey Schafer's [F-Strings](https://www.youtube.com/watch?v=nghuHvKLhJA)

<!--
1. Corey Schafer's [String Formatting](https://www.youtube.com/watch?v=vTX3IwquFkc)
-->

**Wednesday:**
The ASCII encoding scheme, and how text is stored as numbers.

Non-decimal number systems

1. https://www.youtube.com/watch?v=ZL-LhaaMTTE (**watch this before class on wednesday**)

## Lab

TBA
<!--
There are two parts for this lab.

### Part I: Markdown

Visit [Issue #104](https://github.com/mikeizbicki/cmc-csci040/issues/104) and follow the instructions there.

### Part II: `youtube-dl`

One of the benefits of python is that it is easy to download and run programs (called scripts) that other people have written.
Your homework file has you writing one of these scripts,
and this lab will give you practice using a famous script called `youtube-dl`,
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
Depending on your computer's configuration, you may get some error messages with the above command.
If you get an error about the url not being found, you need to put the url in single quotation marks (`'`).
If you get an error about a failed SSL certificate, then add the `--no-check-certificate` option to the command above.

After you download the video, play it on your local computer.
Notice that it's not actually the WarGames movie.
[Click here](#rickrolled) for an explanation.

Scripts generally provide detailed help that tells you how to use the command if you pass the `--help` flag.
If you run
```
$ python3 -m youtube_dl --help
```
you can see that `youtube_dl` has many options for things like setting the audio/video quality of the download, downloading entire playlists, and using web proxies for the download.

### Lab Submission

Upload your downloaded rickroll video to sakai.

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>

###### Rickrolled

You've been [rickrolled](https://en.wikipedia.org/wiki/Rickrolling).
The actual WarGames movie is legally available on YouTube at this link: https://www.youtube.com/watch?v=HNLQ-O-Qx3Y .
If you visit this link with firefox and uBlock Origin enabled,
then you can watch the movie for free without ads.
If you download it with `youtube-dl`, then you can watch it locally on your own computer without ads.
-->
