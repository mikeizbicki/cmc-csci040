#!/bin/python

'''
Lab instructions: 
Complete each function below so that all doctests pass.
You can run the doctests with the command

$ python3 -m doctest --verbose lab.py

Once all doctests pass, upload the output of the above command to sakai.
'''


def rot13(text):
    '''
    [ROT13](https://en.wikipedia.org/wiki/ROT13) stands for "ROTate characters by 13".
    It is a commonly used encryption scheme where each character is replaced by the character 13 positions above/below it.
    For example, the letter 'a' gets replaced by 'n',
    and 'n' gets replaced by 'a'.
    This is of course not a very good encryption scheme because it's easy for anyone to decrypt,
    but it's useful for hiding information from the muggles who can't program.
    It's basically like the [pig latin](https://en.wikipedia.org/wiki/Pig_Latin) of programming.

    HINT:
    Use the `ord` function to convert each character to a number;
    do your math on that number;
    then use `chr` to convert bach to a string.

    >>> rot13('python is awesome')
    'clguba vf njrfbzr'
    >>> rot13('clguba vf njrfbzr')
    'python is awesome'
    >>> rot13('PYTHON')
    'CLGUBA'
    >>> rot13(rot13('python is awesome!!'))
    'python is awesome!!'
    >>> rot13('Crescit cum commercio civitas.')
    'Perfpvg phz pbzzrepvb pvivgnf.'
    >>> rot13('Pynerzbag ZpXraan Pbyyrtr’f zvffvba vf "gb rqhpngr vgf fghqragf sbe gubhtugshy naq cebqhpgvir yvirf naq erfcbafvoyr yrnqrefuvc va ohfvarff, tbireazrag, naq gur cebsrffvbaf, naq gb fhccbeg snphygl naq fghqrag fpubynefuvc gung pbagevohgr gb vagryyrpghny ivgnyvgl naq gur haqrefgnaqvat bs choyvp cbyvpl vffhrf."')
    'Claremont McKenna College’s mission is "to educate its students for thoughtful and productive lives and responsible leadership in business, government, and the professions, and to support faculty and student scholarship that contribute to intellectual vitality and the understanding of public policy issues."'

    HINT:
    Use the accumulator pattern.
    Loop over each character in the string, and if it is not a letter, then just add it to the accumulator.
    If it is a letter, then do a ROT13 transformation using the `ord` and `chr` functions and some simple math.
    You know something is a capital letter because it is >= 'A' and <= 'Z';
    similarly, you know something is a lowercase letter because it is >= 'a' and <= 'z'.
    '''


def greekify(text):
    '''
    Transliterating is the process of converting between two different alphabets at a character-by-character level.
    Unlike translation, transliterating does not take into account the semantic meaning of words.
    This function transliterates between the Greek and Latin alphabets.

    >>> greekify('python is awesome')
    'πψτηον ισ αωεσομε'
    >>> greekify('PyThoN Is AwEsOmE!!!')
    'ΠψΤηοΝ Ισ ΑωΕσΟμΕ!!!'
    >>> greekify('ΠψΤηοΝ Ισ ΑωΕσΟμΕ!!!')
    'PyThoN Is AwEsOmE!!!'
    >>> greekify('CSCI040')
    'CΣCΙ040'
    >>> greekify('Crescit cum commercio civitas.')
    'Cρεσcιτ cυμ cομμερcιο cιvιτασ.'
    >>> greekify('Claremont McKenna College’s mission is "to educate its students for thoughtful and productive lives and responsible leadership in business, government, and the professions, and to support faculty and student scholarship that contribute to intellectual vitality and the understanding of public policy issues."')
    'Cλαρεμοντ ΜcΚεννα Cολλεγε’σ μισσιον ισ "το εδυcατε ιτσ στυδεντσ φορ τηουγητφυλ ανδ προδυcτιvε λιvεσ ανδ ρεσπονσιβλε λεαδερσηιπ ιν βυσινεσσ, γοvερνμεντ, ανδ τηε προφεσσιονσ, ανδ το συππορτ φαcυλτψ ανδ στυδεντ σcηολαρσηιπ τηατ cοντριβυτε το ιντελλεcτυαλ vιταλιτψ ανδ τηε υνδερστανδινγ οφ πυβλιc πολιcψ ισσυεσ."'

    NOTE:
    The `greek_alphabet` and `latin_alphabet` variables provide a mapping between the greek and latin alphabets.
    For example, we know that 'Δ' corresponds to 'D' because the occur at the same position in both strings.

    HINT:
    You should loop over the input text using the accumulator pattern.
    If the next character is at position i in `greek_alphabet`,
    then add the character at position i in the `latin_alphabet` to the accumulator (and vice versa).
    If the character is not in either string,
    then just add that character to the accumulator.
    '''
    greek_alphabet = 'ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσςΤτΥυΦφΧχΨψΩω'
    latin_alphabet = 'AaBbGgDdEeZzHhJjIiKkLlMmNnXxOoPpRrSssTtUuFfQqYyWw'


def character_equality(x, y):
    '''
    Recall that in python, equality of strings is performed at the level of Unicode code points (i.e. characters) and no normalization is done.
    You can implement this function with just the ordinary `==` comparison operator and no normalization.
    The main purpose of this function is to contrast with the `grapheme_equality` function that comes next.

    NOTE:
    Your operating system probably automatically converts the contents of your clipboard to NFC form copy/pasting.
    Therefore, if you copy/pasted this file, the test cases likely will not work.
    You must download this file instead.

    >>> character_equality('A', 'a')
    False
    >>> character_equality('A', 'A')
    True
    >>> character_equality('A', 'Α')
    False
    >>> character_equality('Á', 'A\u0301')
    True
    >>> character_equality('Á', 'Á')
    False
    >>> 'Á' == 'Á'
    False
    >>> character_equality('lập trình máy tính là tốt nhất !!!', 'lập trình máy tính là tốt nhất !!!')
    False
    '''


def grapheme_equality(x, y):
    '''
    This is like the previous function, but equality should be performed at the "grapheme level" instead of the "character level".
    This will require you to normalize the strings before you compare them.
    Notice that the test cases are all the same,
    but the results are different.

    >>> grapheme_equality('A', 'a')
    False
    >>> grapheme_equality('A', 'A')
    True
    >>> grapheme_equality('A', 'Α')
    False
    >>> grapheme_equality('Á', 'A\u0301')
    True
    >>> grapheme_equality('Á', 'Á')
    True
    >>> 'Á' == 'Á'
    False
    >>> grapheme_equality('lập trình máy tính là tốt nhất !!!', 'lập trình máy tính là tốt nhất !!!')
    True
    '''
