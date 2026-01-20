def delete_HTML(text):
    '''
    This function removes all HTML tags from the input text.

    >>> delete_HTML('This is <b>bold</b>!')
    'This is bold!'
    >>> delete_HTML('This is <i>italic</i>!')
    'This is italic!'
    >>> delete_HTML('This is <strong>italic</strong> and this is <ins>strikethrough</ins>!')
    'This is italic and this is strikethrough!'
    '''

    # this is *a* strategy, but it's not a *good* strategy
    # why?
    # so I could pass the test cases by just "hard coding"
    # solutions for the three examples above
    # but then my code won't work for other html tags
    # like <p>, <ol>, <li>, <table> ....
    # >1000 html tags in use
    # more are created every day
    '''
    text = text.replace('<b>', '')
    text = text.replace('</b>', '')
    '''

    # let's write a solution that works for all html tags
    # we need to delete all text that appears between < >
    accumulator = ''
    between_brackets = False
    for c in text:
        if c == '<':
            between_brackets = True
        if between_brackets == False:
            accumulator += c
        if c == '>':
            between_brackets = False
        #if c != '<': and c != '>':
        #    accumulator += c

    return accumulator