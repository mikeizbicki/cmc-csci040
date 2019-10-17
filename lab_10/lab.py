'''
INSTRUCTIONS:

Today's lab is a little different than previous labs.
In particular, there are no doctests that you need to complete.

First, download the book Dracula from http://www.gutenberg.org/files/345/345-h/345-h.htm
and save it in the same directory as your lab.py file.

Then, modify the lab.py file so that:
    1. It reads in the text from Dracula
    2. Replaces all occurrences of the word "Dracula" with "Izbicki"
           All occurrence of the word Izbicki should be in bold so that they are easy to see.
           (Recall that the HTML to make a string of text bold is <strong></strong>.)
           Also note that the title of the book is "D R A C U L A" and this should also change to "I Z B I C K I",
           and that occurrences of "DRACULA" should be replaced by "IZBICKI" maintaining the same capitalization scheme.
    3. Replaces all occurrences of the word "count" with the word "professor".
            Thus, all occurrences of the phrase "Count Dracula" will be replaced by the phrase "Professor Izbicki".
            Note that the word "count" is sometimes capitalized and sometimes lowercase;
            you should be able to replace both of these words with the correct case;
            this will sometimes lead to ungrammatical sentences like "Professor me in",
            but that's okay.
            Also note that words like "country"  and "accounting" should NOT be changed 
            to "professorry" and "acprofessoring";
            you must only replace the word "count" and not words where "count" appears as a substring.
    4. Replaces all occurrences of the phrase "Bram Stoker" with your name
    5. Saves the resulting story to a file called "izbicki.html"
    6. The final file should still have all the html code that makes it a valid webpage
    7. You will upload both your code and the html file izbicki.html to Sakai.
'''
