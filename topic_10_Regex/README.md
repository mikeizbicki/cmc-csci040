# Regular Expressions (regex) + Globbing

Announcements:

1. Collaboration Policy Reminder: <https://github.com/mikeizbicki/cmc-csci040/issues/377>

1. leetcode extra credit: <https://github.com/mikeizbicki/cmc-csci040/issues/393>

1. Quiz Wednesday on glob/regex

    Example problems at <https://github.com/mikeizbicki/quiz/blob/master/quiz_shell/topic01_glob_regex.pdf>

    You will need to understand this syntax for your next project (which we will go over Wednesday).

    Both glob and regex have reputations as:
    1. having scary, non-intuitive syntax
    1. being straightforward (but not "easy") once you work through some examples
    1. being *very* useful

    <br/>
    <img width=400px src=img/cat.jpeg />

    <img width=400px src=img/you-dont.jpg />

## Why do LLMs struggle with regex/globbing?

1. This is the type of question that computer scientists study.

    (And the type of question that you will be able to answer if you take upper-div CS courses.)

1. Answer questions like this requires math.

    <img src=img/math.webp width=400px />

    1. Actual answer (informal proof):

        1. regex expressions require $O(n^2)$ time to run in worst case;
        1. LLMs can only implment $O(n)$ runtime algorithms
        1. $O(n) < O(n^2)$
        1. therefore computing regex is beyond the compute of LLMs

    1. Why can LLMs code certain types of regex/globs?

        How can I know which types of regex/globs LLMs will be able to code?

        Need to take upper-div CS to find out.

        This is the type of reasoning that CS teaches you.

        Coding is not CS.

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
    | MATH126 (randomized algorithms) | 0% programming | 100% math |
    | MATH163 (quantum computing) | 0% programming | 100% math |

    what to take next:
    1. DS sequence / major: CSCI036 (easier than this course)
    1. CS sequence / DS major: CSCI046 (similar difficulty to this course)
