# The DPRK and Unicode

[Unicode](https://unicode.org) is the standard method for representing multilingual text on computers,
and all major programming languages have easy-to-use libraries for working with Unicode text.
The Unicode Consortium is the organization responsible for maintaining the Unicode standard,
and their goal is to be an apolitical body that ensures that all languages/cultures are equally supported.

The Unicode standard, however, is biased in favor of the ROK-Korean dialect over the DPRK-Korean dialect.
This is due to a historical accident where the DPRK did not have the technical capacity to participate in the standards making process,
and so their needs were not considered.
This section first describes the technical problems with the Unicode standard for the DPRK,
then describes the historical causes.

## Technical Problems

The [Committee for Standardization of the DPRK (CSK)](https://www.iso.org/member/1657.html) submitted [a memo](https://unicode.org/wg2/docs/n2056.pdf)[](https://www.unicode.org/L2/L1999/99380.htm) to the Unicode Consortium in 1997 that lists three difficulties in working with Unicode in the DPRK.
None of these problems have been fixed in the last 25 years.
The problems are:

1. The official name of the Korean language script in Unicode is "Hangul" (see [Section 18.6 of the Unicode 14.0 standard](https://www.unicode.org/versions/Unicode14.0.0/)).
    Hangul is the ROK's name for their script,
    and the DPRK prefers the name "Choseongul".
    The DPRK suggested that the name "Korean characters" be adopted as a politically neutral term.

1. The DPRK and ROK use a [different sorting order for their alphabets](https://en.wikipedia.org/wiki/North%E2%80%93South_differences_in_the_Korean_language).
    The ROK order for consonants is

    ```
    ㄱ   ㄲ  ㄴ  ㄷ  ㄸ  ㄹ  ㅁ  ㅂ  ㅃ  ㅅ  ㅆ  ㅇ  ㅈ  ㅉ  ㅊ  ㅋ  ㅌ  ㅍ  ㅎ
    ```

    and the DPRK order is

    ```
    ㄱ   ㄴ  ㄷ  ㄹ  ㅁ  ㅂ  ㅅ  ㅈ  ㅊ  ㅋ  ㅌ  ㅍ  ㅎ  ㄲ  ㄸ  ㅃ  ㅆ  ㅉ  ㅇ
    ```
    For example, in the ROK, the word 까치 (magpie) comes alphabetically before the word 나비 (butterfly),
    but in the DPRK the word 나비 comes alphabetically before 까치.

    The Unicode standard orders Korean characters according to the ROK-ordering,
    and so by default all sorting done in any programming language will sort Korean words in the ROK-preferred way.
    A special extension called a [collation algorithm](https://cldr.unicode.org/index/cldr-spec/collation-guidelines) is required to sort according to the DPRK-ordering.

    As of 2022, the [current list of collation algorithms](https://github.com/unicode-org/cldr/tree/main/common/collation) does not have an entry for the DPRK-dialect of Korean,
    and so it is currently impossible in any programming language to sort text alphabetically accoding to the DPRK-ordering.

1. The DPRK internally uses the [KPS9566 character set](https://en.wikipedia.org/wiki/KPS_9566).
    This character set contains several characters that the Unicode Consortium does not want to support.
    For example, it contains political characters representing the Workers Party of Korea,
    and 4 distinct versions of the character 김
    (one for normal text, and one each for Kim Il Sung, Kim Jong Il, and Kim Jong Un).

    This lack of support for certain characters used by the DPRK prevents documents produced in the DPRK from being opened in tools like Microsoft Word,
    and even programming languages like Python and R cannot work with these documents.
    This lack of compatibility adds considerable friction to negotiations,
    since diplomats between the DPRK and the United States cannot easily exchange documents.
<!--
These Unicode problems make it difficult for diplomats to exchange documents with each other, providing a extra friction to negotiations.  The diplomats of course know nothing about encodings, they just know that they can't open the documents they need to open or get strange [mojibake](https://en.wikipedia.org/wiki/Mojibake).  Basically all the work of doing this encoding translation falls on the DPRK side.  They need technical people to do this, and they want to have technical representation in standardization bodies to avoid these situations in future standards.
-->

There is at least one more problem with the Unicode standard for the DPRK not listed above:

1. The current Unicode standard does not support transliteration of Korean into Latin characters using the [DPRK's preferred Romanization system](https://en.wikipedia.org/wiki/Romanization_of_Korean_(North)),
    and instead only supports the [McCune–Reischauer](https://en.wikipedia.org/wiki/McCune%E2%80%93Reischauer) system.
    Furthermore, transliterations into non-Latin alphabets are not supported at all, despite the importance of transliterating into Cyrillic.
    A [2018 UN report on romanization](https://unstats.un.org/Unsd/geoinfo/UNGEGN/docs/22-GEGN-Docs/wp/gegn22wp48.pdf) describes a good history of the many Romanization systems for Korean.

## Historical Basis

The ROK has been actively and publicly developing their systems for encoding Korean text since the earliest days of the internet.
KAIST first developed the KSC5601 encoding method in 1974,
and actively worked with companies like IBM and Microsoft,
and standards organizations in the US and Europe to ensure widespread support for this standard.
The ROK issued an official Request for Comments (RFC) on the encoding in 1993 via [RFC1557](https://datatracker.ietf.org/doc/html/rfc1557) to suggest that KSC5601 be the standard format for exchanging Korean emails.
When the Unicode Consortium was first founded in 1991,
ROK programmers were well positioned to contribute to the developing standard.
They had the detailed technical knowledge of developing many of their own internal encodings,
they had experience interacting with diverse technical committees,
and they had the English communication skills for communicating in the Unicode Consortium's working language.

In contrast, the DPRK has severely lagged the ROK in this area.
It's not known when the DPRK first developed their own Korean encoding,
but the DPRK's KPS9566 encoding was first published internationally in 1997 and officially registered with the Internaional Standards Organization (ISO) in 1998.
It wasn't until August 1999 that the DPRK began discussions for enabling Unicode compatibility.
The DPRK submitted an [official statement](https://unicode.org/wg2/docs/n2056.pdf)[](https://www.unicode.org/L2/L1999/99380.htm) to the Unicode Consortium outlining their difficulties adopting the Unicode standard (summarized above),
but since they entered this discussion 8 years after it began,
the technical decisions had already been made.
In order to not break backwards compatibility,
the Unicode Consortium issued a [statement](https://unicode.org/wg2/docs/n2392.pdf) that they could not implement the changes requested by the DPRK.

