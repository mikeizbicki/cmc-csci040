# Week 08: Web Scraping

<center>
<img width=600px src=Strip-Hackers-VS-Security-team-650-finalenglish1.jpg />
</center>

**Grades:**

<img src=grades.png width=400px />

1. **WARNING:** Historically, many students lose lots of points on project 2 for not following directions.

    1. This was one of the main causes of losing points on project 1.  (Not uploading the right screenshots.)

1. My teaching philosophy:

    1. The best way to learn a programming language is the same as the best way to learn a human language: immersion.

        That means you're going to feel lost at times... but that's how the professionals feel too!

        <img src=two-states-of-programmers.png width=400px />

    1. Assignments should not be busy work, but actually help you get a job.

        1. Should I add more work to the course?

            *HINT:* [Betterridges's law of headlines](https://en.wikipedia.org/wiki/Betteridge%27s_law_of_headlines) says "no".

            From the [how to become a hacker](http://www.catb.org/~esr/faqs/hacker-howto.html):

            > Boredom and drudgery are evil.

        1. Why do we have github-based projects?
        
            From Google's HR Chief Laszlo Bock (via [qz.com](https://qz.com/382570/goldman-sachs-actually-google-gpas-arent-worthless)):

            > We did a bunch of analysis and found that grades are a little predictive your first two years, but for the rest of your career don’t matter at all.

            So good grades aren't enough, and you need portfolios of projects to show employers.

**Material:**

1. We will go over how to download information from the internet using the `requests` library in python.
    The lecture will be based off of the following three references:

    1. https://automatetheboringstuff.com/2e/chapter12/

    1. https://realpython.com/python-requests/

    1. https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

    Legality of web scraping:

    1. https://www.eff.org/deeplinks/2018/04/dc-court-accessing-public-information-not-computer-crime

    1. https://www.eff.org/cases/hiq-v-linkedin

    1. https://en.wikipedia.org/wiki/Web_scraping#Legal_issues

    <!--
    How HTTP headers are used to track you online

    1. https://panopticlick.eff.org/

    1. https://amiunique.org/faq
    -->

    <!--
    Examples of webscraping in action:

    1. Getting a lifetime supply of garlic pizza sticks: https://www.reddit.com/r/programming/comments/jbjgtj/how_i_used_python_and_selenium_to_get_a_lifetime/
    -->

1. We will go over the `argparse` library for building command line interfaces.
   This library comes with python and does not need to be installed.

   References:

   1. https://realpython.com/command-line-interfaces-python-argparse/

   1. https://docs.python.org/3/library/argparse.html

1. We will go over the beautiful soup (`bs4`) library.

    In order to use this library, you need to understand css selectors.
    We covered this at the beginning of the semester, but you may have forgot.
    You can use the following video to review:

    1. https://www.youtube.com/watch?v=dcCCOiQ1ZuM

    You can use the following references for more details about the `bs4` library:

    1. https://automatetheboringstuff.com/2e/chapter12/

    1. https://realpython.com/beautiful-soup-web-scraper-python/

<!--
**Wednesday:**

I will implement a solution to [hw\_03](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03)
-->

**Facebook goes down (2021)** or Kakao goes down (2022):

Background:
    1. All Facebook properties were down for about 6-14 hours on Tuesday 04 October 2021

        1. It has it's own wikipedia page: https://en.wikipedia.org/wiki/2021_Facebook_outage

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

TBA
<!--
Complete the functions in `lab.py` and optionally `lab_ec.py`.
Upload the output of running the doctests to sakai.
-->
