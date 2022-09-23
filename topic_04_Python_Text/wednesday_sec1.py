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
    text = text.replace('<b>', '')
    text = text.replace('</b>', '')
    text = text.replace('<i>', '')
    text = text.replace('</i>', '')
    # .replace is good if there's an exact string that you want to replace;
    # but wew have a pattern to replace, so .replace doesn't work
    ''' 

    '''
    new_text = ''
    inside_tag = False # will be true whenever we're within < > ; False when we're outside of it
    for i in range(len(text)):
        # do something
        if text[i] == '<':
            inside_tag = True
        elif text[i] == '>':
            inside_tag = False
        elif inside_tag == False:
        #if inside_tag == False and text[i] != '>':
            new_text += text[i]

    return new_text
    '''

    new_text = ''
    lessthans = text.split('<')
    for lessthan in lessthans:
        greaterthans = lessthan.split('>')
        #for greaterthan in greaterthans:
        #    print('greaterthan=',greaterthan)
        new_text += greaterthans[-1]
        #print('lessthan=',lessthan)
    return new_text