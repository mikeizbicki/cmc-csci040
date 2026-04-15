# Project 4: Agents

**tl;dr**
Your docchat project has a variety of tools that *read* data about your computer.
This project adds tools that *write*.
These tools will turn your docchat program into a full-fledged autonomous AI agent.

**learning objectives:**
1. extend smaller projects into larger projects
1. understand how AI agents work

    <img width=300px src=img/ai-ai-agents.jpg />

**due date:**
1. 21 April
1. no modified late penalty
1. the standard 2-day extension for collaboration still applies.

**grading:**
1. The project is worth 16 points.
1. You may still also complete any of the previous extra credits.
    (But any already completed extra credits will not be double counted.)
1. There are also new extra credits.

## Project Specification

1. Your project must meet all of the specifications from project 03 docchat.
    1. If you missed any points on that project, you must fix the issue or you will miss more points again on this project.

1. You must create a new branch in your project and do all of your work in this branch.
    You may not touch the `main`/`master` branch that you submitted for the docchat assignment.

1. Coding tasks.

    1. When your program starts:
        1. You should check for a `.git` folder in the current directory.
            If it is not present, then the program should output an error
            and stop.
        1. You should check for a `AGENTS.md` folder in the current directory.
            If present, you should load it into the conversation using your
            `cat` tool.

            > **NOTE:**
            > `AGENTS.md` is a standard file that all AI agents load when
            > working with a repo.
            > It is like a "README file for AI agents",
            > and describes project-specific instructions that the agent
            > should perform.
            > You can find more details and examples at <https://agents.md/>.

    1. You must add the following tools:
        1. `doctests`
            1. It should take a single argument: `path`
            1. It should run the doctests (with the `--verbose` flag) and return the output

                > **NOTE:**
                > It is helpful for LLMs to have explicit confirmation
                > that test cases are passing.
                > That is why we use the `--verbose` option here.

                > **NOTE:**
                > We have not explicitly covered how to run doctests from
                > within python.
                > There are many ways to do this,
                > and any way you choose is fine.

        1. `write_file`
            1. It should take three arguments: `path`, `contents`, and `commit_message`
            1. It should open `path` and then write `contents` to path
            1. The output file must be utf8 encoded
            1. Then it should use the `git` library in python to run the python equivalent of:
                ```
                $ git add <path>
                $ git commit -m "[docchat] <commit_message>"
                ```

                > **NOTE:**
                > It is standard practice for AI agents to have them
                > use git to commit whatever changes they make to the harddrive.
                > This way, when an agent "goes skynet" on you,
                > it is easy to "travel back in time" to undo their work.
                > Lots of AI researchers these days use terminator
                > memes/analogies when talking about AI.
                >
                > <img width=300px src=img/terminator.jpeg />
            1. If the file is a python file, then you should run the
                doctest tool on the python file and return the output.

        1. `write_files`
            1. It should take two arguments: `files` and `commit_message`
            1. `files` is a list of dictionaries, where each dictionary contains a `path` and `contents` key
                1. For each of these dictionaries, you should write the file the same way you do in the `write_file` function
            1. After writing all files, add/commit them.

            > **NOTE:**
            > I recommend only implementing `write_files` with "real" code,
            > and then make the `write_file` function a simple wrapper
            > around `write_files`.
            > The generic principle here is that:
            > 1. less code is better than more code
            >   1. easier to write
            >   1. easier to write tests
            >   1. easier to make changes in the future
            > 1. DRY: Don't Repeat Yourself
            >
            > <img width=300px src=img/dry.jpg />

            > **NOTE:**
            > Why even both with having a `write_file` tool if it is just
            > a thin wrapper around the `write_files` tool?
            > The answer is because LLMs (and humans) generally understand
            > how to use the more specific tools better than the more
            > generic ones.
            > And even just the presence of the more specific tool
            > can help the model understand how to use the more generic
            > one better if it is actually necessary to use the more generic
            > tool.

        1. `rm`
            1. It should take a single argument: `path`
            1. It should delete the path using the `os.remove` function in python
            1. It should support multiple files at once using globs
            1. It should create a commit with the file removed
                1. The commit message should be `[docchat] rm <path>`

    > **WARNING:**
    > All of the tools above must validate their paths before running.
    > Like your previous tools, they should not run on absolute paths
    > or paths containing `..`.
    >
    > If this part of your previous assignment was broken,
    > the worst that could happen is you would "leak" data to the AI.
    > But now the AI has write permissions.
    > If this part of your assignment is broken,
    > then a rogue AI could choose to delete everything on your computer.

