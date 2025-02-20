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

    '''
    # this works for the test cases, but it's not very general
    # not the best solution
    text = text.replace('<b>', '')
    text = text.replace('</b>', '')
    text = text.replace('<i>', '')
    text = text.replace('</i>', '')
    return text
    '''

    accumulator = ''
    inside_html_tag = False
    # will be true after a < and False after a >
    # will be true when we're in the html tag; and false when outside
    for c in text:
        if c == '<':
            inside_html_tag = True

        # if we are inside of an HTML tag:
        # if c != '>' and inside_html_tag == False:
        if inside_html_tag == False:
            accumulator += c
        
        if c == '>':
            inside_html_tag = False
        # do something with c
    return accumulator
