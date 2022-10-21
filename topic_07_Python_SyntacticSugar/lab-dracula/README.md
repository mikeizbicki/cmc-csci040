# Lab: Dracula

**Overview:**

To celebrate Halloween, you will practice HTML and file/string operations by editing the book *Dracula* to make it even more scary.

**Instructions:**

1. The copyright on the book *Dracula* has expired, and the book is now in the public domain.
    Project Gutenberg (https://gutenberg.org) is a website that makes all public domain books easily downloadable.
    *Dracula* is located at http://www.gutenberg.org/files/345/345-h/345-h.htm .
    Visit this webpage and save it to your computer in a file called `dracula.html` (use: right click -> save as).

1. Create a python file called `dracula.py` file that:
    1. Reads in the text from `dracula.html`.
    2. Replaces all occurrences of the word "Dracula" with "Izbicki".

       All occurrence of the word Izbicki should be in bold so that they are easy to see.

       Recall that the HTML to make a string of text bold is `<strong></strong>`.
       Also note that the title of the book is "D R A C U L A" and this should also change to "I Z B I C K I",
       and that occurrences of "DRACULA" should be replaced by "IZBICKI" maintaining the same capitalization scheme.

    3. Replaces all occurrences of the word "count" with the word "professor".
        Thus, all occurrences of the phrase "Count Dracula" will be replaced by the phrase "Professor Izbicki".

        1. Note that the word "count" is sometimes capitalized and sometimes lowercase.
            You should be able to replace both of these words with the correct case.
            This replacement will sometimes lead to ungrammatical sentences like transforming `Count me in` into `Professor me in`,
            but that's okay for this assignment.

        1. Note that the string "count" sometimes appears inside of a different word, and when this happens, you should not perform the replacement.
            So for example: words like "country"  and "accounting" should not be changed 
            to "professorry" and "acprofessoring".

    4. Replaces all occurrences of the phrase "Bram Stoker" with your name.

    5. Saves the resulting story to a file called `izbicki.html`.

       Note that your final saved file should still have all the html code that makes it a valid webpage.

3. Upload both your `dracula.py` code and `izbicki.html` output file to Sakai.

