# Week 10 + 11: Reddit Bots

<center>
<img width=300px src=duty_calls.png />
</center>

We will be covering how to use the PRAW library this week for making reddit bots.
The textbook does not cover this topic,
but you can find the library's (excellent) documentation here:
<https://praw.readthedocs.io/>

You will need to:

1. create a new reddit account just for this class at the link <https://www.reddit.com/login/>

    1. the word `bot` must be in the account name somewhere

    1. do not include personally identifying information in the account name

1. create a reddit "script application" at the link <https://www.reddit.com/prefs/apps>

## Lab

**Part I:**

On the eleventh hour of the eleventh day of the eleventh month of 1918, an armistice came into effect that effectively ended the First World War.
To honor [Armistice Day](https://en.wikipedia.org/wiki/Armistice_Day),
the `ArmisticeBot` has posted a variety of war poetry to the [/r/cs40_2022fall Lounge](https://www.reddit.com/r/cs40_2022fall/comments/yoc6la/rcs40_2022fall_lounge/) on reddit.
For example, [here's a link](https://www.reddit.com/r/cs40_2022fall/comments/yoc6la/rcs40_2022fall_lounge/ivx2fnu/) to a comment containing Wilfred Owen's *Dulce et Decorum Est*.

Your task is to list the titles of the poems that `ArmisticeBot` has posted,
and the number of times that each poem has been posted.
To complete this task, you should create a python file that:

1. loads the PRAW library and connects to reddit
1. creates a submission variable based on the url <https://www.reddit.com/r/cs40_2022fall/comments/yoc6la/rcs40_2022fall_lounge/>
1. loops over all comments in the submission (not just top level comments) in order to:
    1. check if the comment is posted by `ArmisticeBot`
    1. if it is, then the title of the poem will be the first line of the submission's text
    1. create a dictionary that will have keys as the titles of the poems and values as the number of times this poem has appeared

Once you believe your code is working, then use the `.replace_more` function to ensure that you're looping over all the comments.
Recall that you don't want to use this function while you are initially writing your code because it will slow down your ability to get feedback on whether your code is working or not.

When you are finished, upload to sakai:

1. your python file
1. the results computed by your python file

**Part II:**

Complete the "madlibs lab" in the [/project_04/lab-madlibs](/project_04/lab-madlibs) folder.

<!--
Week 10: [/hw_04/lab-PRAW](/hw_04/lab-PRAW).

Week 11: 
-->
