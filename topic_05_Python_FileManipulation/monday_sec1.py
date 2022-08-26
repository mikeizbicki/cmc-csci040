###############################################################################
# Language issues
###############################################################################

# foreign language text can be included into `str`s

english = 'Computer programming is the best!!!'
chinese = '计算机编程是最好的！！！'
korean = '컴퓨터 프로그래밍이 최고입니다 !!!'
vietnamese = 'lập trình máy tính là tốt nhất !!!'
arabic = '!‏برمجة الكمبيوتر هي الأفضل!‏!‏'

# you can have the same string with multiple languages inside

combined = 'Computer 计算机 هي الأفضل tốt nhất !!!'

# variables can be named using any language

컴퓨터 = 'this is a variable'

# emojis work fine

emoji1 = '😊'
emoji2 = '💩'

# some things are weird

german = 'Strauß'

numbers = '৪৭' # In Tamil ৪ = 4 , ৭ = 7

url1 = 'https://www.BankOfAmerica.com'
url2 = 'https://www.ΒankΟfΑmerica.com'
url3 = 'https://www.BankOf​America.com'

greek = 'αβγδεζηθικλμνξοπρςστυφχψ'

empty = '​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​'

###############################################################################
# Code points
###############################################################################

# Background:
# - a "grapheme" is what Unicode calls an individual "unit" of text being displayed;
#   it's what most people would call a "letter"/"symbol"/"character"
# - a "font" is a set of pictures associated with each grapheme

# Graphemes can be composed of one or more "characters",
# and the same grapheme can be written in different ways

accents_1 = 'á'
accents_2 = 'á'

# len() function displays the number of characters, not the number of graphemes

# Equality in python (and all programming languages) is not based on grapheme-equivalence;
# it is based on character-equivalence

# Every character has a Unicode "code point" that represents the character.
# ord() converts from `str` to the code point
# chr() converts from the code point to `str`

accents_1a = '\xe1'         # \x has range from 0 - 255
accents_1b = '\u00e1'       # \u has range from 0 - 65535
accents_1c = '\U000000e1'   # \U can store from 0 - 4 billion  character, grapheme same, notation is different
accents_2b = 'a\u0301'      # has same grapheme, different characters
accents_2c = 'a\U00000301'

# NOTE:
# We cannot use the `\x` notation to write the character '\u0301'.
# \x only supports code points from 0-255 (1 byte);
# \u supports code points from 0-65335 (2 bytes);
# \U supports all code points (4 bytes);


# character normalization = represent the graphemes in a standard way
# normal form composed (NFC) groups graphemes into as few characters as possible
# normal form decomposed (NFD) ungroups graphemes into as many characters as possible

import unicodedata
#accents_3 = unicodedata.normalize('NFC', accents_1)

# Example: Vietnamese

vietnamese_NFKD = 'lập trình máy tính là tốt nhất !!!'
vietnamese_NFKC = 'lập trình máy tính là tốt nhất !!!'

# Example: Arabic
# Arabic has lots of special characters, see: https://en.wikipedia.org/wiki/Arabic_script_in_Unicode

pbuh = 'ﷺ'       # "Peace be upon him"
basmala = '﷽'   # "In the name of Allah"

# PRINCIPLE 1:
# You must normalize your strings if you want to compare them.

# It doesn't matter which normal form you use in your application,
# but you must pick one and use it consistently.
# Python will not normalize text for you automatically.


# Example: Korean
# Recall that sorting in python is done ASCII-betically for English text
# For non-English text, we sort "Unicode"-betically, or by the Unicode code points of text

korean_alphabet_ROK = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ']
korean_alphabet_DPRK = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄲ', 'ㄸ']

# PRINCIPLE 2:
# It is impossible to sort text "correctly" in any programming language
# unless you know "meta" information about the user (e.g. their country).


###############################################################################
# Encoding
###############################################################################

# The `str` type in python is "syntactic sugar" for a list of code points.
# But how are these code points actually stored physically on the computer?

# Background:
# - a bit is a 0 or a 1
# - one byte is 8 bits
# - a byte is the fundamental unit of information in computer science
# - 8 bits is large enough to store ASCII values (end hence english values, but nothing more)

# a document with 1000 english characters; that means 1000 ASCII values => 1000 bytes

# The `byte` type looks like strings but starts with a `b`

normal_strings = 'they just \n have quotes'
raw_strings = r'quotes that \n start with r' # ignores escape characters

example = b'this is a `byte`'

# everytime you load a file in python, you are always reading bytes

# NOTE:
# The type `byte` in python stores more than one byte!
# 
# The `byte` type represents a container of many bytes,
# and so is similar to a string.
# But because the `byte` type can only store 8bits,
# it cannot store non-ASCII (i.e. non-English) characters.

# >>> korean = b'컴퓨터 프로그래밍이 최고입니다 !!!'
#  File "<stdin>", line 1
# SyntaxError: bytes can only contain ASCII literal characters.

# In order to store non-English text, we need an "encoding" which maps bytes to characters
# .encode() converts from `str` to `byte`
# .decode() converts from `byte` to `str`

# The most popular encoding is UTF-8
# This is a "variable-length" encoding, which means it uses a different number of bytes for each character
# UTF-8 is popular because it "agrees" with ASCII

bytes1 = 'hello world'.encode('utf-8')
bytes2 = 'hello world'.encode('utf-16')
bytes3 = 'hello world'.encode('utf-32')
bytes4 = 'hello world'.encode('iso-8859-1')
bytes5 = 'hello world'.encode('ascii')

# PRINCIPLE 3:
# Whenever you are working with bytes, you must know "meta" information about the encoding.

# Unfortunately, not all encodings support all languages/characters.
# Any encoding that begins with "utf" is safe for unicode characters.

chinese_bytes1 = '计算机编程是最好的！！！'.encode('utf-8')
chinese_bytes2 = '计算机编程是最好的！！！'.encode('utf-16')
chinese_bytes3 = '计算机编程是最好的！！！'.encode('utf-32')
#chinese_bytes4 = '计算机编程是最好的！！！'.encode('iso-8859-1')
#chinese_bytes5 = '计算机编程是最好的！！！'.encode('ascii')

# The len() reports how many bytes a `byte` consumes.

len(chinese_bytes1)
len(chinese_bytes2)
len(chinese_bytes3)

# PRINCIPLE 4:
# Some encodings are better for some languages than others.

# UTF-8 prioritizes English, but it has become the default encoding for most languages.
# This makes a lot of Asians upset because they "waste" lots of disk space/bandwidth.