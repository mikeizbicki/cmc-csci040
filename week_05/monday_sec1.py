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
