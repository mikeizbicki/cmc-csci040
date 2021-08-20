# Week 08: Syntactic Sugar and non-English Languages

<center>
<img width='80%' src=vomiting_emoji.png />
</center>

You can find an explanation of this comic at https://www.explainxkcd.com/wiki/index.php/1813:_Vomiting_Emoji

**Quiz:**
No quiz this week :)

Catch up on your sleep and do well on any midterms you have this week.
<!--
The completed `quiz.pdf` should be submitted to sakai by Friday at midnight.
-->

**Monday/Wednesday:**
We will cover a wide variety of topics that don't neatly fit into other portions of the course.

Non-decimal number systems

1. https://www.youtube.com/watch?v=ZL-LhaaMTTE

Unicode support in python

1. The story of the gun emoji

    1. https://blog.emojipedia.org/apple-and-the-gun-emoji/
    1. https://www.businessinsider.com/apple-change-pistol-emoji-toy-confusion-precedent-meaning-retroactive-2016-8

1. Python tutorial: https://realpython.com/python-encodings-guide/

1. growth of UTF-8: https://en.wikipedia.org/wiki/UTF-8#/media/File:Utf8webgrowth.svg

1. NSA's security risks of Unicode: https://apps.nsa.gov/iaarchive/library/reports/unicode-security-risks.cfm

List comprehensions

1. https://realpython.com/list-comprehension-python/

<!--
https://www.youtube.com/watch?v=oXVmZGN6plY&t=478s

1. `ord`

1. `chr`


ASCII, Unicode, UTF-8, UTF-16, UTF-32, encode, decode

bit, byte

binary, decimal, octal, hexidecimal, base N

int('11',base=8), `bin`, `0b`, `oct`, `0c`, `hex`, `0x`

`ord`,`chr`,`ascii`

`string` module

```
>>> import string
>>> s = "What's wrong with ASCII?!?!?"
>>> s.rstrip(string.punctuation)
```

`str` vs `bytes`

résumé = "~/Documents/resume.pdf"

>>> ibrow = "🤨"
>>> len(ibrow)
1
>>> ibrow.encode("utf-8")
b'\xf0\x9f\xa4\xa8'
>>> len(ibrow.encode("utf-8"))
4o

>>> letters = "αβγδ"
>>> rawdata = letters.encode("utf-8")
>>> rawdata.decode("utf-8")
'αβγδ'
>>> rawdata.decode("utf-16")  # 😧
'뇎닎돎듎'


>>> text = "記者 鄭啟源 羅智堅"
>>> len(text.encode("utf-8"))
26
>>> len(text.encode("utf-16"))
22

>>> alphabet = 'αβγδεζηθικλμνξοπρςστυφχψ'
>>> print(alphabet)
αβγδεζηθικλμνξοπρςστυφχψ


https://en.wikipedia.org/wiki/UTF-8#/media/File:Utf8webgrowth.svg

https://apps.nsa.gov/iaarchive/library/reports/unicode-security-risks.cfm

```
>>> '৪৭'
'৪৭'
>>> int('৪৭')
47
>>> int('89')
89
>>> int('৪৭')
47
>>> ('Strauß')
'Strauß'
>>> len('Strauß')
6
>>> len('Strauß'.upper())
7
>>> len('Strauß'.upper().lower())
7
>>> 'ΐ'
'ΐ'
>>> len('ΐ')
1
>>> len('ΐ'.upper())
3
>>> 'Strauß'.upper()
'STRAUSS'
>>> 'ΐ'.upper()
'Ϊ́'
>>> len('Ϊ́')
3
```



# if there's any chance of using foreign characters in a string,
# then you must normalize the string before doing comparisons

>>> unicodedata.normalize('NFC', u'\u0061\u0301')
u'\xe1'
>>> unicodedata.normalize('NFD', u'\u00e1')
u'a\u0301'


>>> import unicodedata
>>> char = "á"
>>> len(char)
1
>>> [ unicodedata.name(c) for c in char ]
['LATIN SMALL LETTER A WITH ACUTE']

But now:

>>> char = "á"
>>> len(char)
2
>>> [ unicodedata.name(c) for c in char ]
['LATIN SMALL LETTER A', 'COMBINING ACUTE ACCENT']

-->

**Thursday:** Lab.

There is no lab this week.
I will still be available during the normal lab times for questions about your reddit bot homework.

<!--
## Lab

In this lab you will create functions for randomly generating comments.
The instructions are in the `lab.py` file.
-->

