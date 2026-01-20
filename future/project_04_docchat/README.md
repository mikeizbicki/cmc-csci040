# Project 4: docchat

**tl;dr**
You will make a python program that lets you chat with a document.

**due date:**
Sunday 27 April

## Rubric

The project is worth 32 points.
There are 44 points available depending on which tasks you choose to complete.
So it is possible to earn up to 12 points of extra credit if you complete all tasks.

1. (8pts) Github repo organization.

    1. The repo must have no non-necessary files (e.g. `.DS_Store`, `__pycache__`).
    1. The repo mush have no `.env` file (and no hard-coded credentials anywhere else) uploaded.
    1. The repo must have a valid `requirements.txt` file that contains all of the required libraries.
    1. The repo must have continuous integration setup.

        > **NOTE:**
        > Continuous integration means that test cases are automatically run for you everytime you push your code to github.
        > 
        > Setup continuous integration by:
        > 1. Creating a file `.github/workflows/tests.yml` in your project folder.
        > 
        >    The file contents should match my example at <https://github.com/mikeizbicki/docchat/blob/master/.github/workflows/tests.yml>.
        > 
        > 1. Adding a test cases "badge" to your README file.
        >
        >    You can copy the code from my example README at <https://github.com/mikeizbicki/docchat/blob/master/README.md>.
        >    Ensure that you cange the link location to your repo instead of mine!
        > 
        > 1. If the test cases badge for your repo is gray:
        >    You need to enable github actions.
        >    Click the "actions" tab on your repo,
        >    Then click "enable".
        >
        > 1. The test cases for `llm` will fail in github actions because it does not have access to your API key.
        >    Add your API key in the menu item `Settings > secrets and variabls > actions`.
        >    Click `New repository secret`.
        >    The name should be `GROQ_API_KEY` and value your API key from the `.env` file (without the `GROQ_API_KEY=` portion).

    1. The repo must have a `README.md` file that has:
        1. a good title (inside a `#` element)
        1. a short 1-2 sentence description of your program
        1. a test-cases badge that demonstrates that your code passes all test cases
        1. an animated gif example of your program running

            > **NOTE:**
            > Your gif/video should not include all of your VSCode interface,
            > but only your terminal session.
            > You can find good examples of what this looks like at the following links:
            >
            > 1. <https://github.com/faressoft/terminalizer>
            > 2. <https://github.com/ofek/terminal-demo?tab=readme-ov-file#usage>
            > 3. <https://github.com/charmbracelet/vhs>
            > 
            > We will not cover in class how to do this because it will depend on your specific computer settings.
            > If you don't already have a screen recording program that you like, you can find some links and instructions at <https://dev.to/kelli/demo-your-app-in-your-github-readme-with-an-animated-gif-2o3c>.

        1. a text-based usage example inside of a code block
           
            you must have an example where:
            1. your program answers the question well
            1. your program answers the question poorly

        <br/>
        > **Hint:**
        > I recommend that you do not make references to the fact that this is a school project in your README.
        > This will make the project look "more impressive" to future employers who might see it.

1. (16pts) Your `docchat.py` file must have the following functions.
    They are worth 4pts each.

    Every function must have a good docstring and good doctests in order to get full credit on the function.

    If you include any other functions, then they must also have appropriate docstrings and doctests or you will lose (at least) 2 points / function.

    1. ```
        def load_text(filepath_or_url)
        ```

        This function should load text from the input variable.
        It must work whether a filepath or a url has been input.
        It must work with:
        1. ordinary text documents
        1. html files
        1. pdf files

        You do not need to be able to support images like you did in the lab.

    1. ```
        def chunk_text_by_words(text, max_words=100, overlap=50)
        ```

        This function should split the input text document into chunks of length `max_words`.
        Each chunk should overlap previous chunks by the `overlap` amount.

    1. ```
        def score_chunk(chunk, query)
        ```

        This function will associate a "similarity score" between 0 and 1 to the `chunk` and `query` variables.
        Higher scores should signify "more similar" and lower scores should signify "less similar".

    1. ```
        def find_relevant_chunks(text, query, num_chunks=5)
        ```

        This function will:
        1. split the document into chunks
        2. compute the score for each of these chunks
        3. return the `num_chunks` chunks that have the largest score
        
1. (8pts) Your `docchat.py` should take as input from the command line a file path or url and allow the user to chat.
    In the infinite loop, you will need to:
    1. appropriately use the `system`, `user`, and `assistant` portions of the `message` parameter
    1. construct a good prompt that uses the `find_relevant_chunks` function to include important portions of the input document

    The responses from your chatbot must be reasonable and answer the questions you ask.
    You may need to experiment with different prompting styles to get good results.

    > **HINT:**
    > A common way to improve results is to also provide a summary of the document in addition to the results of the retrieval step.

**Extra credit:**

1. (1-1000 pts)
    Experiment with a new method for improving the quality of the RAG output.
    The amount of extra credit will depend on the creativity and effectiveness of your experiment.

    Some simple ideas are:
    1. Ask an LLM directly to do the scoring for you.
    1. Ask an LLM to come up with useful synonyms to the input query,
        then use the existing `score_chunks` function.

    I expect a typical attempt at this extra credit to result in +2 points.
    But it is an open problem how to do this well,
    and it's possible to make a legitimate discovery even as a very junior programmer these days.

1. (2pts)
    Have your program support asking questions in English when the document is non-english.

    An easy way to do this is to ask the LLM to translate the query from English to the non-english language,
    then use the translated query in your function calls.

    You must still be able to support English,
    and the program will need to automatically determine what language the document is written in.
    The [langid library](https://pypi.org/project/py3langid/) is a standard and popular tool for determining the language of a string.

1. (2pts)
    Have your system support chatting with images in addition to text documents.

1. (4pts) 
    Have your program use text-to-speech (TTS) to read its answers outloud.

    You can find instructions on using groq's TTS API at:

    <https://console.groq.com/docs/text-to-speech>

    Those instructions only display how to download the text as a WAV file.
    You will then have to figure out how to play the WAV file.
    There are various libraries to choose from,
    and you can find an overview at <https://realpython.com/playing-and-recording-sound-python/>.

    > **NOTE:**
    > If you complete this task,
    > then you must include a video in your README demonstrating the output.

1. (4pts)
    Have your program use speech to text (STT) to allow the user to ask questions verbally.
    (STT is harder than TTS.)

    You can find instructions on using groq's STT API at:

    <https://console.groq.com/docs/speech-to-text>

    Those instructions assume that the audio is stored in a file.
    You will have to find separate instructions for recording audio.
    (The realpython link above has examples.)

    The hard part about this extra credit is figuring out when to begin and end the sound recording process.
    The technique of waiting for a key phrase like "Okay Google" or "Hey Siri" is called *trigger word detection* and relatively hard to get working well.
    A simpler technique is to require the user to press a key (like spacebar) to begin recording;
    when the key is released, then the file is saved and sent to the llm.

    > **NOTE:**
    > If you complete this task,
    > then you must include a video in your README demonstrating the output.

## Submission

Submit a link to your github repo in sakai.

Additionally: You should submit a 1-2 sentence explanation of what you believe your grade should be.  In particular:
1. If you completed any extra credit, say so.
1. If there are portions of your assignment that do not work, I may be more lenient in grading if you say so.
