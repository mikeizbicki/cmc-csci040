# SQL

<img width=500px src=img/dilbert5.jpg />

So far we've seen four types of languages:

1. **Procedural**: Python, Shell (sometimes called Bash/Zsh)

    Tell the computer step by step exactly HOW to accomplish ANY TASK.
    The instructions are STEP-BY-STEP.

1. **Markup**: HTML/CSS, Markdown

    Tell the computer WHAT to DISPLAY, and the computer figures out HOW to do it.

1. **Data Definition**: CSV, JSON/YAML/TOML

    Tell the computer WHAT data to STORE, but don't do anything with it.

1. **Query**: CSS Selector, Regex, Glob

    Tell the computer WHAT information to FIND.

<img width=500px src=img/quote.jpg />

SQL is an example of a **declarative** language.
In SQL, you tell the computer WHAT to COMPUTE,
and the computer figures out HOW automatically.

SQL is arguably the most important language for data scientists.
For example:

1. All interactive webpages use a SQL database to store user content.
    Data scientists run SQL code to extract and process this information.

1. SQL is "provably efficient".
    Python libraries like Pandas are "guaranteed" to be slower than SQL.

    <img width=400px src=img/meme.jpg />

1. Most technical interviews will do advanced SQL problems.
    To get a job as a data scientist, you'll have to write SQL code live in front of your future boss.

    In this class, we won't cover advanced SQL concepts.
    (That will be covered in CSCI143.)
    Instead, we'll be covering how to connect SQL to Python...
    basically the "why should I care" aspect of SQL.

You'll need to know the following SQL commands:

1. CREATE: <https://www.w3schools.com/sql/sql_create_table.asp>

1. INSERT: <https://www.w3schools.com/sql/sql_insert.asp>

1. SELECT: <https://www.w3schools.com/sql/sql_select.asp>
    <!--
    1. WHERE <https://www.w3schools.com/sql/sql_where.asp>
    1. JOIN <https://www.w3schools.com/sql/sql_join_inner.asp>
    -->

1. UPDATE: <https://www.w3schools.com/sql/sql_update.asp>

1. DELETE: <https://www.w3schools.com/sql/sql_delete.asp>

How to run quiz problems:
```
$ pip3 install litecli
$ litecli quiz.db < quiz_schema.sql
$ litecli quiz.db
quiz.db> /* enter problem here */
```

> **NOTE:**
> If a problem runs DELETE/UPDATE on the database,
> you will need to delete and recreate the database before the next problem.
> You can use the commands:
> ```
> $ rm quiz.db
> $ litecli quiz.db < quiz_schema.sql
> ```

<!--
We'll use the following reference for connecting SQL to python:

1. <https://stackabuse.com/a-sqlite-tutorial-with-python/>
-->

### Project Notes

~80% of the class missed points on writing test cases.
1. if you missed points, you can get them back by fixing the test cases for next submission
1. everyone is responsible for good test cases on your next submission

Recall that test cases should:
1. be human readable (simple)
1. actually demonstrate what the function does

Here are examples of bad test cases from students:
```
def cat(filename):
    """Read the contents of a UTF-8 text file.

    >>> from pathlib import Path
    >>> test_path = Path('tools_cat_test.txt')
    >>> _ = test_path.write_text('hello', encoding='utf-8')
    >>> cat('tools_cat_test.txt')
    'hello'
    >>> _ = test_path.unlink()
    >>> cat('tools_cat_test.txt')
    "Error: [Errno 2] No such file or directory: 'tools_cat_test.txt'"
    >>> _ = open('binary_file.txt', 'wb').write(b'\\xff\\xfe')
    >>> cat('binary_file.txt')
    "Error: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte"
    >>> import os; os.remove('binary_file.txt')
    """
```

```
def run_cat(path: str) -> str:
    """Read a file and return text, or an error string if it cannot be read.

    >>> import tempfile
    >>> from pathlib import Path
    >>> with tempfile.TemporaryDirectory() as d:
    ...     p = Path(d)
    ...     f = p / "note.txt"
    ...     _ = f.write_text("hello\\nworld", encoding="utf-8")
    ...     old = Path.cwd()
    ...     import os
    ...     os.chdir(d)
    ...     print(run_cat("note.txt"))
    ...     os.chdir(old)
    hello
    world
    >>> run_cat("../secret.txt")
    'ERROR: unsafe path'
    >>> run_cat("missing.txt")
    'ERROR: file not found'
    >>> import tempfile, os
    >>> from pathlib import Path
    >>> with tempfile.TemporaryDirectory() as d:
    ...     p = Path(d)
    ...     old = os.getcwd()
    ...     os.chdir(d)
    ...     _ = p.joinpath("u16.txt").write_text("hola", encoding="utf-16")
    ...     run_cat("u16.txt")
    ...     os.chdir(old)
    'hola'
    >>> with tempfile.TemporaryDirectory() as d:
    ...     p = Path(d)
    ...     old = os.getcwd()
    ...     os.chdir(d)
    ...     _ = p.joinpath("bad.txt").write_bytes(b"\\xff")
    ...     run_cat("bad.txt")
    ...     os.chdir(old)
    'ERROR: cannot decode file'
    >>> with tempfile.TemporaryDirectory() as d:
    ...     old = os.getcwd()
    ...     os.chdir(d)
    ...     run_cat(".")
    ...     os.chdir(old)
    'ERROR: path is a directory'
```

