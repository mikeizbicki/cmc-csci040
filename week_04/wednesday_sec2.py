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
    text = text.replace('<b>','')
    text = text.replace('</b>','')
    text = text.replace('<i>','')
    text = text.replace('</i>','')
    # .replace is good when you know exactly what to replace;
    # but it's bad when there's a pattern that you want to replace
    '''

    '''
    new_text = ''
    inside_tag = False # this will be true whenever text[i] is between < > and false if not between < >
    for i in range(len(text)):
        if text[i] == '<':
            inside_tag = True
        elif text[i] == '>':
            inside_tag = False
        else:
            if inside_tag == False:
                new_text += text[i]
    '''

    new_text = ''
    xs = text.split('<')
    # this doesn't work: xs.split('>')
    for x in xs:
        ys = x.split('>')
        new_text += ys[-1]
        print('ys=',ys)
    print('xs=',xs)

    return new_text