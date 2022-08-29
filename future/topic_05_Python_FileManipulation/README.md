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

**Facebook in the news:**

1. Leaks
    1. Facebook Whistleblower Leaks Thousands of Pages of Incriminating Internal Docs: https://news.ycombinator.com/item?id=28761294
    1. Mark's response: https://news.ycombinator.com/item?id=28767700

    1. ASIDE:
        1. the website https://news.ycombinator.com is called "Hacker News", but it's not *really* about hacking

        1. the website https://phrack.org is a *real* hacker website

1. Outage
    1. All Facebook properties were down for about 6-14 hours on Tuesday
    1. Estimated lost revenue is $90 million https://www.managementstudyguide.com/economic-impact-of-facebook-outage.htm
    1. Stock price fell 2% => Mark lost $7 billion dollars in value

How does an outage like this happen?

1. Map of Facebook datacenters: https://baxtel.com/data-centers/facebook

1. Submarine cables:

    1. map: https://www.submarinecablemap.com/

    1. cables can get physically disconnected:

        1. images: https://www.google.com/search?q=submarine+cable+laying&tbm=isch

        1. sharks: https://slate.com/technology/2014/08/shark-attacks-threaten-google-s-undersea-internet-cables-video.html

    1. Aside: NSA wire tapping of cables:

        1. (1971-1981) Operation Ivy Bells: https://en.wikipedia.org/wiki/Operation_Ivy_Bells

        1. (2003-) Room 641A: https://en.wikipedia.org/wiki/Room_641A

        1. (2008-) PRISM: https://en.wikipedia.org/wiki/PRISM_(surveillance_program)

        1. (2015-) NSA's Utah Datacenter: https://nsa.gov1.info/utah-data-center/

    1. Incidents:

        1. Syria internet blackout: https://www.washingtonpost.com/news/worldviews/wp/2013/05/08/how-did-syria-cut-off-the-entire-country-from-the-internet/

            1. Telecommunications without borders helps Syria overcome the blackouts: https://www.tsfi.org/en/our-missions/disaster-response/syria-crisis

            1. Syrian blackout caused by the NSA according to Snowden: https://www.theguardian.com/world/2014/aug/13/snowden-nsa-syria-internet-outage-civil-war

        1. Vietnam has regular internet outages due to cable breakages: https://saigoneer.com/saigon-technology/11885-sharks,-anchors-red-tape-why-it-takes-forever-to-fix-vietnam-s-broken-internet-cables

1. In Facebook's case, the cables got "logically" disconnected

    1. Every computer on the internet has an IP address, and all communication on the internet is between IP addresses

       Find yours here: https://whatismyipaddress.com/

       DNS associates a domain name with an IP address for convenience

       | domain | ip address |
       | ------ | ---------- |
       | facebook.com | 157.240.11.35 |
       | google.com | 142.250.68.14 |

       IP addresses are 4 byte numbers

       1. Each number between the `.` is 1 byte

       1. 1 byte stores numbers between 0-255

       1. 4 bytes stores numbers up to 4.2 billion

       1. Bad News: there's not enough IP addresses for everyone in the world!

           1. Most of you are probably using multiple IP addresses (phone, laptop, etc.)

           1. IP addresses are expensive: https://ipv4marketgroup.com/ipv4-pricing/

    1. To send a message from your computer to Facebook, your computer sends information through many different computers called "routers"

        1. CISCO is the most famous company for making routers: https://www.cisco.com/c/en/us/products/routers/index.html#~products

        1. Each router has a big internal table of which IP addresses correspond to which physical connections

        1. A protocol called BGP (Border Gateway Protocol) is how routers communicate which IPs are in which locations

        1. Facebook misconfigured their BGP settings, telling all the routers in the world that their IPs no longer exist

        1. So every router stopped sending traffic to facebook IPs

1. Fully understanding all these details requires multiple graduate-level networking courses

## Lab

### Part I

Please complete the following survey about how class is going so far: https://docs.google.com/forms/d/1Weuolk5Q9RsmqVFiF8Qgbc1cd_LQNiKMY-RYAq1SPlg

The survey is 100% anonymous, and it will help me adjust the course moving forward.

### Part II

Complete the doctests in the `lab.py` and upload the results to sakai.

### Part III (optional/extra credit)

You may earn 1 point of extra credit (and so get a 6/5 on the lab) if you translate the phrase "python is awesome" into at least 100 languages and upload these translations to sakai.
Fortunately, there is a python interface to google translate,
so you don't have to do this manually...
I fill gross just thinking about doing this manually...
you can just use a for loop!

The python library is called `deep_translator`,
and it provides interfaces to many different translation services.
You can find the documentation at https://pythonrepo.com/repo/nidhaloff-deep-translator-python-miscellaneous ,
although you won't need to look in detail at the documentation to complete this assignment.

You can install `deep_translator` library similarly to how you installed `youtube-dl` library, using the `pip3` command.
The command should look something like
```
$ pip3 install deep_translator
```

Then you can translate from English to Spanish using the following commands in interactive python:
```
from deep_translator import GoogleTranslator
>>> GoogleTranslator(source='en', target='es').translate("python is awesome")
'Python es asombroso'
```
We can also get the list of all supported languages using the command
```
>>> GoogleTranslator.get_supported_languages()
['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu', 'Filipino', 'Hebrew']
```
Now, to complete the assignment, all you have to do is loop over the list above, calling the translate function with `target=` each of the supported languages.
