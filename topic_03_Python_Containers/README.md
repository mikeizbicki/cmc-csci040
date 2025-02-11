# Week 03: Python containers (lists and dictionaries)

<img width=500px src=img/two-states-of-programmers.png />

1. We will cover [Chapter 4 - Lists](https://automatetheboringstuff.com/2e/chapter4/) abd [Chapter 5 - Dictionaries](https://automatetheboringstuff.com/2e/chapter5/) of the book.

1. Electronic version of quiz pdf at <https://github.com/mikeizbicki/quiz/blob/master/quiz_python/topic03_containers.pdf>

1. Background videos:

    1. [Lesson 10](https://www.youtube.com/watch?v=M-CoVBK_bLE&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=10)

       Key terms:

       1. local scope

       1. global scope

       1. local variable

       1. global variable

       How can you tell if a variable is local or global?

    1. [Lesson 11](https://www.youtube.com/watch?v=qS0UkqaYmfU&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=11)

        Key terms:

        1. `try`

        1. `except`

        1. input validation

     1. [Lesson 12](https://www.youtube.com/watch?v=48WXHT0dfEY&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=12)

     1. [Lesson 13](https://www.youtube.com/watch?v=48WXHT0dfEY&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=12)

        Key terms:

        1. list

        1. item

        1. comma deliminated

        1. `[]`

        1. index

        1. negative indexes

        1. slice

        1. slice shortcuts

        1. `del`

        1. `list()`

        1. `in`

        1. `not in`

        <!-- len is polymorphic -->

    1. [Lesson 14](https://www.youtube.com/watch?v=umTnflPbYww&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=14)

       Key terms:

       1. list-like / sequences

       1. range object

       1. multiple assignment

       1. swapping variables

       1. augmented assignment operators

    1. [Lesson 15](https://www.youtube.com/watch?v=Z9IxxW7428A&list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW&index=15)

       Key terms:

       1. method vs function

       1. `.index`

       1. `.append` <-- important

       1. `.insert`

       1. `.remove`

       1. `.sort` <-- important

       1. ASCII-betical order

    1. [Dictionaries](https://www.youtube.com/watch?v=daefaLgNkw0)        

        Key Terms:

        1. dictionary, map, key-value pair

        1. key

        1. value

        1. `{}`

        1. `[]`

        1. `.get`

        1. `.update`

        1. `del`

        1. `.keys`

        1. `.values`

        1. `.items`

## Lab

TBA

<!--
<center>
<img width=800px src=img/phd113007s1.gif />
</center>

Complete the `lab.py` file and submit your doctests to sakai.

def min_of_digits(n):
    '''
    Return the smallest digit in the input number n.

    HINT:
    This function uses the same while loop pattern as sum_of_digits.

    >>> min_of_digits(1)
    1
    >>> min_of_digits(57)
    5
    >>> min_of_digits(75)
    5
    >>> min_of_digits(571)
    1
    >>> min_of_digits(1234567890)
    0
    >>> min_of_digits(9999999949999)
    4
    '''
    minimum = 10
    while n>0:
        if n%10 < minimum:
            minimum = n%10
        n //= 10
    return minimum


-->
