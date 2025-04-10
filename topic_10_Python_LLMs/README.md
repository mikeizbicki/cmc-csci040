# Topic 10: Using LLMs from within Python

<img src=img/chatgpt.png width=300px />

**Learning objectives:**

1. Understand how to use LLMs from python
1. Understand 2 common security mistakes with LLMs
    1. key leaking
    1. prompt injection
1. Get more practice using real world documentation

## Lecture Notes

We will write a simple program to summarize an input document.

I will do most of the steps in class, and you get to follow along.

You will still have to submit your finished product to sakai.

### Step 0: Project Setup

Create a new project folder `docsum`.

Create an account and API key at <https://groq.com/>.
Groq is a [pre-revenue LLM startup](https://www.youtube.com/watch?v=BzAdXyPYKQo) focused on developing faster hardware to compete with NVIDIA.

Create a file `.env` that contains your API key in the form
```
GROQ_API_KEY=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
```

### Step 1: Get a Basic Example Working

The Groq company has a python library called `groq`.
You can find basic examples here: <https://github.com/groq/groq-python#usage>

Under the hood, the python library uses a web API.
The documentation at <https://console.groq.com/docs/> uses this API,
but you do not need to interact with the API directly.

You will need to use the `python-dotenv` library to store your API keys: <https://github.com/theskumar/python-dotenv>

<!--
The python library `groq` is also compatible with the openai api: <https://console.groq.com/docs/openai>
-->

### Step 2: Create the Document Summarizer

Create a file `docsum.py` that:
1. takes a file (of any type) as a command line argument
1. summarizes that file using the Groq API

> **Useful links:**
>
> 1. <https://docs.python.org/3/library/argparse.html>
> 1. ~~<https://github.com/btimby/fulltext>~~
> 
>   <https://github.com/deanmalmgren/textract>
>
> <img src=img/google.jpg width=300px />

> **Announcement (2025-04-08):**
> 
> Over the weekend, facebook released the new Llama4 series of models.
> You can find details at <https://ai.meta.com/blog/llama-4-multimodal-intelligence/>.
>
> These models are available on groq,
> and you will be required to use the llama4 model for your submission.
> You can find details on the supported groq models at: <https://console.groq.com/docs/models>.

### Step 3: Submit Project

Create a `README.md` file.
1. The file should explain what your `docsum.py` file does and how to use it.
    (You must have a code block that shows example usage and output.)
1. The file should use reasonable markdown styling.
    (Especially with code blocks vs inline code.)

Create a new github project for your repo.
Commit and upload all of your changes.

Submit the link to your github repo on sakai.

<!--
> **NOTE:** (Wednesday, 4 Sep 2024)
>
> Today in class, we will cover:
>
> 1. Using github actions with LLMs for continuous integration.
>    
>    This is harder than normal due to the API keys.
>
> 1. Writing good test cases for programs with LLMs.
>
>    Again, harder than normal due to the random nature of LLMs.
>
> 1. How to effectively use LLMs to help you write your own code.
>
>    Focus on test cases!!!
>
> 1. Handling documents that are "too large" for the LLM via *recursive summarization*.
>
>    The next topic will cover *retrieval augmented generation* (RAG),
>    which is an alternative technique for working with large documents / document collections.
>
> 1. Handling rate limits.
>
> All future assignments will be incorporating all of this material,
> since this is what I consider to be a requirement for a "minimal viable git repo".
>
> Several of you have already submitted the assignment in sakai.
> You will need to update your assignment to include the material we cover today in class.
>
> Assignment "nominally" due this Sunday@midnight.
> If you can't complete it by then:
>
>   1. no points off
>   1. but you're behind, and we should chat about how to catch up
-->

## Stupid Mistakes Programmers Make With LLMs

### Mistake 1: Leaking API keys

<img src=img/apikey.jpg width=300px /> <img src=img/api2.webp width=300px />

Very common support request on the OpenAI forums:
1. <https://community.openai.com/t/key-leaked-unexpectedly-any-possible-reason/280948>
1. <https://community.openai.com/t/my-api-is-getting-leaked-need-advice/280564>
1. <https://community.openai.com/t/api-key-stolen-charged-lost-of-anybody-help-me/390240>
1. <https://community.openai.com/t/someone-used-my-api-key-and-used-up-all-my-limit/774218>

Tools for stealing API keys:
1. <https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/API%20Key%20Leaks>

<!--
To secure API keys for github actions, see: <https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions>
-->

### Stupid Mistake 2: Trusting User Input

<img src=img/prompt.png width=600px />

See the following links:

1. Prompt injection attacks against ChatGPT 3: <https://simonwillison.net/2022/Sep/12/prompt-injection/>

    The post above is part of a series that tracks lots of realworld prompt injection exploits: <https://simonwillison.net/series/prompt-injection/>

    The article on image prompt injection is particularly fun: <https://simonwillison.net/2023/Oct/14/multi-modal-prompt-injection/>.

1. Data exfiltration from Slack AI via indirect prompt injection <https://promptarmor.substack.com/p/data-exfiltration-from-slack-ai-via>
   
   and the corresponding hacker news post <https://news.ycombinator.com/item?id=41302597>

<!--
## Capture the Flag

<img src=img/ctf.png width=300px />

Solve as much as you can of the CTF at <https://invariantlabs.ai/ctf-challenge-24>.
You should be able to solve at least the "playground" level.

> **NOTE:**
> This is a real, currently active, CTF challenge.
> It started in August 5th and runs until September 2nd.

> **NOTE:**
> There is no grade attached to this assignment.

    1. <https://verse.systems/blog/post/2024-03-19-a-ctf-challenge-for-llms-for-code-analysis/>
    1. <https://github.com/dhammon/ai-goat>
-->
