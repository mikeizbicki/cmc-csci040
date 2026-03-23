# Object Oriented Programming (OOP)

**Announcements (Monday 9 March):**

1. Current grade distribution:

    | grade range       | num students |
    | ----------------- | ------------ |
    | 100 <= grade      | 3            |
    | 90 <= grade < 100 | 9            |
    | 80 <= grade < 90  | 5            |
    | grade < 80        | 2            |

2. Syntactic sugar quiz this Wednesday.

    Recall: we didn't cover everything in class.

3. No lab session this Friday (due to spring break).

    1. Still have lab assignment (posted below).

    1. I will be available in my office during lab time if you'd like to ask questions.

4. After spring break quiz on <https://github.com/mikeizbicki/quiz/blob/master/quiz_python_with_exceptions/topic06_oop.pdf>

**Announcements (Monday 23 March):**

1. Everything graded

1. Reminder:
    1. quiz Wednesday on OOP
    1. no class Friday (Cesar Chavez day)

1. Map of rest of semester
    1. you've completed about 40% of the points in this class
    1. weekly quizzes / labs
    1. 3 projects

        due dates no earlier than:

        | project | date |
        | --- | --- |
        | Project 3 - AI retrieval augmented generation (RAG) | Tuesday, Apr 7 |
        | Project 4 - AI coding agent | Tuesday, Apr 21 |
        | Project 5 - Twitter Clone | (graduating) Wednesday, May 6<br/> (non-graduating) Friday, May 15 |

1. For Wednesday:

    Create an API key with groq.com: <https://console.groq.com/keys>
    - faster than OpenAI, but 1-2 year old models
    - free LLM access, but limited number of requests
    - you can complete all required tasks for this class with the free tier

    (optional) Create an API key at: <https://openrouter.ai/>
    - allows access to *every* AI system from one location (e.g. OpenAI/Anthropic/Google/Grok)
    - costs money ($10 will be enough for this class)
    - some extra credits will require using these AI systems

## Lecture Notes

1. References:

    1. <https://automatetheboringstuff.com/> does not cover OOP.

    1. Book Reference: [Chapter 1.13](https://runestone.academy/runestone/books/published/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html) and [Chapter 2](https://runestone.academy/runestone/books/published/pythonds/ProperClasses/toctree.html)

    1. <https://realpython.com/python3-object-oriented-programming/>

1. The `class` keyword lets you define your own data structures

    1. Object Oriented Programming (OOP) is programming with classes

        1. Pronounce OOP as "Oh Oh Pee"

        1. You should think of a class as a "container"

        1. IMNSHO, most OOP programming takes the "using classes" idea too far, and use classes where it's not appropriate

           <img src=img/1*6rqSrrz_Q5m80KZM9XbqRg.jpeg />
           <br/>
           <br/>

           <img src=img/8jcj2z7h61741.png width=600px />
           <br/>
           <br/>

           <img src=img/object-oriented-programming-is-an-exceptionally-bad-idea-which-could-only-63887355.png />

    1. OOP vocabulary:

        1. an "object" is what a variable references;
           an "instance" of a class is an object whose type is that "class";

           in python, the `type` function returns the type of the object

        1. Python uses [duck typing](https://en.wikipedia.org/wiki/Duck_typing)

           <img src=img/duck.jpg width=400px />

           <img src=img/dog-duck.jpeg width=400px />

        1. variables within a class are called "attributes" or "properties"

           in other programming languages, there is a distinction between "private" attributes (only accessible within the class) and "public" attributes (accessible everywhere);
           in python, no such distinction exists;
           if an attribute "should" not be accessed outside of the class, in python, we prefix the name with an underscore

           <img src=img/thinking-about-class-structure-object-oriented-programmers-marxists-also-strong-opinions-66225550.png />

        1. functions within a class are called "methods"

        1. functions that begin/end with double underscores are called "double underscore"/"dunder" methods or "magic" methods

            1. `__init__` is the "constructor" and is called when an instance is first created

               <img src=img/m3vxtt66jsg61.jpg width=400px />

<!--
            1. `__str__` / `__repr__` methods let us "pretty print" our objects;
               `__str__` should be human readable, `__repr__` should be machine readable

               Reference: <https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr>
-->

1. PEP8: <https://www.python.org/dev/peps/pep-0008/>

    1. Naming:
        1. PEP = Python Enhancement Proposal
        1. the 8 in flake8 comes from PEP8
        1. the flake in flake8 comes from [pyflakes](https://pypi.org/project/pyflakes/),
            which does [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) to find broken (i.e. flakey) code

    1. class names should be in `CamelCase`

    1. everything else is `snake_case`

    1. python never uses `lowerCamelCase` (like CamelCase but first letter is lowercase; this is common in other languages)

## Lab

Posted at: <https://github.com/mikeizbicki/pullrequest-tutorial/>
