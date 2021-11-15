# Reddit Bot Lab II: Text Generation

<center>
<img width='80%' src=cartoon.png />
</center>

## Overview

In the last lab you learned how to programmatically read/write messages to reddit.
In this lab, we will focus on generating realistic content for the messages you will write for the homework.

**Required readings:**

* [Documenting the tactics of an anti-net neutrality bot campaign](https://hackernoon.com/more-than-a-million-pro-repeal-net-neutrality-comments-were-likely-faked-e9f0e3ed36a6).
  This campaign used the same MadLibs algorithm you'll be implementing in lab.

* [The GPT-2 model for generating much more realistic text](https://www.theguardian.com/technology/2019/jul/04/ai-fake-text-gpt-2-concerns-false-information)

**Optional readings:**

* [A more technical description of GPT-2](https://blog.floydhub.com/gpt2/)
    and a [tutorial for creating GPT-2 reddit bots](https://bonkerfield.org/2020/04/twenty-minute-gpt2-reply-bot/)

* More examples of automatic text generation:

  _WARNING: Potentially NSFW_

    * Bots talking to each other:
        
        * Using "Madlibs" (1960s tech): <https://www.reddit.com/r/csci040temp/>

        * Using Markov Chains (1990s tech): <https://www.reddit.com/r/SubredditSimulator/>

        * Using GPT-2 (2019 tech): <https://www.reddit.com/r/SubSimulatorGPT2/>

    * Bots writing memes: <https://www.reddit.com/r/aigeneratedmemes/top/>

**How do these advanced CS algorithms work?**

<img width=800px src=math.webp />

## Lab Instructions

1. In the first part of this lab, you'll experiment with the state-of-the-art text generation technique called GPT-3.
   Create a free account at <https://play.aidungeon.io/>, and play around with the game for 10-20 minutes.
   I personally find that the game generates realistic sentences and paragraphs, but it has trouble making longer cohesive narratives.
   But it's still pretty amazing/scary how good it is.

1. For our reddit bots, we will be using a much simpler MadLibs-style text generation algorithm.
   Follow the instructions in the `madlibs.py` file to implement this algorithm and post some basic messages to reddit.
