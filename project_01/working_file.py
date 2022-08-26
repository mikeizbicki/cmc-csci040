def compile_italic_star(line):
    '''
    Convert "*italic*" into "<i>italic</i>".

    HINT:
    Italics require carefully tracking the beginning and ending positions of the text to be replaced.
    This is similar to the `delete_HTML` function that we implemented in class.
    It's a tiny bit more complicated since we are not just deleting substrings from the text,
    but also adding replacement substrings.

    >>> compile_italic_star('*This is italic!* This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_star('*This is italic!*')
    '<i>This is italic!</i>'
    >>> compile_italic_star('This is *italic*!')
    'This is <i>italic</i>!'
    >>> compile_italic_star('This is not *italic!')
    'This is not *italic!'
    >>> compile_italic_star('*')
    '*'
    '''

    # step 1: get the indexes of the *
    start_index = None
    stop_index = None
    for i in range(len(line)):
        '''
        if start_index is None and line[i] == '*':
        #if not start_index and line[i] == '*':
            start_index = i
        else:
            if line[i] == '*':
                end_index = i
        '''

        if line[i] == '*':
            if start_index is None:
                start_index = i
            else:
                stop_index = i
    
    # don't try to implement everything at once;
    # always check your intermediate steps
    #print('start_index=', start_index)
    #print('stop_index=', stop_index)

    # step 2: use the indexes to create the new string
    # if start_index and stop_index
    if start_index is not None and stop_index is not None:
        line = line[:start_index] + '<i>' + line[start_index+1:stop_index] + '</i>' + line[stop_index+1:]

    return line

