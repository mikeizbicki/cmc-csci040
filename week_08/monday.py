###############################################################################
# Number issues
###############################################################################



# what is binary?
# the number system of only 1s and 0s
# every number can be represented in binary with just 1s and 0s
# most fundamental number system
# each individual number (0 or 1) is called a bit
# we group collections of 8 bits into "bytes"

# file that is 10 megabytes ; mega=million, bytes=8 bits
# 100 gigabyte harddrive ; giga =  billion, 800 billion bits 

# octal 
# uses only the numbers 0-7
# almost never used; I've never had a reason to use

# hexidecimal
# uses the numbers 0-9 but also uses the "numbers" A-F
# provides a convenient way to represent binary
# a 2-digit hexadecimal number is stored with 8 bits = 1 byte
# almost always used when talking about how numbers are actually stored


# every letter has a number associated with it
# we're actually storing that number

ord # converts a letter into a number
chr # converts a number back into a letter

# sorting doesn't work "alphabetically", it works "ASCIIbetically"
# ASCII is the name of the system that associates English letters with numbers















###############################################################################
# Language issues
###############################################################################

# differences between languages

english = 'Computer programming is the best!!!'
english2 = 'Computer programming is the best！！！'

chinese = '计算机编程是最好的！！！'

korean = '컴퓨터 프로그래밍이 최고입니다 !!!'
컴퓨터 = 'this is a variable'

vietnamese = 'lập trình máy tính là tốt nhất !!!'

arabic = '!‏برمجة الكمبيوتر هي الأفضل!‏!‏'

# character weirdness

emoji1 = '😊'
emoji2 = '💩'

german = 'Strauß'

numbers = '৪৭' # In Tamil ৪ = 4 , ৭ = 7

url1 = 'https://www.BankOfAmerica.com'
url2 = 'https://www.ΒankΟfΑmerica.com'
url3 = 'https://www.BankOf​America.com'

greek = 'αβγδεζηθικλμνξοπρςστυφχψ'

empty = '​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​'

# character normalization = represent the characters in a standard way
# PRINCIPLE 1: you must normalize your strings if you want to compare them
# unicodedata.normalize('NKFD', variable_name)

accents_1 = 'á'
accents_2 = 'á'

accents_3 = '\xe1'
accents_3b = '\u00e1'
accents_3c = '\U000000e1'
accents_4 = 'a\u0301'

vietnamese_NFKD = 'lập trình máy tính là tốt nhất !!!'
vietnamese_NFKC = 'lập trình máy tính là tốt nhất !!!'

# encoding takes a string, and gives you the numbers associated with that string
# similar to the ord function, but works on entire strings, insted of just characters

pbuh = 'ﷺ'
basmala = '﷽' # see: https://en.wikipedia.org/wiki/Arabic_script_in_Unicode
