# Retrieval Augmented Generation (RAG)

<img src=img/debug.png width=300px />

## Announcements

**Tuesday 15 Apr:**

1. no quiz this week :)
1. docsum repos:
    1. lots of minor problems (resubmit for full credit)
    1. proper formatting of commands in README
    1. specify dependencies in `requirements.txt`
    1. keep your project organized with folders
    1. do not include "bad files" in the repo
        1. examples: `__pycache__`, `.DS_Store`

        <img src=img/linus.png width=300px />

**Thursday 17 Apr:**

1. We will do more live coding in lab tomorrow in preparation for your project.

1. Project will be due Sunday 27 April.

1. We will start the next (and last) material next week.

<br/>

<img src=img/tea.png width=400px />

## Lecture Notes

**Review:**

1. Protect your API keys
    1. API keys go in the `.env` file
    1. add `.env` to `.gitignore`
1. Using LLMs on untrusted text is dangerous
1. Write doctests for your non-LLM code
1. Use *recursive summarization* to summarize large documents

**Overview of RAG**

RAG will solve two problems for us:

1. LLMs cannot handle large documents/conversations.

    RAG works on tasks other than summarization.
    
    We will build a "chatbot" / "question answering" application.

1. LLMs cannot learn new material after their training date.

    > **Example:**
    > Why did Trump place tariffs on China in 2025?

    RAG lets us include this new material in "the context".

    Provides similar benefits to
    1. retraining a new model, and
    1. fine tuning an existing model
    but it is much easier/cheaper to do.

Example use cases:
1. Search the internet <https://www.perplexity.ai/>
1. Chat with documentation <https://docs-chat.groqcloud.com/>
1. *(Your next homework)*  Ask questions about the contents of a document

### Part 0: Building a Command Line Chatbot

New python techniques:
1. `input` function
1. `readline` module

### Part 1: Prompt Engineering

<img height=240px src=img/prompt.webp /> <img height=240px src=img/nice.png />

There are 4 "roles" that can be passed to the llm:
1. system
1. user
1. assistant
1. tool

Guides for prompt engineering:
1. OpenAI: <https://platform.openai.com/docs/guides/prompt-engineering>
1. Anthropic: <https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview>

Anthropic publishes their system prompts for state of the art (SOTA) models:
1. Official announcements: <https://docs.anthropic.com/en/release-notes/system-prompts>
1. Reddit discussion: <https://www.reddit.com/r/LocalLLaMA/comments/1f2kchq/anthropic_now_publishes_their_system_prompts/>

One of the reasons Anthropic decided to do this is that it is "trivial" to extract these system prompts via prompt injection.
1. Anthropic: <https://www.reddit.com/r/LocalLLaMA/comments/1ecd0jo/claude_prompt_leaked/lf03zz0/?context=3&share_id=Ntkvzjoz9gwFzWMWCMSCH>
1. OpenAI: <https://x.com/dylan522p/status/1755086111397863777?t=bpvmx9OcT-OcxJdFwy64Dg>

The "model card" for a model provides:
1. Recommended system/user prompts
1. Training cutoff date information
1. See LLama 4 model card: <https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md>

### Part 2: RAG

<img width=400px src=img/rag.jpg />

The procedure looks like:
1. User inputs their question.

    > Who are the presidential nominees?

