# Week 05: Unicode + files

<img width=400px src=vomiting_emoji.png />

You can find an explanation of this comic at https://www.explainxkcd.com/wiki/index.php/1813:_Vomiting_Emoji

**Monday:** Unicode

1. Unicode is the international standard for representing text as numbers.

1. Python is famous for it's good, native Unicode support.
    Other languages like C/C++/Java it's technically possible to use Unicode correctly, but it's much more difficult.

    1. Historical note:
        Python 3 broke off from Python 2 due to fundamental differences in vision about how Unicode should be supported.
        You can read more about [these differences from a famous pythonista here](https://lucumr.pocoo.org/2014/1/5/unicode-in-2-and-3/).

1. This information is not in the textbook,
    and we will use the references linked below.

   Actually, Unicode is something that's commonly not taught to computer science majors in the United States,
    since we believe that everyone should learn to speak a proper language like English.

   But companies actually have to work in the real world, with real people from outside the US,
    and often complain that colleges don't teach real-world skills like Unicode to CS majors.

*References:*

1. Python tutorial: https://realpython.com/python-encodings-guide/ (**this is our main "textbook" and you are responsible for all the material in this link**)

1. growth of UTF-8: https://en.wikipedia.org/wiki/UTF-8#/media/File:Utf8webgrowth.svg

1. The story of the gun emoji

    1. https://blog.emojipedia.org/apple-and-the-gun-emoji/
    1. https://www.businessinsider.com/apple-change-pistol-emoji-toy-confusion-precedent-meaning-retroactive-2016-8

1. NSA's security risks of Unicode: https://apps.nsa.gov/iaarchive/library/reports/unicode-security-risks.cfm

1. Unicode in the DPRK

    1. The DPRK uses the [KPS9566](https://en.wikipedia.org/wiki/KPS_9566) character set in most of its internal documents, including the [Red Star OS](https://en.wikipedia.org/wiki/Red_Star_OS)

        1. There are many other alternative encodings for Korean characters developed by ROK, China and the US

    1. 13 currently used emojis were first proposed by the DPRK; these include:

        | Code Point | Glyph    | Name          |
        | ---------- | -------- | ------------- |
        | U+2615     | ☕       | HOT BEVERAGE  |
        | U+2690     | ⚐        | WHITE FLAG    |
        | U+2691     | ⚑        | BLACK FLAG    |

    1. Several minor international incidents have been caused by misunderstandings between the DPRK and the Unicode Consortium

        1. The DPRK complained that the Unicode Consortium unfairly adopted the South Korean alphabetical order without consulting the DPRK: https://unicode.org/wg2/docs/n2231.pdf

        1. The Unicode Consortium did not accept symbols specific to the Worker's Party of Korea: https://unicode.org/wg2/docs/n2392.pdf

        1. Master's thesis exploring the topic: https://www.era.lib.ed.ac.uk/bitstream/handle/1842/12253/Hwang2005.pdf

**Wednesday:**
We will cover [Chapter 9 - Reading and Writing Files](https://automatetheboringstuff.com/2e/chapter9/) of the book,
but we will also talk about the interaction between files and Unicode.

Prelecture videos:

1. Corey Schafer's [Reading and Writing to Files](https://www.youtube.com/watch?v=Uh2ebFW8OYM)

1. Corey Schafer's [Error Handling Try/Except](https://www.youtube.com/watch?v=NIWwJbo-9_8)

## Lab

TBA

<!--

gziped files of different encodings

-->
