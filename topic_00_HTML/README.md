# Week 00: Front-end web development

<center>
<img width='100%' src=img/ft111002-foxtrot-comics-bill-amend-html-tag-jason-marcus-sunday-comic-strip.png />
</center>

**Monday:** Course Intro

**Wednesday:** HTML

1. Prelecture videos:

    > **NOTE:**
    > You will not be directly graded on the content of these videos,
    > but they provide useful background information that will make lectures much easier to follow.
    > I understand the temptation to not watch them---and I probably wouldn't have as a student either---but even the most technically inclined students will not have seen a lot of the information in these videos.
    >
    > One of the [three virtues of a programmer is laziness](https://thethreevirtues.com/).
    > I am lazy and I hope to train you all to be lazy in this course. 
    > So one of my commitments to you all is that I will never ask you to do busywork.

    1. [Inside a google data center](https://www.youtube.com/watch?v=XZmGGAbHqa0)

    1. (Optional) [Inside a Facebook data center](https://www.youtube.com/watch?v=_r97qdyQtIk)

    1. (Optional) [Inside Amazon web services (AWS)](https://www.youtube.com/watch?v=94PO2-TL4Vs)

    1. (optional) [How a philosophy major from a liberal arts college with 2.4 GPA got jobs at Facebook and Uber making $300k as a data scientist](https://www.youtube.com/watch?v=YGflHj1SjA4&t=2m15s)

    <!--
    1. (optional) [Data science expectations vs reality](https://www.youtube.com/watch?v=8LucP1wiX1g)
    -->

    Watch the following videos if you don't already understand the key terms listed below.

    1. [How the web works - the big picture](https://www.youtube.com/watch?v=hJHvdBlSxug)

        Key terms you should understand:

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

    1. [Three types of web development](https://www.youtube.com/watch?v=Kg0Q_YaQ3Gk)

        Key terms you should understand:

        * Static websites
        * Static site generator
        * Dynamic websites
        * Single page apps

1. Prelecture tasks:

    > **NOTE:**
    >
    > Throughout this course we will be installing lots of software.
    > You are welcome to use lab computers, but most students choose to use your own laptops.
    > Unlike in other classes, all of the software we use is open source, so you can freely download it on your own machine and keep access to it after the semester/graduation.
    > Due to security reasons, this software cannot be preinstalled on the lab machines,
    > and so you must install it yourself for each computer that you choose to use.
    > If you change computers, you will have to reinstall the needed software.

    1. [Install VSCodium](https://vscodium.com/).
        VSCodium is the open source version of [Microsoft's VSCode](https://code.visualstudio.com/Download).
        The only difference is that VSCode contains additional tracking plugins that allows Microsoft to monitor what you do and run code on your computer,
        which.

    1. [Install Firefox](https://www.mozilla.org/en-US/exp/firefox/new/).
        Chome/Safari/Internet Explorer are not acceptable alternatives for this class.

    1. Install and enable the following Firefox plugins:

        1. [uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/) for blocking ads.

            1. uBlock Origin is widely considered by hackers to be the best existing adblocker.
                Other adblockers either sell your browsing info to advertisers or allow advertisers to pay to have their ads not blocked.

            1. It is possible to use uBlock Origin from chrome, but chrome has some anti-adblocker technology built into it that makes it less effective.
                If you're interested in technical details about why this is the case, see https://github.com/gorhill/uBlock/wiki/uBlock-Origin-works-best-on-Firefox .

        1. [Decentraleyes](https://addons.mozilla.org/en-US/firefox/addon/decentraleyes/) reduces how much online web companies can track you.

        1. (optional) [uMatrix](https://addons.mozilla.org/en-US/firefox/addon/umatrix/) provides even more fine-grained control over what the websites that you access are allowed to do.

            This is an advanced extension, and so you should only install it if you are willing to perform a lot of configuration work.
            I personally use it to browse the internet, but I can understand why many people would choose not to.
            The documentation states:

            > uMatrix does not guarantee that sites will work fine: it is for advanced users who can figure how to un-break sites, because essentially uMatrix is a firewall which works in relaxed block-all/allow-exceptionally mode out of the box: it is not unexpected that sites will break.

    1. If you do not already have a GitHub account,
       then [create one](https://github.com/join).

       You may choose any username that you like.
       Job applications commonly ask for GitHub profiles,
       so you should pick something professional that you would want to share with them.

       When prompted for the account type, choose the free account option.

1. Cheatsheets

    In this class, you are encouraged to use cheatsheets for all labs, projects, and quizzes.

    You can find links to the electronic versions of the cheatsheets in this project folder.

    Quizzes will be open note.

## Lab

<center>
<img width='100%' src=img/dt160320.jpg />
</center>

**tl;dr**
The goal of this lab is to publish a simple webpage online so that others can view it.
This is the first step in completing [project\_00](/project_00/).

**Prelab Instructions:**

Ensure that you have pressed the "watch" button at the top of this webpage.
Read and follow the instructions in [Issue #320: the meet and greet thread](https://github.com/mikeizbicki/cmc-csci040/issues/236).

Watch the following videos if you're not already familiar with their contents:
    
1. [What is github?](https://www.youtube.com/watch?v=w3jLJU7DT5E)

1. [Understanding GitHub Issues](https://www.youtube.com/watch?v=TKJ4RdhyB5Y)

1. [The rise of open source software](https://www.youtube.com/watch?v=SpeDK1TPbew)

1. "Creative Commons" is a type of open source license for non-code (books, webpages, music, images, etc.).
    Watch [this video explaining Creative Commons licences](https://www.youtube.com/watch?v=4ZvJGV6YF6Y).

1. [Quick Google Analytics introduction](https://www.youtube.com/watch?v=RL61v47WyHs)

**Instructions:**

The lectures/videos have not explicitly covered how to do most of the tasks in this lab.
The main purpose of this lab is to get you comfortable trying to read and figure out documentation...
even if that means just trying random stuff until it works.

1. [Follow these directions](https://pages.github.com/) to create a GitHub Pages webpage.
   In the step marked `?` (after step `1` and before step `2`),
   select `I don't know` for `What git client are you using?`.
   This will give you instructions on how to install the GitHub Desktop program for your operating system.

1. [Follow these directions](https://creativecommons.org/choose/) to include a creative commons license on your webpage.
   You may select any version of the license.

   > **NOTE:**
   > This requires that you add a snippet of HTML to your webpage.
   > (I recommend the very bottom, but any location is fine.)
   > Whenever you modify your webpage,
   > you will have to go through the process of uploading your files to github using GitHub Desktop again.

1. [Follow these instructions](https://support.google.com/analytics/answer/1008015?hl=en) to create a Google Analytics account and add Google Analytics to your webpage.

   > **NOTE:**
   > Once again, you must modify your HTML in order to insert the required `<script>` tag into your webpage.
   > Every time you modify your webpage, you must go through the process of uploading with GitHub Desktop.

   > **NOTE:**
   > Google Analytics does NOT work when you have uBlock Origin activated.
   > To ensure that Google Analytics is correctly working,
   > you should temporarily disable uBlock Origin.
   > Then, you can visit your google analytics page to see that it registers you as a visitor.

1. [Follow these instructions](https://developers.facebook.com/docs/plugins/like-button/) to create a Facebook Like button for your webpage.

   Like with Google Analytics, Facebook Like buttons do not work when the adblock plugins are enabled.

   > **NOTE:**
   > Don't forget to upload with GitHub Desktop!
   > Facebook's like button and google analytics will both be broken if your webpage is only served "locally" from your own computer and not from a web server like github.

1. Get at least 5 people to like your webpage on Facebook,
   and 5 people to star your webpage's repo on GitHub.
   I recommend using the lab time to trade likes/stars with other students.

   > **NOTE:**
   > The reason for getting these likes and stars is that github and google search also use stars to help rank webpages in search results.
   > More stars means higher rankings in the search results.
   > For the project, you will also have to get links from other webpages.
   > So now would also be a good time to trade these links (although it's not explicitly required for the lab).

1. Upload the url to your completed webpage to sakai.
