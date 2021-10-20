# Week 07: More matplotlib + Syntactic Sugar

**Monday:**
Fall break, no class

**Wednesday:**

1. We will go over the following "syntactic sugars"

    1. list comprehensions: https://realpython.com/list-comprehension-python/

    1. dictionary comprehensions: https://www.datacamp.com/community/tutorials/python-dictionary-comprehension

    "Syntactic Sugar" is just a short way of writing common idioms in code;
    python is famous for having lots of syntactic sugar

    <img src=syntactic_sugar_everywhere.jpeg width=600px />

    We've already seen some examples of syntactic sugar:

    <img src=while_for.png width=600px />

    List comprehensions are a famous and controversial form of syntactic sugar.
    They can simplify your code a lot, or make it difficult to read.

    <img src=pooh.jpg width=400px />
    <br>
    <br>
    <br>

    <img src=hip.webp width=400px />

    ---

    Form 1:

    ```
    accumulator = [ COMPUTATION for VARIABLE in LIST ]
    ```

    same as

    ```
    accumulator = []
    for VARIABLE in LIST:
        accumulator += COMPUTATION
    ```
    
    Form 2:
    ```
    accumulator = [ COMPUTATION for VARIABLE in LIST if CONDITION]
    ```

    same as

    ```
    accumulator = []
    for VARIABLE in LIST:
        if CONDITION:
            accumulator += COMPUTATION
    ```

    ---

    In general: `while` loops > `for` loops > list comprehensions
    
1. We will continue to cover more common pitfalls with matplotlib

Prelecture video:

1. Corey Shafer's comprehension tutorial: https://www.youtube.com/watch?v=3dt4OGnU5sM

## Lab

TBA
