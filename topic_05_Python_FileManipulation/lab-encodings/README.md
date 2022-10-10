# Lab: Files and File Encodings

## Part 1: Historical Problems with non-English Text

In 1972, President Richard Nixon flew to China

<img src= width=800px />

The [Shanghai Communiqué](https://en.wikipedia.org/wiki/Shanghai_Communiqu%C3%A9) was a joint statement by the United States and the People's Republic of China (PRC) in 1972.
The communiqué is famous for first articulating the United States' [One China](https://en.wikipedia.org/wiki/One_China) policy with the following declaration:

> The United States acknowledges that all Chinese on either side of the Taiwan Strait maintain there is but one China and that Taiwan is a part of China. The United States Government does not challenge that position. 

<!--
Describes the subtle arts of translation:
[](https://usuaris.tinet.cat/apym/on-line/translation/2018_trust_hubris.pdf)
Describes the fallout of changing translation:
https://china.usc.edu/michel-oksenberg-translation-problem-joint-communique-january-3-1979
-->

The official English version of the document was stored electronically as ASCII text.
You can find a copy in the file `shanghai_communique.english`.

> **NOTE:**
> It is possible on modern computers for filenames to contain spaces and non-ASCII characters, but these weird characters require special handling in certain edge cases, and so it is traditional not to use these characters.

Run the following code to view the communiqué from python:
```
>>> f = open('shanghai_communique.english', mode='tr', encoding='ascii')
>>> text_english = f.read()
>>> print(text_english[:1000])
```
> **NOTE:**
> For all the code blocks in this file, you should open up interactive python and type in the code exactly as it appears here, and ensure that you get the correct output.
> You don't need to submit this output in anyway, but the actual coding tasks at the end are built off of this knowledge.

When the communiqué was first created,
there was no encoding scheme for representing Chinese language text electronically,
and so it was impossible to store the Chinese translation on a computer.

The PRC recognized this was a major problem,
and began developing their own encoding scheme for Chinese characters.
In 1980, they introduced the first standard for encoding Chinese characters called [GB2312](https://en.wikipedia.org/wiki/GB_2312) (ASCII was invented in 1963... China was nearly 20 years behind in computer tech.).
The file `shanghai_communique.chinese1` contains a Chinese translation of the communiqué stored in the GB2312 encoding.
Access it in python with the following code:
```
>>> f = open('shanghai_communique.chinese1', encoding='gb2312')
>>> text_gb2312 = f.read()
>>> print(text_gb2312[:1000])
```

### Encoding details

Recall that ASCII works by associating each English letter with a byte (a number between 0-255).
For example, the letter `A` is associated with the number 65 (which is 0x41 in hex), and we can verify that in python with the commands:
```
>>> 0x41
65
>>> b'\x41'.decode('ASCII')
'A'
```
The Chinese encoding GB2312 works in a similar way,
but it associates each Chinese character (called a Hanzi) with TWO bytes instead of just one.
For example, the Hanzi 友 means "friend" and is represented with the two bytes `\xd3` and `\xd1`:
```
>>> b'\xd3\xd1'.decode('gb2312')
'友'
```
With two bytes, any number between 0-65335 can be represented.
Although there are over 100,000 Chinese characters that have been created,
most of these characters are only used in rare historical contexts.
Modern Chinese text uses only about 3000 common characters,
and so GB2312's 2 byte encoding is enough for representing modern text.
<!--
You can find the full list of the 6675 Hanzi supported by the GB2312 encoding [on wiktionary](https://en.wiktionary.org/wiki/Appendix:Chinese_hanzi_by_GB_2312_quwei_code).
-->

### Alternative representations of Hanzi

Unfortunately, the GB2312 encoding is not the only way to represent Hanzi on the computer.
The GB2312 encoding scheme was designed specifically to use the [simplified Chinese characters](https://en.wikipedia.org/wiki/Simplified_Chinese_characters) characters in use in mainland-China,
but does not support the [traditional Chinese characters](https://en.wikipedia.org/wiki/Traditional_Chinese_characters) used in Taiwan.
Taiwanese programmers therefore independently created their own system for storing Hanzi called the [Big5 encoding](https://en.wikipedia.org/wiki/Big5).

<!--
For example, Taiwanese programmers did not want to have to use the GB2312 encoding scheme,
and so they developed their own standard called the [Big5 encoding](https://en.wikipedia.org/wiki/Big5) in 1984.

> **Historical Background:**
>
> The Taiwanese programmers didn't want to use the GB2312 standard for two reasons.
> The first was political.
> Taiwan officially did not recognize the PRC government of mainland China,
> and so for reasons of national pride wanted to develop their own standard.
> But Taiwanese programmers also had good technical reasons for not liking the GB2312 standard due to a language reform implemented in mainland China.
>
> When the Chinese Communist party took power in mainland China, less than 25% of the country knew how to read and write Chinese.
> So one of the first efforts of the Communist government was to improve literacy rates.
> Part of this effort was a reform in how Chinese characters worked, leading to the development of [simplified Chinese characters](https://en.wikipedia.org/wiki/Simplified_Chinese_characters).
> About 2000 characters have been modified under this system.
> The Taiwanese government, however, decided to continue using the old traditional Chinese characters.
> The existing GB2312 standard focused on supporting computers in mainland-China that use simplified Chinese characters,
> and therefore lacked many of the features needed for the traditional characters in use in Taiwan.
-->

Unfortunately,
Big5 is not compatible with GB2312,
and this makes it difficult for Taiwanese and mainland-Chinese people to communicate.
There are two problems that cause this incompatibility.

**The first encoding problem:**

Not all byte sequences are valid for every encoding scheme.
One of the most common Chinese characters is [人 (meaning "man")](https://en.wiktionary.org/wiki/%E4%BA%BA).
In the GB2312 encoding scheme, it has byte sequence `b'\xc8\xvb'`;
but this isn't a valid byte sequence in the Big5 encoding,
and so we get an error message when we try to decode it:
```
>>> b'\xc8\xcb'.decode('gb2312')
'人'
>>> b'\xc8\xcb'.decode('big5')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  UnicodeDecodeError: 'big5' codec can't decode byte 0xc8 in position 0: illegal multibyte sequence
```
If we try to load a file that contains one of these "bad byte sequences" with the wrong encoding,
Python will throw an error.
For example, the following python code tries to open our GB2312 encoded file in python using the Big5 encoding:
```
>>> f = open('shanghai_communique.chinese1', encoding='big5')
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  UnicodeDecodeError: 'big5' codec can't decode byte 0xc8 in position 11: illegal multibyte sequence
```
The Shanghai communique is something that Taiwanese diplomats definitely need to be able to read, however.
In order to transmit the document to them electronically, we need to re-encode it using the Big5 encoding.

The file `shanghai_communique.chinese2` contains the Shanghai communique encoded using Big5.
You can load it in python with the code
```
>>> f = open('shanghai_communique.chinese2', encoding='big5')
>>> text_big5 = f.read()
>>> print(text_big5[:1000])
```
Unfortunately, the Big5 encoding isn't able to handle the simplified Chinese characters in use by mainland China.
```
>>> b''
```

<!--
But if you try to open the Taiwanese Big5 encoded document with the mainland-Chinese GB2312 encoding, Python will also throw an error:
```
>>> f = open('shanghai_communique.chinese2', encoding='gb2312')
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  UnicodeDecodeError: 'gb2312' codec can't decode byte 0xa4 in position 7: illegal multibyte sequence
```
-->

**A possible solution:**

One idea to solving this problem is that we could try to automatically detect which encoding is being used in a file.
For example, we could try to first open a file in the GB2312 encoding,
and if that doesn't work, then we could open the file using the Big5 encoding.

The following Python function uses python's built-in `try`/`except` blocks to achieve this goal:
```
>>> def load_chinese_file(filename):
...     f = open(filename, 'br')
...     bs = f.read()
...     try:
...         text = bs.decode('gb2312')
...         print('gb2312')
...     except UnicodeDecodeError:
...         text = bs.decode('big5')
...         print('big5')
...     return text
...
```
Now we can load files in Chinese without specifying the encoding:
```
>>> text1 = load_chinese_file('shanghai_communique.chinese1')
>>> text2 = load_chinese_file('shanghai_communique.chinese2')
```

**The second problem:**

Unfortunately, the solution above doesn't always work because sometimes python won't give an error when we use the "wrong" encoding to load a file.
In particular, some byte sequences are valid in multiple encodings.
For example,
the GB2312 two byte sequence for 友 ("friend") is the same as the Big5 two byte sequence for 衭 (the front of a shirt):
```
>>> b'\xd3\xd1'.decode('gb2312')
'友'
>>> b'\xd3\xd1'.decode('big5')
'衭'
```
This can lead to unfortunate translation issues, especially in text that contains both English and Chinese.
For example, the byte sequence `b'I love \xd3\xd1'` can be interpreted either as "I love friends" or "I love shirts" depending on which encoding scheme is in use:
```
>>> b'I love \xd3\xd1'.decode('gb2312')
'I love 友'
>>> b'I love \xd3\xd1'.decode('big5')
'I love 衭'
```

### Modern Encodings and Unicode

Since the 1980s, many more encodings for Chinese characters have been developed.
The PRC extended the GB2312 encoding into [GBK](https://en.wikipedia.org/wiki/GBK_(character_encoding\)) in 1993 and [GB18030](https://en.wikipedia.org/wiki/GB_18030) in 2005.
The Taiwanese Big5 encoding has been extended into Big5+, Big5E, Big5-2003, CPD, and [HKSCS](https://en.wikipedia.org/wiki/Hong_Kong_Supplementary_Character_Set).
Microsoft created their own encoding called [Code Page 950](https://en.wikipedia.org/wiki/Code_page_950) and IBM created their own encoding called [CCSID](https://en.wikipedia.org/wiki/CCSID).
This great diversity of encodings made it extremely difficult for Chinese people to communicate with each other online.

The [Unicode Consortium](https://unicode.org/consortium/consort.html) was founded in 1991 to solve this problem (and other similar problems in other languages).
(The Consortium is primarily run by engineers at the major American tech companies; you can find a full list of the supporting companies at [the Unicode webpage](http://www.unicode.org/history/contributors.html).)
Their [mission](https://home.unicode.org/press/) is to

> Enable people around the world to use computers in any language.

This is an extremely difficult and politically-sensitive task for internationally used languages like Chinese.
Chinese characters are used not just in mainland China and Taiwan, but also in Malasia, Singapore, Hong Kong, Macau, Vietname, South Korea, North Korea, and Japan.
Representatives from all of these societies have been working together since 1991 on a process called [Han Unification](https://en.wikipedia.org/wiki/Han_unification) to figure out how to create a single system for representing Chinese characters that will work for anyone.
For the most part, they've been tremendously successful, [although Japanese speakers still commonly complain that their characters aren't quite right](https://heistak.github.io/your-code-displays-japanese-wrong/).

Unicode provides three standard methods for encoding characters that work in any language: UTF-8, UTF-16, and UTF-32.
The UTF stands for "Unicode Transformation Format" and the number stands for the number of bits required to store an English letter.
Since about the year 2000, most software has shipped using UTF-8 as the default encoding scheme, and now the vast majority of websites on the internet use UTF-8:

<img src=utf8.png />

Until 2017, the PRC government officially required that all documents in China be stored using the GB2312 encoding.
In 2017, this requirement was removed due to the success of Unicode and the UTF-8 encoding,
and the majority of Chinese websites have switched over to using UTF-8.
As of September 2022, [only 5.4% of websites served from mainland China use the GB2312 encoding](https://w3techs.com/technologies/segmentation/sl-cnter-/character_encoding),
with 94% using UTF-8.
The United Nations' [Minimum standards of multilingualism for United Nations websites](https://www.un.org/en/multilingualism-web-standards) explicitly requires that all websites use UTF-8.

Political battles over emoji [continue to this day](https://blog.emojipedia.org/apple-hides-taiwan-flag-in-hong-kong/).

## Part II

**The Scenario:**

For the rest of this lab, you will pretend to be an analyst at the US ["State Department"](https://www.quora.com/Why-does-the-CIA-famously-use-the-US-State-Department-as-cover-for-its-covert-officers?).
<!-- https://cryptome.org/dirty-work/spot-spook.htm -->
You've become aware that an internal source is leaking classified secrets about US nuclear submarines to the Brazilian government.
A [field agent](https://www.quora.com/What-does-a-CIA-field-agent-do) has intercepted these communications.
Unfortunately

'''
>>> f = open('secret_message.txt', 'rb')
>>> f.read()
b'Ant\xf4nio, encontre-me na embaixada \xe0 meia-noite de ter\xe7a-feira.\n'
'''
Antônio

António


> **Historical Note:**
>
> This scenario is not made up.
> In 2019, an engineer working for the US Navy contacted the Brazilian military and [attempted to sell plans for the US Virginia class nuclear submarines](https://www.nytimes.com/2022/03/15/us/politics/submarine-spy-brazil.html).
> (Brazil has a long history of attempting and failing to build their own nuclear submarines.)
> The Brazilians didn't want to participate in the scheme, and so forwarded the information to the CIA
