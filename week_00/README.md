# Week 00: Front-end web development

<center>
<img width='100%' src=ft111002-foxtrot-comics-bill-amend-html-tag-jason-marcus-sunday-comic-strip.png />
</center>

*Monday:* Course Intro

*Wednesday:* HTML

1. Prelecture videos:

    1. [Data Science: Reality vs Expectations](https://www.youtube.com/watch?v=8LucP1wiX1g)

    1. [Inside a google data center](https://www.youtube.com/watch?v=XZmGGAbHqa0)

    1. (Optional) [Inside a Facebook data center](https://www.youtube.com/watch?v=_r97qdyQtIk)

    1. (Optional) [Inside Amazon web services (AWS)](https://www.youtube.com/watch?v=94PO2-TL4Vs)

    1. [How the web works - the big picture](https://www.youtube.com/watch?v=hJHvdBlSxug)

        Key terms:

        * Browser
        * Server
        * URL
        * Domain
        * IP Address
        * DNS
        * HTML
        * CSS
        * Javascript
        * HTTP
        * HTTPS

    1. (Optional) [Three types of web development](https://www.youtube.com/watch?v=Kg0Q_YaQ3Gk)

        Key terms:

        * Static websites
        * Static site generator
        * Dynamic websites
        * Single page apps

1. Prelecture tasks:

    NOTE:
    Throughout this course we will be installing lots of software.
    You are welcome to use lab computers, but most students choose to use your own laptops.
    Unlike in other classes, all of the software we use is open source, so you can freely download it on your own machine and keep access to it after the semester/graduation.
    Due to security reasons, this software cannot be preinstalled on the lab machines,
    and so you must install it yourself for each computer that you choose to use.
    If you change computers, you will have to reinstall the needed software.

    1. [Install VSCode](https://code.visualstudio.com/Download) (or if you don't want Microsoft tracking you, install the open source version [VSCodium](https://vscodium.com/))

    1. [Install Firefox](https://www.mozilla.org/en-US/exp/firefox/new/)
       (Chome/Safari/Internet Explorer are not acceptable alternatives for this class.)

    1. Install and enable the following Firefox plugins:

        1. [uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/) for blocking ads.

            1. uBlock Origin is widely considered by hackers to be the best existing adblocker.
                Other adblockers either sell your browsing info to advertisers or allow advertisers to pay to have their ads not blocked.

            1. It is possible to use uBlock Origin from chrome, but chrome has some anti-adblocker technology built into it that makes it less effective.
                If you're interested in technical details about why this is the case, see https://github.com/gorhill/uBlock/wiki/uBlock-Origin-works-best-on-Firefox .

        1. [Decentraleyes](https://addons.mozilla.org/en-US/firefox/addon/decentraleyes/) reduces how much online web companies can track you.

    1. If you do not already have a GitHub account,
       then [create one](https://github.com/join).

       You may choose any username that you like.
       Job applications commonly ask for GitHub profiles,
       so you should pick something professional that you would want to share with them.

       When prompted for the account type, choose the free account option.

**Friday:**

1. Prelecture videos:
    
    1. [What is github?](https://www.youtube.com/watch?v=w3jLJU7DT5E)

    1. [The rise of open source software](https://www.youtube.com/watch?v=SpeDK1TPbew)

    1. "Creative Commons" is a type of open source license for non-code (books, webpages, music, images, etc.).
        Watch [this video explaining Creative Commons licences](https://www.youtube.com/watch?v=4ZvJGV6YF6Y)

    1. [Understanding GitHub Issues](https://www.youtube.com/watch?v=TKJ4RdhyB5Y)

    1. [Quick Google Analytics introduction](https://www.youtube.com/watch?v=RL61v47WyHs)

## Lab

<center>
<img width='100%' src=dt160320.jpg />
</center>

The goal of this lab is to publish a simple webpage online so that others can view it.
This is the first step in completing [hw\_00](/hw_00/).

Instructions:

1. Ensure that you have pressed the "watch" button at the top of this webpage.
   Read and follow the instructions in [Issue #1: the meet and greet thread](https://github.com/mikeizbicki/cmc-csci040/issues/1).

1. [Follow these directions](https://pages.github.com/) to create a GitHub Pages webpage.
   In the step marked `?` (after step `1` and before step `2`),
   select `I don't know` for `What git client are you using?`.
   This will give you instructions on how to install the GitHub Desktop program for your operating system.

1. [Follow these directions](https://creativecommons.org/choose/) to include a creative commons license on your webpage.
   You may select any version of the license.

   NOTE: 
   
   1. This requires that you add a snippet of HTML to your webpage.
      (I recommend the very bottom, but any location is fine.)
      Whenever you modify your webpage,
      you will have to go through the process of uploading your files to github using GitHub Desktop again.

1. [Follow these instructions](https://support.google.com/analytics/answer/1008015?hl=en) to create a Google Analytics account and add Google Analytics to your webpage.

   NOTE: 
   
   1. Once again, you must modify your HTML in order to insert the required `<script>` tag into your webpage.
      Everytime you modify your webpage, you must go through the process of uploading with GitHub Desktop.

   1. Google Analytics does NOT work when you have uBlock Origin or uMatrix activated.
      To ensure that Google Analytics is correctly working,
      you should temporarily disable these plugins.
      Then, you can visit your google analytics page to see that it registers you as a visitor.

1. [Follow these instructions](https://developers.facebook.com/docs/plugins/like-button/) to create a Facebook Like button for your webpage.

   Like with Google Analytics, Facebook Like buttons do not work when the adblock plugins are enabled.

   NOTE:

   1. Don't forget to upload with GitHub Desktop!

1. Get at least 5 other students from class to like your webpage on Facebook,
   and 5 other students to "star" your webpage's repo on GitHub.
   You can use the zoom chat or the GitHub issues to communicate with the other students.

1. Upload the url to your completed webpage to sakai.
