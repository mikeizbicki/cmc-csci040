###############################################################################
# Most languages "just work" in python
###############################################################################

# foreign language text can be included into `str`s
English = 'Computer programming is the best!!!'
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
emoji2 = '😔'
emoji3 = '💩'
emoji4 = '🔫'

###############################################################################
# Some things are "just weird"
###############################################################################

# for historical reasons, some characters contain font information 
italic = '𝘊𝘰𝘮𝘱𝘶𝘵𝘦𝘳 𝘱𝘳𝘰𝘨𝘳𝘢𝘮𝘮𝘪𝘯𝘨 𝘪𝘴 𝘵𝘩𝘦 𝘣𝘦𝘴𝘵'
fraktur = '𝕮𝖔𝖒𝖕𝖚𝖙𝖊𝖗 𝖕𝖗𝖔𝖌𝖗𝖆𝖒𝖒𝖎𝖓𝖌 𝖎𝖘 𝖙𝖍𝖊 𝖇𝖊𝖘𝖙'
teletype = 'Ｃｏｍｐｕｔｅｒ　ｐｒｏｇｒａｍｍｉｎｇ　ｉｓ　ｔｈｅ　ｂｅｓｔ'
upsidedown = 'ʇsǝq ǝɥʇ sı ɓuıɯɯɐɹɓoɹd ɹǝʇndɯoƆ'
circles = 'Ⓒⓞⓜⓟⓤⓣⓔⓡ ⓟⓡⓞⓖⓡⓐⓜⓜⓘⓝⓖ ⓘⓢ ⓣⓗⓔ ⓑⓔⓢⓣ'

# upper/lower case is "weird"
german = 'Strauß'

# numbers are "weird" in some languages
numbers = '৪৭' # In Tamil ৪ = 4 ; ৭ = 7

# some languages "look like each other"; this is a security issue
url1 = 'https://www.BankOfAmerica.com'
url2 = 'https://www.ΒankΟfΑmerica.com'
url3 = 'https://www.BankOf​America.com'

greek = 'αβγδεζηθικλμνξοπρςστυφχψ'

# some characters don't display
empty = '​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​'

###############################################################################
# Code points
###############################################################################

# Unicode is the standard system for representing ALL languages on computers
# Python 3.0 was the first major programming language to have "good" Unicode support
# C/C++/Java have Unicode support; but it's not "trivial" in python

# About Unicode
# - a "grapheme" is what Unicode calls an individual unit of text being displayed;
#   it's what most people would call a "letter"/"symbol"/"character"
# - a "font" is a set of pictures associated with each grapheme
# - graphemes can be composed of one or more "characters",
#   and the same grapheme can be written in different ways

accents_1 = 'á'
accents_2 = 'á'

# NOTE:
# Equality in python (and all programming languages) is not based on grapheme-equivalence;
# it is based on character-equivalence

# NOTE:
# len() function displays the number of "code points"/"characters", not the number of graphemes

# Every character has a Unicode "code point" that represents the character.
# ord() converts from `str` to the code point (`int`)
# chr() converts from the code point to `str`

# these \XXXXX represent the a with the accent
accents_1a = '\xe1'         # \x has range from 0 - 255
accents_1b = '\u00e1'       # \u has range from 0 - 65535
accents_1c = '\U000000e1'   # \U can store from 0 - 4 billion  character

# these \XXXXX represent "add an accent to the previous character"
accents_2b = 'a\u0301'      
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
accents_1_NFC = unicodedata.normalize('NFC', accents_1)
accents_2_NFC = unicodedata.normalize('NFC', accents_2)

# Example: Vietnamese

vietnamese_NFD = 'lập trình máy tính là tốt nhất !!!'
vietnamese_NFC = 'lập trình máy tính là tốt nhất !!!'

# NFKD/NFKC normal forms are used to remove "font" information
# The "K" stands for "compatibility"

# Example: Fractur
fractur_NFC = unicodedata.normalize('NFC', '𝕮𝖔𝖒𝖕𝖚𝖙𝖊𝖗 𝖕𝖗𝖔𝖌𝖗𝖆𝖒𝖒𝖎𝖓𝖌 𝖎𝖘 𝖙𝖍𝖊 𝖇𝖊𝖘𝖙')
fractur_NFD = unicodedata.normalize('NFD', '𝕮𝖔𝖒𝖕𝖚𝖙𝖊𝖗 𝖕𝖗𝖔𝖌𝖗𝖆𝖒𝖒𝖎𝖓𝖌 𝖎𝖘 𝖙𝖍𝖊 𝖇𝖊𝖘𝖙')
fractur_NFKC = unicodedata.normalize('NFKC', '𝕮𝖔𝖒𝖕𝖚𝖙𝖊𝖗 𝖕𝖗𝖔𝖌𝖗𝖆𝖒𝖒𝖎𝖓𝖌 𝖎𝖘 𝖙𝖍𝖊 𝖇𝖊𝖘𝖙')
fractur_NFKD = unicodedata.normalize('NFKD', '𝕮𝖔𝖒𝖕𝖚𝖙𝖊𝖗 𝖕𝖗𝖔𝖌𝖗𝖆𝖒𝖒𝖎𝖓𝖌 𝖎𝖘 𝖙𝖍𝖊 𝖇𝖊𝖘𝖙')

# Example: Arabic
# Arabic has lots of special characters, see: https://en.wikipedia.org/wiki/Arabic_script_in_Unicode

pbuh = 'ﷺ'       # "Peace be upon him"
basmala = '﷽'   # "In the name of Allah"


# PRINCIPLE 1:
# You must normalize your strings if you want to compare them.
# Python will not normalize text for you automatically.
# It is traditional to use NFC,
# but it does not matter which one you choose.

################################################################################
# Sorting
################################################################################

# Recall that sorting in python is done ASCII-betically for English text
# For non-English text, we sort "Unicode"-betically, or by the Unicode code points of text

# Example: German
words = ['Bären', 'Käfer', 'küssen', 'Ähnlich', 'Äpfel'];

# Example: Korean
korean_alphabet_ROK = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ']
korean_alphabet_DPRK = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄲ', 'ㄸ']

# PRINCIPLE 2:
# It is impossible to sort text "correctly" in any programming language
# unless you know "meta" information about the "locale" of the user (e.g. their country).

###############################################################################
# Encoding
###############################################################################

# How are strings physically stored on the computer?

# Background:
# - a bit is a 0 or a 1
# - one byte is 8 bits
# - a byte is the fundamental unit of information in computer science
# - 8 bits is large enough to store ASCII values (end hence English values, 
#   but nothing more)

# Example:
# A document with 1000 English characters needs 1000 bytes = 1kb

# The `bytes` type looks like strings but starts with a `b`
normal_strings = 'they just \n have quotes'
raw_strings = r'quotes that \n start with r' # ignores escape characters
example = b'this is a `byte`'

# NOTE:
# raw strings are just normal strings, and so they can be compared directly;
# byte strings (i.e. `bytes`) are an entirely different type;
# so they cannot be compared directly with strings.

# NOTE:
# The type `bytes` in python stores more than one byte!
# The `bytes` type represents a container of many bytes,
# and so is similar to a string.
# But because the `bytes` type can only store 8bits at each position,
# it cannot store non-ASCII (i.e. non-English) characters.

# Example:
# >>> korean = b'컴퓨터 프로그래밍이 최고입니다 !!!'
#  File "<stdin>", line 1
# SyntaxError: bytes can only contain ASCII literal characters.

# Every time you load a file in python,
# you are always reading bytes

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