```
def cat(filename):
    '''
    Opens a file and returns its contents as a string.

    >>> isinstance(cat('chat.py'), str)
    True
```

Better but still bad test cases:

```
def cat(path):
    """
    Read the contents of a file and return it as a string, or return an error message if the file cannot be accessed.

    >>> cat("nonexistent_file.txt")
    'Error: file not found'

    >>> cat("../secret.txt")
    'Error: unsafe path'

    >>> cat(".")
    'Error: could not read file'

    >>> cat("tools/cat.py") != ""
    True
    """
```

```
def cat(path):
    """
    Return the contents of a safe text file.

    >>> cat("../secret.txt")
    'Error: unsafe path'
    >>> cat("this_file_should_not_exist_123.txt").startswith("Error:")
    True
    >>> "def cat(path):" in cat("tools/cat.py")
    True
    """
```

```
def cat(file):
    """Return the full text contents of *file*.

    Blocks absolute paths and directory traversal.  Returns a plain
    error string (not an exception) on failure so the LLM can relay
    the message to the user.

    >>> cat('tools/cat.py').startswith('\"\"\"Tool: read')
    True
    >>> cat('nonexistent_file.txt')
    "Error: file 'nonexistent_file.txt' not found"
    >>> cat('/etc/passwd')
    "Error: path '/etc/passwd' is not allowed"
    >>> cat('../secret.txt')
    "Error: path '../secret.txt' is not allowed"
    >>> import unittest.mock
    >>> with unittest.mock.patch('builtins.open', side_effect=UnicodeDecodeError('utf-8', b'', 0, 1, 'bad')):
    ...     cat('tools/cat.py')
    "Error: file 'tools/cat.py' is not a text file"
    """
```

Example of good test cases:
```
def cat(path):
    r'''
    Returns the contents of a text file.

    >>> cat('test_files/hello_world')
    'hello world'

    >>> print(cat('test_files/hello_world2'))
    hello world
    hola mundo
    salve munde

    Returns an error whenever the path does not exist or is a binary file.

    >>> cat('test_files/does_not_exist')
    'Error: path does not exist')

    >>> cat('test_files/image.png')
    'Error: path is not a text file'

    Does not support absolute paths or directory traversal.

    >>> cat('/etc/passwd')
    'Error: cannot use absolute path'

    >>> cat('../secret_file')
    'Error: input path cannot be relative'
    '''
```

n00bs are infamous for writing crappy tests:

<img width=400px src=img/tests-meme2.jpeg /><br/>
<img width=400px src=img/tests-meme3.webp /><br/>
<img width=400px src=img/tests-meme4.jpg /><br/>

But writing good tests is legitimately hard to do.
And a sign of a truely good programmer is to know which functions should get tested.

<img width=400px src=img/tests-meme-anti1.jpg /><br/>
<img width=400px src=img/tests-meme-anti2.jpg /><br/>

**AI SYSYEMS SUCK AT WRITING TEST CASES!**
1. if your human-facing code smells like AI, you will not get a good job

    what is "human-facing"?

    1. understanding this requires "taste"
    1. AI won't be much help figuring this out
    1. reading other people's code will
1. if your README smells like AI, you will not get a good job
1. **THE CORRECT AI WORKFLOW:**
    1. write the doctests by hand
    1. let the AI write the code that passes the doctest

**New Project Guidelines:**
1. doctests for tools:
    1. may not use any mocks
    1. may not use the `in` or `isinstance` builtins
1. doctests for `Chat` or `repl` may use `in` if you explain why:

    You can replace something like:
    ```
    class Chat:
        '''
        A simple interface for working with LLMs.

        Each instance tracks its own separate conversation.
        Notice that in the conversation below,
        the second response includes information from the first message.

        >>> chat = Chat()
        >>> chat.send_message('my name is bob', temperature=0.0)
        'Arrr, ye be Bob, eh? Yer name be known to me now, matey.'
        >>> chat.send_message('what is my name?', temperature=0.0)
        "Ye be askin' about yer own name, eh? Yer name be... Bob, matey!"

        Because each Chat instance is independent,
        a second instance will not have access to the name specified above.

        >>> chat2 = Chat()
        >>> chat2.send_message('what is my name?', temperature=0.0)
        "Arrr, I be not aware o' yer name, matey."
        '''
    ```
    with
    ```
    class Chat:
        '''
        A simple interface for working with LLMs.

        Because LLMs are non-deterministic, the doctests below do not show the full output of the LLM.
        We simply assert that the model's response includes the name 'Bob' if the conversation has already mentioned the name.

        >>> chat = Chat()
        >>> response = chat.send_message('my name is bob', temperature=0.0)
        >>> response = chat.send_message('what is my name?', temperature=0.0)
        >>> 'Bob' in response
        True

        The response should not include the name 'Bob' if the conversation has not mentioned the name.

        >>> chat2 = Chat()
        >>> response = chat2.send_message('what is my name?', temperature=0.0)
        >>> 'Bob' in response
        False
        '''
    ```

### Interesting Links
1. ChatGPT 4o sycophany:
    - <https://www.lesswrong.com/posts/zi6SsECs5CCEyhAop/gpt-4o-is-an-absurd-sycophant>
    - <https://openai.com/index/sycophancy-in-gpt-4o/>
1. master vs main:
    - <https://github.com/mikeizbicki/cmc-csci143/issues/750>
1. Github's fake star economy:
    - <https://awesomeagents.ai/news/github-fake-stars-investigation/>
    - <https://news.ycombinator.com/item?id=47831621>

