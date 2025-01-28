# Topic 01: More front-end web development

<img width='50%' src=img/Strip-Vengeance-de-codeur-650-finalenglish.jpg />

**Monday:** Cascading Style Sheets (CSS)

1. We will be covering Chapter 3 in Shay Howe's [HTML & CSS](https://learn.shayhowe.com/html-css/) book.
    Last week we covered chapters 1-2.

1. The most important concept to learn is the *CSS selector*.
    1. Must understand the parent/child/sibling/etc relationship between HTML nodes.
    1. CSS selectors will be vital for understanding web scraping.
    1. Quiz on Thursday.

        See `practice_quiz1.pdf` and `practice_quiz2.pdf` for example problems.

        You will have the first 10 minutes of class to complete the quiz.

        I will arrive 10 minutes early, and you can also start before class if you'd like.
    1. The following Javascript can be used to get the answer to any quiz problem.
        Enter it the Firefox *debug console* (which you can open by pressing F12).
        ```
        document.querySelectorAll('selector') 
        ```

1. Starting next week, we will focus on back-end dev rather than front-end dev.
    There's a LOT more to front-end dev that we're not covering (we're only doing like 10% of Shay Howe's book),
    and backend devs tend to not know much about frontend dev...

    <!--
    <img width='40%' src=img/Strip-High-Level-CSS-english650-final-1.jpg />
    &nbsp;
    -->
    <img width='50%' src=img/Strip-CSS-respect-650-finalenglish1.jpg />

## Lab

We will use the first portion of the lab time to go over the CSS quiz that will happen next week.

<img width=40% src=img/photoshop.jpg>

Prelab videos:

1. Matt Cutts was formerly the head of Google's web spam team,
   and now runs the United States Digital Service (a recently created branch of the US government).
   Watch his video on [How Google Search Works](https://www.youtube.com/watch?v=KyCYyoGusqs).

1. [Whitehat vs blackhat SEO](https://www.youtube.com/watch?v=jOSz-uutUfc)

Instructions:

1. Select a high profile user from [X/Twitter](https://x.com/), [BlueSky](https://bsky.app/), or [Mastodon](https://mstdn.social/explore).
    Use Firefox's developer console to edit one of their messages to say something they would never say.
    Take a screenshot and post the screenshot to GitHub Issues here: <https://github.com/mikeizbicki/cmc-csci040/issues/324>.

    You can find examples from previous semesters at:
    1. <https://github.com/mikeizbicki/cmc-csci040/issues/242>
    1. <https://github.com/mikeizbicki/cmc-csci040/issues/86>

<!--
1. (Optional) How to remove ads/popups/other crap from websites:

    1. uBlock Origin internally uses css selectors to block ads on webpages.
       It contains a large list of these selectors that have been manually curated,
       and all elements on a page that match one of these selectors will be removed from the webpage.
       In this portion of the lab, you will explore how to create these rules for yourself to block content on a webpage.
       
    1. First, you'll need to find a webpage that has content on it that you want to block.
       I recommend using https://nytimes.com and blocking the blue login buttons on the top-right of the screen.
       (Because this is a popular webpage, there are already rules for blocking all the ads and paywall popups,
       so we can't add rules for these.)

    1. Follow the instructions on [this webpage](https://www.ghacks.net/2017/02/21/ublock-origin-how-to-remove-any-element-from-a-page-permanently/) to create a rule for blocking the popup permanently with uBlock Origin. 

    1. If you'd like to learn more details about the rules uBlock Origin uses,
       you can visit [this webpage](https://adblockplus.org/filter-cheatsheet#elementhideemulation).
-->

1. Start working on project_00.

   > **HINT:** Now would be a good time to arrange with other students in the class to share backlinks to each other's websites!

    <img width='100%' src=img/comic14.gif />

> **NOTE:**
> There is nothing to submit on sakai for this lab.
