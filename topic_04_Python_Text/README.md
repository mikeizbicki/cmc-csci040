# Topic 04: Text data

<img src=img/4rules.jpg width=300px>

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

1. You will need to understand non-decimal number systems (e.g. binary, octal, and hexadecimal).  You can watch this video for a review: <https://www.youtube.com/watch?v=ZL-LhaaMTTE>

## Lab

There are two parts for this lab.

### Part I: Markdown

Visit [Issue #257](https://github.com/mikeizbicki/cmc-csci040/issues/257) and follow the instructions there.

### Part II: `yt-dlp`

One of the benefits of python is that it is easy to download and run programs (called scripts) that other people have written.
In your next homework you will write one of these scripts.
The purpose of this lab is to give you practice using other people's scripts.

You will use a famous script called `yt-dlp`,
which lets you easily download videos from youtube and other video sites onto your computer.
(The `yt` stands for "youtube", the `dl` stands for "download", and the `p` stands for "plus" to indicate that the program works with more than just youtube.)

`pip3` is the program that installs these python scripts onto your computer.
To install `yt-dlp`, run the command
```
$ pip3 install yt-dlp
```
If this command doesn't work for you, then see [Appendix A](https://automatetheboringstuff.com/2e/appendixa/) of *Automate the Boring Stuff* for instructions on configuring `pip3` for your system.
(Or just ask me...)

Once you've successfully installed `yt-dlp`,
you can run the script with the command
```
$ python3 -m yt_dlp
```
Notice that the command above uses an underscore `_` instead of a dash `-`.
If everything is working correctly, you should get output that looks like
```
Usage: __main__.py [OPTIONS] URL [URL...]

__main__.py: error: You must provide at least one URL.
Type yt-dlp --help to see a list of all options.
```
In order to download a youtube file, simply paste the URL at the end of the command.
The URL <https://www.youtube.com/watch?v=dQw4w9WgXcQ> links to the WarGames movie (which is one of the movies to watch to get an A in the class),
and so if you run the command
```
$ python3 -m yt_dlp https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
then the script will download WarGames onto your computer.
Depending on your computer's configuration, you may get some error messages with the above command.
If you get an error about the url not being found, you need to put the url in single quotation marks (`'`).
If you get an error about a failed SSL certificate, then add the `--no-check-certificate` option to the command above.

After you download the video, play it on your local computer.
Notice that it's not actually the WarGames movie.
[Click here](#rickrolled) for an explanation.

> **Aside:**
> Is using `yt-dlp` legal?
> Yes.
>
> Why would a tool for pirating be legal?
> It has many legitimate uses besides pirating.
> For example:
> 1. The [Aleph with Beth youtube channel]() develops videos for teaching Hebrew.
>   They have [explicit instructions about how to use `yt-dlp` to download their videos in order to watch them in locations without internet access](https://freehebrew.online/offline/).
> 1. The KCNA watch website provides an archive of all material published by the DPRK (i.e. North Korea).
>   They use `yt-dlp` to archive videos,
>   and you can find the [archived repository here](https://kcnawatch.org/kctv-archive/).
>   Foreign policy analysts can rely on the fact that videos in this archive will not be modified/deleted due to changes in the political climate.
>
> Previously, the standard package for downloading content from youtube was called `youtube-dl`,
> but a legal battle with the RIAA caused the project to "fork" to the new `yt-dlp` project.
> The primary complaint that the RIAA had against `youtube-dl` was that they used several examples in their documentation that could be construed as encouraging piracy;
> the `yt-dlp` documentation does not contain these examples and so is not subject to the same litigation,
> although it can certainly still be used for piracy.
> In general in the US, developing or possessing software is never illegal,
> and you cannot be prosecuted for developing or possessing particular software.
> You will be prosecuted for any illegal activity that you use the software for.
> The distinction is subtle but important.
>
> You can find details on the history of `youtube-dl`/`yt-dlp` and the legalities at Hacker News: <https://news.ycombinator.com/item?id=24872911>.
> This is a famous social media website for news and discussions about programming.

Scripts generally provide detailed help that tells you how to use the command if you pass the `--help` flag.
If you run
```
$ python3 -m yt-dlp --help
```
you can see that `yt-dlp` has many options for things like setting the audio/video quality of the download, downloading entire playlists, and using web proxies for the download.

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
The actual WarGames movie is legally available on YouTube at this link: <https://www.youtube.com/watch?v=HNLQ-O-Qx3Y>.
If you visit this link with firefox and uBlock Origin enabled,
then you can watch the movie for free without ads.
The link is flagged as being copyrighted,
and so cannot be (easily) downloaded with `yt-dlp`.
