#!/usr/bin/env python3
'''
This file downloads a webpage and performs a simple statistical analysis
to compute the most frequently used words on the webpage.
You can select which webpage is downloaded by changing the url variable.
Otherwise, you do not have to modify this file in any way.
The main part of the assignment consists of modifying the helper_functions.py file.
'''

import helper_functions
import extra_credit
url='https://en.wikipedia.org/wiki/Laika'

# download the html
html=helper_functions.download_html(url)
title=helper_functions.get_h1_tag(html)

# extract the meaningful text from the html
text=helper_functions.get_p_contents(html)
text=helper_functions.remove_newlines(text)
text=helper_functions.remove_punctuation(text)
text=helper_functions.remove_numbers(text)
text=helper_functions.remove_stop_words(text)

# calculate the top words
counts=helper_functions.count_words(text)
counts=helper_functions.get_top_k_words(counts,20)

# display the output
print('url:',url)
print('title:',title)
print('-'*20)
helper_functions.print_dictionary(counts)
extra_credit.generate_wordcloud(text)
