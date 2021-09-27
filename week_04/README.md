# Week 04: Text data

![This commic is a joke about error message in python.](4rules.jpg)

**Monday:**
We will cover [Chapter 6 - Strings](https://automatetheboringstuff.com/2e/chapter6/).

<!--
NOTE:
    Need raw strings for homework doctests!
    Need \n \t \r
-->

Recommended (intermediate-level) videos:

1. The techniques in these videos are not required to complete you assignments,
    but if you use them,
    the assignments will be easier.

1. Corey Schafer's [Strings - Working with Textual Data](https://www.youtube.com/watch?v=k9TUPpGqYTo)

1. Corey Schafer's [F-Strings](https://www.youtube.com/watch?v=nghuHvKLhJA)

1. Corey Schafer's [String Formatting](https://www.youtube.com/watch?v=vTX3IwquFkc)

**Wednesday:**
We will begin covering Unicode, which is the international standard for storing non-English text.
Likely, we will continue talking about Unicode next week.

1. Python is famous for it's good, native Unicode support.
    Other languages like C/C++/Java it's technically possible to use Unicode correctly, but it's much more difficult.

    1. Historical note:
        Python 3 broke off from Python 2 due to fundamental differences in vision about how Unicode should be supported.
        You can read more about [these differences from a famous pythonista here](https://lucumr.pocoo.org/2014/1/5/unicode-in-2-and-3/).

1. This information is not in the textbook,
    and we will use the references linked below.

1. Actually, Unicode is something that's commonly not taught to computer science majors in the United States,
    since we believe that everyone should learn to speak a proper language like English.

1. But companies actually have to work in the real world, with real people from outside the US,
    and often complain that colleges don't teach real-world skills like Unicode to CS majors.

**References:**

Non-decimal number systems

1. https://www.youtube.com/watch?v=ZL-LhaaMTTE

Unicode support in python

1. The story of the gun emoji

    1. https://blog.emojipedia.org/apple-and-the-gun-emoji/
    1. https://www.businessinsider.com/apple-change-pistol-emoji-toy-confusion-precedent-meaning-retroactive-2016-8

1. Python tutorial: https://realpython.com/python-encodings-guide/

1. growth of UTF-8: https://en.wikipedia.org/wiki/UTF-8#/media/File:Utf8webgrowth.svg

NSA's security risks of Unicode: https://apps.nsa.gov/iaarchive/library/reports/unicode-security-risks.cfm

**Comics/Memes**

<img width=400px src=vomiting_emoji.png />

You can find an explanation of this comic at https://www.explainxkcd.com/wiki/index.php/1813:_Vomiting_Emoji


## Lab

There are two parts for this lab.

### Part I: Markdown

Visit [Issue #104](https://github.com/mikeizbicki/cmc-csci040/issues/104) and follow the instructions there.

### Part II: TBA


<!--
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

1. Corey Schafer's [`if __name__ == '__main__'`](https://www.youtube.com/watch?v=sugvnHA7ElY)

## Lab

Complete the `lab.py` file and submit your doctests to sakai.

### Lab Submission

Upload your rickroll video to sakai.

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
