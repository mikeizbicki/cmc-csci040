################################################################################
# To simplify the test cases for this lab,
# I've created several dictionary variables that show example uses of dictionaries.
# The first set of examples involve grades for a math, english, and economics class.
################################################################################

math_grades={
        'donald knuth':85,
        'hypatia':75,
        'emmy noether':86,
        'leonhard euler':92,
        'albert einstein':95,
        'shelton cooper':72,
        'ada lovlace':96,
        'mike izbicki':100,
        }

english_grades={
        'emily dickenson':92,
        'edgar allan poe':88,
        'robert frost':83,
        'dorthy day':95,
        'douglas adams':42,
        'maya angelou':89,
        'emma goldman':85,
        'mike izbicki':100
        }

economics_grades={
        'john maynard keynes':82,
        'christine lagarde':85,
        'alan greenspan':92,
        'adam smith':88,
        'kristalina georgieva':79,
        'karl marx':90,
        }

def get_number_of_students_in_class(d):
    '''
    returns the total number of entries in the dictionary

        >>> get_number_of_students_in_class(math_grades)
        8
        >>> get_number_of_students_in_class(english_grades)
        8
        >>> get_number_of_students_in_class(economics_grades)
        6
    '''

def student_with_highest_grade(d):
    '''
    returns the key that has the greatest value

        >>> student_with_highest_grade(math_grades)
        'mike izbicki'
        >>> student_with_highest_grade(english_grades)
        'mike izbicki'
        >>> student_with_highest_grade(economics_grades)
        'alan greenspan'
    '''

def students_getting_an_a(d):
    '''
    returns a list of students whose grade is at least 90;
    that is, it returns all keys whose value is at least 90

    NOTE: the returned list is required to be sorted,
    and this can be achieved by using the sort() function

        >>> students_getting_an_a(math_grades)
        ['ada lovlace', 'albert einstein', 'leonhard euler', 'mike izbicki']
        >>> students_getting_an_a(english_grades)
        ['emily dickenson', 'dorthy day', 'mike izbicki']
        >>> students_getting_an_a(economics_grades)
        ['alan greenspan', 'karl marx']
    '''

################################################################################
# Twitter uses python dictionaries to store the information about each tweet.
# The following list contains real tweets sent by President Trump.
################################################################################

trump_tweets=[
        { "id_str": "947824196909961216", 
          "text": "Will be leaving Florida for Washington (D.C.) today at 4:00 P.M. Much work to be done, but it will be a great New Year!", 
          "created_at": "Mon Jan 01 13:37:52 +0000 2018",
          "retweet_count": 8656, 
          "user":{
            "name":"Donald J. Trump",
            "screen_name":"realdonaldtrump",
            "location":"Washington, DC",
            },
          },
        { "id_str": "947614110082043904", 
          "text": "HAPPY NEW YEAR! We are MAKING AMERICA GREAT AGAIN, and much faster than anyone thought possible!", 
          "created_at": "Sun Dec 31 23:43:04 +0000 2017", 
          "retweet_count": 35394, 
          "user":{
            "name":"Donald J. Trump",
            "screen_name":"realdonaldtrump",
            "location":"Washington, DC",
            },
          }, 
        { "id_str": "947810806430826496", 
          "text": "Iran is failing at every level despite the terrible deal made with them by the Obama Administration. The great Iranian people have been repressed for many years. They are hungry for food &amp; for freedom. Along with human rights, the wealth of Iran is being looted. TIME FOR CHANGE!", 
          "created_at": "Mon Jan 01 12:44:40 +0000 2018", 
          "retweet_count": 15176, 
          "user":{
            "name":"Donald J. Trump",
            "screen_name":"realdonaldtrump",
            "location":"Washington, DC",
            },
          }, 
        { "id_str": "947802588174577664", 
          "text": "The United States has foolishly given Pakistan more than 33 billion dollars in aid over the last 15 years, and they have given us nothing but lies &amp; deceit, thinking of our leaders as fools. They give safe haven to the terrorists we hunt in Afghanistan, with little help. No more!", 
          "created_at": "Mon Jan 01 12:12:00 +0000 2018", 
          "retweet_count": 51483, 
          "user":{
            "name":"Donald J. Trump",
            "screen_name":"realdonaldtrump",
            "location":"Washington, DC",
            },
          }, 
        { "id_str": "947592785519173637", 
          "text": "As our Country rapidly grows stronger and smarter, I want to wish all of my friends, supporters, enemies, haters, and even the very dishonest Fake News Media, a Happy and Healthy New Year. 2018 will be a great year for America!", 
          "created_at": "Sun Dec 31 22:18:20 +0000 2017", 
          "retweet_count": 39698, 
          "user":{
            "name":"Donald J. Trump",
            "screen_name":"realdonaldtrump",
            "location":"Washington, DC",
            },
          }, 
        ]

def most_retweeted(lst):
    '''
    This function takes as input a list of tweets,
    it inspects these tweets to find the tweet with the highest "retweet_count",
    and returns the "id_str" of that tweet.

        >>> most_retweeted(trump_tweets[:1])
        '947824196909961216'
        >>> most_retweeted(trump_tweets[:2])
        '947614110082043904'
        >>> most_retweeted(trump_tweets[:3])
        '947614110082043904'
        >>> most_retweeted(trump_tweets[:4])
        '947802588174577664'
        >>> most_retweeted(trump_tweets[:5])
        '947802588174577664'
    '''


################################################################################
# DO NOT MODIFY BELOW THIS LINE
################################################################################

import doctest
doctest.testmod(verbose=True)
