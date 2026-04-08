# Project 3: docchat

**tl;dr**
You will make a python program that lets you chat with documents.
You will be extending the project you started from [lab-more-project-setup](https://github.com/mikeizbicki/lab-more-project-setup).

**learning objectives:**
1. understand how AI agents work under the hood
1. create doctests / other project scaffolding "from scratch"
1. create "long lived" projects
    1. in a future lab, someone else will have to commit code to your project
    1. in the next project, you will extend this project with more features
    1. in your last project, you will use this project to write code for you

**due date:**
1. 14 April
1. Don't put off the coding here until the last minute;
    expect that the coding will take you longer than you think.

    Estimating the time it will take to complete a coding project is a famously hard problem,
    and there are lots of memes about this difficulty:

    <img width=300px src=img/meme1.png />

    <img width=300px src=img/meme2.jpg />

    <img width=300px src=img/meme3.jpg />

    <img width=300px src=img/meme4.png />

**modified late penalties:**
1. it is important that you all get this project working correctly
1. therefore we will use the modified late penalty schedule below

    | days late | standard policy | this project policy |
    | --- | --- | --- |
    | 1 | -1 | -1 |
    | 2 | -2 | -1 |
    | 3 | -4 | -2 |
    | 4 | -8 | -2 |
    | 5 | -16 | -4 |
    | 6 | -32 | -4 |
    | 7 | -64 | -8 |
    | 8 | -128 | -8 |
    | 9 | -256 | -16 |

1. the standard 2-day extension for collaboration still applies.

**grading:**
The project is worth 32 points.
There are also 20 possible points of extra credit,
so it is possible to get 52/32 on this assignment.

## Project Specification

1. Your project must meet all of the specifications in <https://github.com/mikeizbicki/lab-more-project-setup>.

1. Coding tasks.

    1. You must extend the `Chat` class to support the following tools:
        1. `calculate`: this tool should be copied from the groq tutorial on local tool use: <https://console.groq.com/docs/tool-use/local-tool-calling>.

        1. `ls`: this tool behaves just like the `ls` program in the shell; it optionally takes 1 argument
            1. if no arguments are provided, then the program lists all of the files in the current folder
            2. if one argument is provided, then the program lists all of the files in that folder
            3. hints:
                1. use the `glob.glob` function to list the files
                2. recall that `glob.glob` is non-deterministic, and so the files may be returned in an arbitrary order; to make test cases reliable, you should sort the files asciibetically before returning them

        1. `cat`: this tool opens a file and outputs the contents
            1. the tool takes a single argument that is the file to read
            1. hints:
                1. you must catch any exceptions that your code raises; common exceptions include `FileNotFoundError` (if the file doesn't exist) and `UnicodeDecodeError` (if the file exists but is not a text file)
                1. for windows machines, you may have to work with files encoded in both UTF-16 and UTF-8 (depending on your computer); for all other machines, UTF-8 only should be fine

        1. `grep`: this tool takes two parameters; the first is a regex, and the second is a path (optionally with globs)
            1. the tool should:
                1. load every file that matches the glob
                1. then it should loop through every line in the file and see if it matches the regex
                1. if it does match the regex, then that line should be added to the output
                1. if no lines match the regex, then there should be no output
            1. like `cat`, `grep` must not allow absolute paths or directory traversal attacks
            1. hints:
                1. recall that `re.search` can be used to search through a string to see if it matches a regex

    1. All tools should be able to be called in either of the following ways:
        1. Automatically: This is the standard way of tool calling discussed in the groq tutorial: <https://console.groq.com/docs/tool-use/local-tool-calling>.
        1. Manually:
            1. Inside the repl, the user should be able to type `/command param1 param2` in order to run the specified command manually.

                For example:
                ```
                chat> /ls .github
                workflows
                chat> what files are in the .github folder?
                There is only a `workflows` folder in the `.github` folder.
                ```
                In the example chat above, the user manually ran the `ls` tool before asking a question about a folder.
                Therefore, the output of `ls` is already in the model's "context window" and so the model does not need to do a tool use call to answer the question.

                Note that the `/ls .github` command did not actually invoke the LLM at all, but directly ran the command.
                This "slash command" syntax is common in AI agents in order to get faster feedback (there is no need to invoke the API call, which is slow, so the output returns instantly) and to get more stable results (sometimes LLMs may not use the correct tools to perform a certain task, and so it can be useful to force them to perform certain tasks this way).

            1. Modify the `repl` function so that it checks to see if the first character of a line begins with `/`

    1. **WARNING:**

        Each of the tools above allows the LLM to read contents from your computer.
        We only want these tools to be able to read contents from the current folder that your `chat` tool was run from.
        In particular, none of your tools should allow:
        1. reading absolute paths (paths that start with a `/`), or
        1. [directory traversal attacks](https://en.wikipedia.org/wiki/Directory_traversal_attack) (i.e. the tool should not allow passing in the filename `..` anywhere in the filepath, which could allow the LLM to read documents outside the directory in which it is being run).

        The easiest way to make your tools safe is to create a common helper function `is_path_safe`.
        1. This function will take a single argument as input, and check if it is an absolute path or if it contains `..`.
        1. All of your tools can then call this function, and only procede if it returns `True`.

1. Coding Conventions
    1. Every function must have a docstring
        1. The docstring must contain a brief 1 sentence English language description of what the function does.
        1. The docstring must contain doctests that demonstrate what the function does.
        1. It is okay for class methods to not have their own doctests (these can be in the class docstring instead).
    1. Every class must have a docstring.
        1. The docstring must contain a brief 2-3 sentence English language description of what the class does.
        1. The docstring must contain doctests that demonstrate what the class does.
    1. Every file must have a docstring that contains a brief 1-2 sentence description of the file. Not doctests are required.
    1. You must have a file `chat.py` that contains the "main code" for your program.
    1. Every tool must be in its own file inside of a `tools` subfolder.
        For example, the `ls` tools should have a file `tools/ls` that contains the code/json necessary for that tool.
    1. You must have >90% code coverage from your doctests.
        1. Every tool should have 100% code coverage.
        1. Only IO-performing functions in the main `chat.py` file are allowed to have <100% coverage.
    1. You should avoid "cheesy" doctests that do not meaningfully test the function.

        For example:
        ```
        def do_fancy_string_processing(input_str):
            '''
            This function does a lot of hard, fancy string processing.

            >>> assert do_fancy_string_processing('this is s **super** __hard__ function to implement')
            '''
        ```
        The doctest above uses the `assert` command to avoid printing the output of the `do_fancy_string_processing`.
        This doctests only demonstrates that the function does not error,
        but it does not demonstrate what the function actually does.
        Why is this bad?
        1. The doctest does not help me as a user understand when to use this function.
        1. The function could totally change behavior and my test suite won't alert me to this change.

1. Integration tests

    1. Your repo must include a folder `test_projects`
    1. In the `test_projects` folder, you should have "submodules" for all of the previous class projects
        1. The three previous projects are: creating your own webpage, markdown compiler, and ebay scraper
        1. Recall that a submodule is a "git repo inside another git repo".  They should be added using the command `git submodule add <url>`. YOU SHOULD NEVER CLONE A REPO INSIDE OF ANOTHER REPO!

1. Github repo organization.

    > **Hint:**
    > I recommend that you do not make references to the fact that this is a school project in your README.
    > This will make the project look "more impressive" to future employers who might see it.

    1. The repo must have no non-necessary files (e.g. `.DS_Store`, `__pycache__`).
    1. The repo mush have no `.env` file (and no hard-coded credentials anywhere else) uploaded.
    1. The repo must have a valid `requirements.txt` file that contains all of the required dependencies, and any other files required for building the project with `pip`.
    1. The repo must have the following github actions:
        1. doctests
        1. integration tests
        1. flake8

            > **NOTE:**
            > Your lab had doctests and integration tests github actions, but not flake8.
            > You should copy the github actions for flake8 from one of the previous assignments.

    1. The repo must have a `README.md` file that has:
        1. a good title (inside a `#` element)
        1. a short 1-2 sentence description of your program
        1. the following badges:
            1. one for each of your github actions (3 in total)
            1. one for pypi
            1. one for code coverage
        1. an animated gif example of your program running

            > **NOTE:**
            > Your gif should not include all of your VSCode interface,
            > but only your terminal session.
            > You can find good examples of what this looks like at the following links:
            >
            > 1. <https://github.com/faressoft/terminalizer>
            > 2. <https://github.com/ofek/terminal-demo?tab=readme-ov-file#usage>
            > 3. <https://github.com/charmbracelet/vhs>
            >
            > We will not cover in class how to do this because it will depend on your specific computer settings.
            > If you don't already have a screen recording program that you like, you can find some links and instructions at <https://dev.to/kelli/demo-your-app-in-your-github-readme-with-an-animated-gif-2o3c>.

        1. a text-based usage example inside of a code block, one for each of the git submodules

            1. some examples of such code blocks are:
                ```
                $ cd markdown_compiler
                $ chat
                chat> does this project use regular expressions?
                No. I grepped all of the python files for any uses of the `re` library and did not find any.
                ```
                or
                ```
                $ cd ebay_scraper
                $ chat
                chat> tell me about this project
                The README says this project is designed to scrape product information off of ebay.
                chat> is this legal?
                Yes. It is generally legal to scrape webpages, but ebay offers an API that would be more efficient to use.
                ```
            1. these examples should be inside of their own markdown section
            1. you must have a 1 sentence explanation for each example that explains why it is good

**Extra credit:**

> **NOTE:**
> There is no reasonable way to write doctests for many of these tasks,
> so completing this task will likely reduce your code coverage.
> You should be okay as long as you maintain 100% code coverage on your tool functions.

1. (1pts)
    Allow your program to take a command line argument that is a message to pass to the llm.

    For example:
    ```
    $ chat 'what files are in the .github folder?'
    The only file in this folder is the workflows subfolder
    $ chat 'what is this project about?'
    Looking at the README.md file, I see this project is an AI agent for chatting with documents.
    ```

1. (1pts)
    Allow your program to support a `--debug` flag that prints out tool use calls.

    For example:
    ```
    $ chat
    chat> what files are in the .github folder?
    The only file in this folder is the workflows subfolder
    chat> ^C
    $ chat --debug
    chat> what files are in the .github folder?
    [tool] /ls .github
    The only file in this folder is the workflows subfolder
    ```
    To get this extra credit, you must have both doctests and an integration test demonstrating this behavior works.

1. (2pts)
    Allow your program to support a `--provider` flag that lets you specify which provider to use.

    You should support the following providers:
    1. `openai`: use the latest gpt model
    1. `anthropic`: use the latest claude opus 4.6 model
    1. `google`: use the latest gemini model
    1. `groq` (default): use whichever groq model you like the best

    > **NOTE:**
    > You will need an <https://openrouter.ai> API key to complete this task.
    > All of your queries should cost less than a penny, so spending $10 on credits should be more than enough.

1. (2pts)
    Add a new tool `compact`.

    This tool will call the LLM to summarize the current chat session (i.e. everything in `chat.messages` into just 1-5 lines of text.
    Then it will replace the contents of the `chat.messages` list with a single entry that contains the summary.

    This is useful for reducing the number of tokens in the current chat.
    Reducing the number of tokens is useful for:
    1. getting quicker responses from the LLMs
    1. improving LLM accuracy (they can often get distracted by lots of unnecessary previous chat messages)
    1. preventing API rate limits (remember that you have only a certain number of tokens per day you are allowed to use, and reducing the number of tokens in the chat prevents you from hitting those limits)
    1. reducing the cost of running the chat (you are using a free API, but normally we pay per token)

    > **NOTE:**
    > The compact command will need to create its own instance of the `Chat` class.
    > This is technically called a "subagent".

1. (2pts)
    Have your chat program support tab completion in `/` commands.

    Pressing tab while in the command portion should complete the command, and pressing tab in a parameter section should complete based on filenames.

    For example:
    1. if someone types `/` and then presses tab, they will get a list of supported tools
    1. if someone types `/l` and then presses tab, then `/ls` will be automatically completed for them
    1. if someone types `/ls .g` and then presses tab, then `/ls .git` will be automatically completed for them (recall that there should be a `.git` and `.github` path in the project folder)
    1. if someone types `/ls .gith` and then presses tab, then `/ls .github` will be automatically completed for them

    For examples of how to complete this task, see:
    1. <https://gist.github.com/christoomey/801888>
    1. <https://docs.python.org/3/library/readline.html>

1. (2pts)
    Have your system support chatting with images in addition to text documents.

    Groq has a tutorial at <https://console.groq.com/docs/vision#how-to-pass-locally-saved-images-as-input> for passing images into the LLM.

    You will need to add a new tool `load_image` that behaves similar to `cat` and adds an image to the messages list.
    The `load_image` tool, however, is a bit more complicated because it cannot just "return image" because tool output needs to be in text form.
    Instead, your tool will need to directly modify the `Chat.messages` list somehow.

1. (2pts)
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
    > If you choose this extra credit and add a video to the README, you do not need to also add an animated gif.

1. (2pts - 4pts)
    Have your program use speech to text (STT) to allow the user to ask questions verbally.

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

    > **NOTE:**
    > If you use trigger word detection instead of a keypress, you will get an additional +2 points of extra credit.

1. (4pts) Deploy your chat program to iphone/android.

    You can find instructions on deploying python code to these platforms at:
    1. <https://docs.python.org/3/using/android.html>
    1. <https://docs.python.org/3/using/ios.html>

    This requires a lot of mucking around in programming languages that we have not covered in class.

## Submission

Submit a link to your github repo in sakai.

Additionally: You should submit a 1-2 sentence explanation of what you believe your grade should be.  In particular:
1. If you completed any extra credit, say so.
1. If there are portions of your assignment that do not work, I may be more lenient in grading if you say so.
