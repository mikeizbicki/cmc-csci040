# Week 00: HTML + git

<center>
<img width='100%' src=img/ft111002-foxtrot-comics-bill-amend-html-tag-jason-marcus-sunday-comic-strip.png />
</center>

**Wednesday:** HTML

1. Cheatsheets

    In this class, you are encouraged to use cheatsheets for all labs, projects, and quizzes.

    You can find links to the electronic versions of the cheatsheets in this topic folder above.

## Lab

<center>
<img width='100%' src=img/dt160320.jpg />
</center>

**tl;dr**
The goal of this lab is to publish a simple webpage online using git.
This is the first step in completing [project\_00](/project_00/).

### Prelab Instructions:

1. Install the following software:

    > **NOTE:**
    > Throughout this course we will be installing lots of software.
    > You are welcome to use lab computers, but most students choose to use your own laptops.
    > Unlike in other classes, all of the software we use is open source, so you can freely download it on your own machine and keep access to it after the semester/graduation.
    > Due to security reasons, this software cannot be preinstalled on the lab machines,
    > and so you must install it yourself for each computer that you choose to use.
    > If you change computers, you will have to reinstall the needed software.

    1. [Install VSCodium](https://vscodium.com/).
        VSCodium is the open source version of [Microsoft's VSCode](https://code.visualstudio.com/Download).
        The only difference is that VSCode contains additional tracking plugins that allows Microsoft to monitor what you do and run code on your computer.
        If you already have VSCode installed, you may use that instead.

    1. Install git.

        1. (Non-windows users)
            Go to <https://git-scm.com/install/> and follow the instructions for your OS.
            VSCodium will automatically be integrated with git after the install.

        1. (Windows-users)
            You will need to follow some special steps to integrate git with VSCodium.
            Find instructions for installing and configuring with VSCodium at on [this stackoverflow question](https://stackoverflow.com/questions/42606837/how-do-i-use-bash-on-windows-from-the-visual-studio-code-integrated-terminal/50527994#50527994).

    1. [Install Firefox](https://www.mozilla.org/en-US/exp/firefox/new/).
        Chome/Safari/Internet Explorer are not acceptable alternatives for this class.
        We will be doing things with firefox that do not work with these other browsers.

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

       > **NOTE:**
       > In the programming world, an alias like `phantomHaxor1337` [would be considered professional](https://archive.nytimes.com/www.nytimes.com/library/review/031200hacker-handles-review.html).
       > Anything that is not sexual or racist is acceptable.
       >
       > Using an alias that is not your legal name is particularly advisable if your legal name is hard for native English speakers to pronounce.
       > (It's not fair, but it's true.)

       > **NOTE:**
       > My primary github account name is `mikeizbicki`.
       > I have other accounts with more hacker pseudonymns.
       > If you are able to find any of these other pseudonymns that I use online, you will earn my respect :)

       When prompted for the account type, choose the free account option.

1. Ensure that you have pressed the "watch" button at the top of this webpage.
    Read and follow the instructions in [#371: the meet and greet thread](https://github.com/mikeizbicki/cmc-csci040/issues/371).

1. Watch the following videos.

    > **NOTE:**
    > You will not be directly graded on the content of these videos,
    > but they provide useful background information that will make lectures easier to follow.
    > I understand the temptation to not watch them---and I probably wouldn't have as a student either---but even the most technically inclined students will not have seen a lot of the information in these videos.
    >
    > One of the [three virtues of a programmer is laziness](https://thethreevirtues.com/).
    > I am lazy and I hope to train you all to be lazy in this course.
    > So one of my commitments to you all is that I will never ask you to do busywork.

    1. [Inside a google data center](https://www.youtube.com/watch?v=XZmGGAbHqa0)

    1. (Optional) [Inside a Facebook data center](https://www.youtube.com/watch?v=_r97qdyQtIk)

    1. (Optional) [Inside Amazon web services (AWS)](https://www.youtube.com/watch?v=94PO2-TL4Vs)

    1. Watch the following videos if you don't already understand the key terms listed below.

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

1. (optional) [What is github?](https://www.youtube.com/watch?v=w3jLJU7DT5E)

1. (optional) [Understanding GitHub Issues](https://www.youtube.com/watch?v=TKJ4RdhyB5Y)

1. (optional) [Quick Google Analytics introduction](https://www.youtube.com/watch?v=RL61v47WyHs)

<!--
1. [The rise of open source software](https://www.youtube.com/watch?v=SpeDK1TPbew)

1. "Creative Commons" is a type of open source license for non-code (books, webpages, music, images, etc.).
    Watch [this video explaining Creative Commons licences](https://www.youtube.com/watch?v=4ZvJGV6YF6Y).
-->

### Instructions

I will walk through the following steps with you in class.

1. [Follow these instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) to create a *personal access token* (PAT) for github.

1. [Follow these instructions](<https://docs.github.com/en/pages/quickstart>) to create a github pages website.

1. Upload a file to your webpage by:

    1. In the terminal, run the following commands to download your github repository onto your local computer:
        ```
        $ git clone https://github.com/<username>/<username>.github.io
        $ cd <username>.github.io
        ```

        > **NOTE:**
        > The `$` is called the *prompt*.
        > This symbol indicates that everything following the `$` is a terminal command (and not for example an HTML command or python command).
        > When entering these commands into the terminal, you should copy/paste everything to the right of the `$` but not the `$`.
        > Whenever you see `<username>` in the commands above, you should replace that with your actual github username.

    1. Create a file `index.html` inside the `<username>.github.io` folder with the following content:

        ```
        <b>hello</b> <i>world</i>!
        ```

    1. Run the following terminal commands to upload your `index.html` file to github.

        ```
        $ git add index.html
        $ git commit -m 'initial commit'
        $ git push origin main
        ```

        > **NOTE:**
        > Whenever you make a change to your files locally, you will need to re-run the `git add`, `git commit`, and `git push` commands above to upload to github.
        > You will need to do this several times throughout the lab in the steps below.

**Part 2:**

Complete the instructions in the [messages repo](https://github.com/mikeizbicki/messages/) to practice github and meet your classmates.

**Part 3:**

You will complete the following steps without a live demo from me.
I encourage you to work with your neighbors and ask me questions.

> **NOTE:**
> Our lectures have not explicitly covered how to do most of the tasks in this lab.
> The main purpose of this lab is to get you comfortable trying to read and figure out documentation...
> even if that means just trying random stuff until it works.

1. [Follow these directions](https://creativecommons.org/choose/) to include a creative commons license on your webpage.
   You may select any version of the license.

   > **NOTE:**
   > This requires that you add a snippet of HTML to your webpage.
   > (I recommend the very bottom, but any location is fine.)
   > Whenever you modify your webpage,
   > you will have to go through the process of uploading your files to github again.

1. [Follow these instructions](https://support.google.com/analytics/answer/1008015?hl=en) to create a Google Analytics account and add Google Analytics to your webpage.

   > **NOTE:**
   > Don't forget to upload your modified file to github!

   > **NOTE:**
   > Google Analytics does NOT work when you have uBlock Origin activated.
   > To ensure that Google Analytics is correctly working,
   > you should temporarily disable uBlock Origin.
   > Then, you can visit your google analytics page to see that it registers you as a visitor.

1. [Follow these instructions](https://developers.facebook.com/docs/plugins/like-button/) to create a Facebook Like button for your webpage.

   Similar to Google Analytics, Facebook Like buttons do not work when the adblock plugins are enabled.

   > **NOTE:**
   > Don't forget to upload to github!

1. Get at least 5 people to like your webpage on Facebook,
   and 5 people to star your webpage's repo on GitHub.
   I recommend using the lab time to trade likes/stars with other students.

   > **NOTE:**
   > The reason for getting these likes and stars is that github and google search also use stars to help rank webpages in search results.
   > More stars means higher rankings in the search results.
   > For the project, you will also have to get links from other webpages.
   > So now would also be a good time to trade these links (although it's not explicitly required for the lab).

1. Upload the url to your completed webpage to canvas.

    The lab is nominally due on Sunday at midnight,
    but I won't deduct any late points if you miss this first deadline so that you have a chance to get any help that you need.
