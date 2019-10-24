'''
INSTRUCTIONS:

Just like lab 10, today's lab has no doctests for you to complete.

Step 1: Go to https://github.com/bpb27/trump_tweet_data_archive

Step 2: Download the files `condensed_*.json.zip`, where * is a year.
        There should be 10 total files (2009-2018).
        The 2018 file actually also includes tweets from 2019 and is updated hourly.

Step 3: Unzip each of these files to get files that look like `condensed_*.json`.

Step 4: Write a python program that:

    1. Opens each file and loads the file using the json library.
       Each file contains a list of tweets, and if you concatenate each file's tweets
       together you will get a list of all tweets ever sent by Donald Trump.

    2. Prints the total number of tweets.

    3. Counts the number of tweets that contain the following keywords:
       `Obama`, `Trump`, `Mexico`, `Russia`, and `Fake News`.
       It's important to remember that each of these words can appear with many 
       different capitalizations, and your program should count the word 
       no matter how it is capitalized.  For example, `OBAMA`, `obama`, and `ObAmA`
       all need to count as an occurance of the word `Obama`.

    4. Prints out a count of each of these words.

My program ran on all tweets as of 7AM on 24 October 2019 gives the output

    len(tweets)= 36307
    counts= {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333, 'mexico': 199}

Your program should give the same numbers (or possibly a few higher if Trump sends new tweets over the next few days).

========================================
EXTRA CREDIT:

You may earn up to 3 points of extra credit on this lab if you also:

    1. select at least 3 more interesting words/phrases to count in trump's tweets,

    2. calculate the percentage of tweets that contain each word, and

    3. display them nicely.

The display must have all words right justified and the percents printed with two 
significant figures (on both sides of the decimal) as shown in the example output below.

    percentage of tweets using phrase:
                  daca : 00.17
             fake news : 00.92
      mainstream media : 00.06
                mexico : 00.55
                 obama : 07.47
                russia : 01.13
                 trump : 38.35
                  wall : 00.91
'''