1. **Retrieve** articles related to the question from a database.
    ```
    ARTICLE0_URL: https://abcnews.go.com/Politics/wireStory/iowa-judge-rules-libertarian-candidates-keeping-names-off-113486437
    ARTICLE0_TITLE: Judge keeps Libertarian candidates off ballot for Congress - ABC News
    ARTICLE0_SUMMARY: On September 7, 2024, a judge in Iowa ruled that three Libertarian candidates seeking U.S. House seats will not appear on the ballot this November, upholding a state election panel's decision. The candidates, Nicholas Gluba, Marco Battaglia, and Charles Aldrich, were removed from the ballot due to a technicality related to the Libertarian Party's nomination process at its party convention, which was held on the same day as precinct caucuses. The State Objection Panel, composed of one Democratic and two Republican elected officials, ruled 2-1 that the Libertarians failed to follow state law, which requires the term of convention delegates to begin the day after the caucuses. The ruling was supported by Republican Party officials and conservative attorney Alan Ostergren, who argued that the Libertarian Party's failure to comply with state law is mandatory and requires strict compliance. The judge's decision means that the Libertarian nominees will not be included on the ballot for now, and an appeal to the Iowa Supreme Court is still possible, which could further delay the certification and printing of ballots.

    ARTICLE1_URL: https://apnews.com/article/election-2024-libertarian-candidates-iowa-ca070a5f9511ec39242df9d8c80fcdab
    ARTICLE1_TITLE: Iowa judge rules against Libertarian candidates, keeping their names off the ballot for Congress | AP News
    ARTICLE1_SUMMARY: In a ruling upheld by a Polk County District Judge, three Libertarian candidates for U.S. House seats in Iowa will not appear on the ballot this November due to a technicality. The State Objection Panel, composed of Democratic and Republican elected officials, ruled that the Libertarian Party failed to follow state law when nominating the candidates, citing a lack of compliance with state law regarding convention delegate terms. The judge agreed with the panel's 2-1 decision, finding that the state law is "mandatory in nature and requires strict compliance." The ruling means that the names of nominees Nicholas Gluba, Marco Battaglia, and Charles Aldrich will not be included on the ballot, at least until an appeal to the Iowa Supreme Court is heard. The case highlights the challenges faced by independent and third-party candidates, who often have little chance of winning but can potentially impact the outcome of an election.

    ARTICLE2_URL: https://ground.news/article/george-bush-wont-formally-endorse-candidate-in-2024-election-reports
    ARTICLE2_TITLE: Ground News - George Bush won't formally endorse candidate in 2024 election: Reports
    ARTICLE2_SUMMARY: Former President George W. Bush has decided not to endorse any candidate in the 2024 presidential election, according to reports from multiple outlets. This decision is notable because Bush has endorsed candidates in past elections, including Mitt Romney in 2012 and John McCain in 2008. His office stated that Bush has "retired from presidential politics years ago" and declined to comment on how he or his wife Laura Bush would vote in the upcoming election. This move comes as some party members are publicly endorsing their preferred candidates, including former Vice President Dick Cheney, who announced his support for the Republican nominee just a day prior to Bush's decision.

    ARTICLE3_URL: https://www.aljazeera.com/news/2024/9/7/ahead-of-the-us-presidential-debate-how-are-harris-and-trump-preparing
    ARTICLE3_TITLE: Ahead of the US presidential debate, how are Harris and Trump preparing? | US Election 2024 News | Al Jazeera
    ARTICLE3_SUMMARY: The upcoming presidential debate between Vice President Kamala Harris and former President Donald Trump is poised to be a high-stakes encounter, with both candidates aiming to gain an edge in the neck-and-neck election. Harris, who launched her campaign just seven weeks ago, is seeking to establish herself as a strong contender, while Trump is looking to expand his appeal beyond his base. The debate will mark the first time the two candidates have faced off in person, and experts warn that a single mistake or gaffe can cost a candidate the election. Harris's team plans to use the debate to showcase her prosecutorial style and address Trump's attacks, while Trump is expected to rely on his unpredictable debate performances and "spidery sixth sense" to capitalize on camera-ready moments. The debate is also likely to highlight the differences in preparation methods between the two candidates, with Trump opting for freewheeling discussions with staffers and Harris practicing with mock debates. Additionally, the debate will put a spotlight on Trump's potential to continue using sexist attacks against Harris, who is facing societal preconceptions about women and people of color. Ultimately, the outcome of the debate will depend on how each candidate navigates these challenges and presents themselves to the American public.
    ```

1. **Augment** the user's prompt with the articles.

    System:
    ```
    You are a news analyst.
    ```

    User:
    ```
    You will be given several articles and a question.
    Answer the question based on the articles.

    ARTICLE0: ...
    ARTICLE1: ...
    ARTICLE2: ...
    ARTICLE3: ...

    QUESTION:
    Who are the presidential nominees?
    ```