1. Github repo organization.
    1. Add examples to your README showing the agent in action.
        The examples should demonstrate that your agent has created/modified/deleted files and created git commits.
        You will need to use shell commands like (`ls`, `cat`, and `git`) and proper prompt formatting.

        One possible example is:

        The session below demonstrates that `docchat` can create files when asked
        and these files are automatically added to the git repo.
        ```
        $ ls -a
        .git  AGENTS.md  README.md
        $ git log --oneline
        c21103f (HEAD -> master) init commit
        $ docchat
        chat> Create python code that implements the project in README.md
        Created the file hello_world.py
        chat> ^C
        $ ls -a
        .git  AGENTS.md  README.md  hello_world.py
        $ git log --oneline
        3cfb0a6 (HEAD -> master) create basic hello world python project
        c21103f init commit
        ```

**Extra credit:**

1. (1pt) Create a `pip_install` tool.

    The tool should take a single parameter `library_name`,
    and run the `pip3 install <library_name>` command.

    > **WARNING:**
    > Recall that pypi libraries can contain arbitrary code in them.
    > That means that any agent with this ability can choose
    > (on purpose or on accident) to destroy your computer.

1. (2pts) Implement the [Ralph Wiggum loop](https://ghuntley.com/loop/).

    Whenever your doctests fail,
    you should force the AI agent to do another round of tool usage.
    You should only leave the loop after the doctests successfully pass.

    You may choose to have the loop always enabled or to make it something that can be turned on/off.

1. (4pts) Get your AI agent to autonomously complete the markdown compiler assignment.

    To claim this extra credit, you will need to include in your README file a link to a branch of your markdown compiler assignment that has only commits from your AI agent inside of it.
    The easiest way to do this is to create a new repo and not try to reuse your existing repo.

    > **HINT:**
    > The llama models and the groq API are not great at this task
    > (because the llama models are old and the free tier groq API has
    > pretty severe token limits).
    > It is much easier to complete this task using a *state of the art* (SOTA)
    > model like OpenAI's latest GPT model or Anthropic's latest opus model.
    > I recommend getting an <https://openrouter.ai> API key so that
    > you can experiment with different models.
    > Actually completing this task with the latest, most expensive model
    > should only take less than $0.10,
    > but I recommend putting about $10 in credits on the account so you
    > can play around with the models a bit.

1. (4pts) Allow your models to "update" files instead of only "overwriting" them.

    You will have to update the `write_file` / `write_files` tools so that
    the `contents` parameter is optional and another `diff` parameter
    is provided instead.
    (A diff is a standard format for describing the changes in files.)
    Applying a diff to generate an updated file is called *patching*
    the file.

    Unfortunately, even SOTA LLMs are bad at generating correct diffs.
    This is mostly because a diff requires line numbers,
    and LLMs are bad at "counting" which line a piece of code is on.
    (And we can more-or-less prove that "counting" will always be hard
    for LLMs.)
    The most immediate consequence of this limitation is that you won't
    be able to use standard diff/patch tools to apply the updates.

    There are many work arounds,
    and you are welcome to use whatever technique you can get to work.
    I recommend using [wiggle](https://github.com/neilbrown/wiggle),
    which is a nice tool for applying these "broken diffs" generated by LLMs.

    > **QUESTION:**
    > Why care about file updates instead of rewrites?
    >
    > **ANSWER:**
    > For large files:
    > 1. Rewriting the whole file wastes a lot of tokens,
    >    which makes using the agent more expensive.
    > 1. LLMs often make typos (like forgetting a to match `(` and `)`).
    >    These small typos will make code "look correct" but be have
    >    very wrong behavior.

## Submission

Submit a link to *the new branch of your github repo* in canvas.

Additionally: You should submit a 1-2 sentence explanation of what you believe your grade should be.  In particular:
1. If you completed any extra credit, say so.
1. If there are portions of your assignment that do not work, I may be more lenient in grading if you say so.
