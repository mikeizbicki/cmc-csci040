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

    """
    text = text.replace('<b>','')
    text = text.replace('</b>','')
    text = text.replace('<i>','')
    text = text.replace('</i>','')
    """

    """
    # most straightforward is to use a for loop,
    # it's going to be a lot of code, and so a bit complicated for that reason
    new_text = ''
    inside_of_a_tag = False # boolean variables that control how a loop works, are often called flags
    for i in range(len(text)):
        #if text[i] is inside of an HTML tag:
        if text[i] == '<':
            inside_of_a_tag = True
        if text[i] == '>':
            inside_of_a_tag = False
        if not inside_of_a_tag and text[i] != '>': # how can inside_of_a_tag be False?
            new_text += text[i]
    """

    '''
    # have to repeat this multiple times
    #while there are html tags in text:
    #while '<' in text:
    for i in range(1000):
        if '<' in text:
            start_of_tag = text.find('<')
            end_of_tag = text.find('>')
            text = text[:start_of_tag] + text[end_of_tag+1:]
    '''

    #while there is still html to remove:
    if '<' in text:
        start_of_tag = text.find('<')
        end_of_tag = text.find('>')
        text = text[:start_of_tag] + text[end_of_tag+1:]

    return text

# two hard problems in computer science:
# 1. naming variables
# 2. cache invalidation
# 3. off by one errors

# replace is good if you know the exact substring to replace,
# but if you only know a pattern, then replace is bad.

# find function