1. **Generate** a response based on the new prompt.

#### The Hard Part is Retrieval

**Problem:** How do we decide which documents to put in the context?

**Answer:**

1. No one knows!!!

1. Lots of methods have been proposed.

1. They all use lots of math.

    <img src=img/math.webp width=400px />

1. ChatGPT can automate "mundane" coding work.

    But it can't automate the mathematical understanding.

    <img src=img/finally.jpeg width=300px />

1. CS courses at CMC:

    | course | %programming | %math |
    | --- | --- | --- |
    | CSCI040 (~~computing for web~~ intro to hacking) | 100% programming | 0% math |
    | | | |
    | CSCI036 (foundations of data science) | 100% programming | 0% math |
    | CSCI046 (data structures) | 80% programming | 20% math |
    | CSCI143 (big data) | 80% programming | 20% math |
    | CSCI145 (data mining) | 20% programming | 80% math | 
    | CSCI148 (graph algorithms) | 0% programming | 100% math | 
    | MATH389 (combinatorial optimization) | 0% programming | 100% math |

<!--
The vast majority of RAG tutorials encourage you to use a "vector db" for storing documents.

<img height=240px src=img/vector1.webp /> <img height=240px src=img/vector2.jpeg />

Pinecone is the "coolest"
1. Groq has a tutorial on their website for integrating with pinecone: <https://groq.com/retrieval-augmented-generation-with-groq-api/>.
1. I don't like it
    1. It's not open source
    1. It's not even free-as-in-beer: <https://www.pinecone.io/pricing/>

We will use an ordinary SQL database.
1. Easier to setup.
1. Can do everything that a vector database can do and more!

Normally, I prefer to [use postgres for everything](https://news.ycombinator.com/item?id=40418983).

<img width=400px src=img/postgres.jpg />

The main downside of postgres is that setup is "hard".

1. The details are covered in CSCI143 big data:
    1. docker / docker-compose,
    1. lots of shell tricks,
    1. complicates your testing infrastructure,
1. For a good SWE, this should all be trivial.

But sqlite3 is also a pretty good choice,
especially for 1-off or small projects.

1. We'll use sqlite3.
1. Lots of good SWEs use sqlite3 for everything.

   <img width=300px src=img/sqlite.jpg />

   <img width=400px src=img/sql.jpg />


> **ASIDE:**
> 
> The top 3 complaints I hear from industry folk about recent grads are:
> 1. juniors don't use version control
> 1. juniors don't write tests
> 1. juniors don't understand SQL
> 
>    <img width=400px src=img/relational.jpg />

#### Document Search

We will use sqlite3's built-in FTS5 system <https://www.sqlite.org/fts5.html>.
1. uses [BM25](https://www.sqlite.org/fts5.html#the_bm25_function) ranking function
1. simple
1. fast
1. easy to understand what it does
1. good enough results

SOTA systems (e.g. google/bing/kagi/yandex/baidu/etc) all use vector-based methods.
1. must select a model to generate the vectors
1. much more complicated to setup logistically
1. much harder to interpret/debug the results
1. very little improvement due to the vector results

The best way to improve results is to use non-text features:
1. pagerank
1. publication date

Both postgres and sqlite3 can perform vector searches.
1. postgres: <https://github.com/pgvector/pgvector>
1. sqlite3: <https://github.com/asg017/sqlite-vec>
-->

<!--
#### What to Actually Do

1. Create a new github repo based off of <https://github.com/mikeizbicki/ragnews>

    Don't fork my repo.
    It'll look "more impressive" if it is you're own repo and not a fork.

1. Fix the three broken functions with FIXME annotations.

1. Create a "reasonable" README file.

    1. Github actions badge.
    1. Pass test cases.
    1. Explanation of what the repo does.
    1. Example usage.

1. Submit the completed project link to sakai.
-->
