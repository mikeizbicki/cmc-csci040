def compile_italic_underscore(line):
    '''
    Convert "_italic_" into "<i>italic</i>".

    HINT:
    This function is almost exactly the same as `compile_italic_star`.

    >>> compile_italic_underscore('_This is italic!_ This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('_This is italic!_')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is _italic_!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    '''

    newline = ''
    is_italic = False
    for x in line:
        if x == '_' and not is_italic:
            newline = newline + '<i>'
            is_italic = True
        elif x == '_' and is_italic:
            newline = newline + '</i>'
        else:
            newline = newline + x
    return newline

