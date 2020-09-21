#!/usr/bin/python3

'''
This script converts markdown documents into HTML documents.
'''

################################################################################
#
# The functions in this section are currently not implemented.
# Your main task in this homework is to implement them.
# If all of these functions pass their doctests,
# then the script overall will run successfully.
#
################################################################################


def compile_headers(line):
    '''
    This is the simplest function to implement,
    because headers only use hashtags at the beginning of the text.

    >>> compile_headers('# This is the main header')
    '<h1> This is the main header</h1>'
    >>> compile_headers('## This is a sub-header')
    '<h2> This is a sub-header</h2>'
    >>> compile_headers('### This is a sub-header')
    '<h3> This is a sub-header</h3>'
    >>> compile_headers('#### This is a sub-header')
    '<h4> This is a sub-header</h4>'
    >>> compile_headers('##### This is a sub-header')
    '<h5> This is a sub-header</h5>'
    >>> compile_headers('###### This is a sub-header')
    '<h6> This is a sub-header</h6>'
    >>> compile_headers('      # this is not a header')
    '      # this is not a header'
    '''
    return line


def compile_italic_star(line):
    '''
    Italics require carefully tracking the beginning and ending positions of the text to be replaced.

    >>> compile_italic_star('*This is italic!* This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_star('*This is italic!*')
    '<i>This is italic!</i>'
    >>> compile_italic_star('This is *italic*!')
    'This is <i>italic</i>!'
    >>> compile_italic_star('This is *italic*, and this is *italic*!')
    'This is <i>italic</i>, and this is <i>italic</i>!'
    >>> compile_italic_star('This is not *italic!')
    'This is not *italic!'
    >>> compile_italic_star('*')
    '*'
    '''
    return line


def compile_italic_underscore(line):
    '''
    This function is almost exactly the same as the star version,
    but it uses underscores instead.

    >>> compile_italic_underscore('_This is italic!_ This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('_This is italic!_')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is _italic_!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is _italic_, and this is _italic_!')
    'This is <i>italic</i>, and this is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    '''
    return line


def compile_strikethrough(line):
    '''
    The strikethrough and bold annotations are very similar to implement as the italic function.
    The difference is that there are two delimiting characters instead of one.
    This will require carefully thinking about the range of your for loop and all of your list indexing.

    >>> compile_strikethrough('~~This is strikethrough!~~ This is not strikethrough.')
    '<ins>This is strikethrough!</ins> This is not strikethrough.'
    >>> compile_strikethrough('~~This is strikethrough!~~')
    '<ins>This is strikethrough!</ins>'
    >>> compile_strikethrough('This is ~~strikethrough~~!')
    'This is <ins>strikethrough</ins>!'
    >>> compile_strikethrough('This is ~~strikethrough~~, and this is ~~strikethrough~~!')
    'This is <ins>strikethrough</ins>, and this is <ins>strikethrough</ins>!'
    >>> compile_strikethrough('This is not ~~strikethrough!')
    'This is not ~~strikethrough!'
    >>> compile_strikethrough('~~')
    '~~'
    '''
    return line


def compile_bold_stars(line):
    '''
    This function is similar to the strikethrough function.

    >>> compile_bold_stars('**This is bold!** This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_stars('**This is bold!**')
    '<b>This is bold!</b>'
    >>> compile_bold_stars('This is **bold**!')
    'This is <b>bold</b>!'
    >>> compile_bold_stars('This is **bold**, and this is **bold**!')
    'This is <b>bold</b>, and this is <b>bold</b>!'
    >>> compile_bold_stars('This is not **bold!')
    'This is not **bold!'
    >>> compile_bold_stars('**')
    '**'
    '''
    return line


def compile_bold_underscore(line):
    '''
    This function is similar to the strikethrough function.

    >>> compile_bold_underscore('__This is bold!__ This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_underscore('__This is bold!__')
    '<b>This is bold!</b>'
    >>> compile_bold_underscore('This is __bold__!')
    'This is <b>bold</b>!'
    >>> compile_bold_underscore('This is __bold__, and this is __bold__!')
    'This is <b>bold</b>, and this is <b>bold</b>!'
    >>> compile_bold_underscore('This is not __bold!')
    'This is not __bold!'
    >>> compile_bold_underscore('__')
    '__'
    '''
    return line


def compile_code(line):
    '''
    This function is like the italics function because inline code uses only a single character as a delimiter.
    It is more complex, however, because inline code blocks can contain valid HTML inside of them,
    but we do not want that HTML to get rendered as HTML.
    Therefore, we must convert the `<` and `>` signs into `&lt;` and `&gt;` respectively.

    >>> compile_code('You can use backticks like this (`1+2`) to include code in the middle of text.')
    'You can use backticks like this (<code>1+2</code>) to include code in the middle of text.'
    >>> compile_code('This is inline code: `1+2`')
    'This is inline code: <code>1+2</code>'
    >>> compile_code('`1+2`')
    '<code>1+2</code>'
    >>> compile_code('This example has html within the code: `<b>bold!</b>`')
    'This example has html within the code: <code>&lt;b&gt;bold!&lt;/b&gt;</code>'
    >>> compile_code('This example has a math formula in the  code: `1 + 2 < 4`')
    'This example has a math formula in the  code: <code>1 + 2 &lt; 4</code>'
    '''
    return line


def compile_links(line):
    '''
    The links and images are potentially more complicated because they have many types of delimeters: `[]()`.
    These delimiters are not symmetric, however, so we can more easily find the start and stop locations using the strings find function.

    >>> compile_links('Click on the [course webpage](https://github.com/mikeizbicki/cmc-csci040)!')
    'Click on the <a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>!'
    >>> compile_links('[course webpage](https://github.com/mikeizbicki/cmc-csci040)')
    '<a href="https://github.com/mikeizbicki/cmc-csci040">course webpage</a>'
    >>> compile_links('this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)')
    'this is wrong: [course webpage]    (https://github.com/mikeizbicki/cmc-csci040)'
    >>> compile_links('this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040')
    'this is wrong: [course webpage](https://github.com/mikeizbicki/cmc-csci040'
    '''
    return line


def compile_images(line):
    '''
    Images is almost exactly the same as links,
    except that images have a leading `!`.

    >>> compile_images('[Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    '[Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)'
    >>> compile_images('![Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    '<img src="https://avatars1.githubusercontent.com/u/1052630?v=2&s=460" alt="Mike Izbicki" />'
    >>> compile_images('This is an image of Mike Izbicki: ![Mike Izbicki](https://avatars1.githubusercontent.com/u/1052630?v=2&s=460)')
    'This is an image of Mike Izbicki: <img src="https://avatars1.githubusercontent.com/u/1052630?v=2&s=460" alt="Mike Izbicki" />'
    '''
    return line


################################################################################
#
# You only need to modify the code in this section if you are completing the extra credit.
#
################################################################################


def compile_lines(text):
    '''
    This function calls all of the functions you created above to convert the full markdown file into HTML.
    '''
    lines = text.split('\n')
    new_lines = []
    in_paragraph = False
    for line in lines:
        line = line.strip()
        if line=='':
            if in_paragraph:
                line='</p>'
        else:
            if line[0] != '#' and not in_paragraph:
                in_paragraph = True
                line = '<p>'+line
            line = compile_headers(line)
            line = compile_strikethrough(line)
            line = compile_bold_stars(line)
            line = compile_bold_underscore(line)
            line = compile_italic_star(line)
            line = compile_italic_underscore(line)
            line = compile_code(line)
            line = compile_images(line)
            line = compile_links(line)
        new_lines.append(line)
    new_text = '\n'.join(new_lines)
    return new_text


################################################################################
#
# This section does not need to be modified at all.
#
################################################################################

if __name__=='__main__':

    # process command line arguments
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    parser.add_argument('--add_css', action='store_true')
    args = parser.parse_args()

    # validate that the input file is a markdown file
    if args.input_file[-3:] != '.md':
        print('ERROR: the --input_file does not end in .md')
        sys.exit(1)

    # load the input file
    with open(args.input_file, 'r') as f:
        text = f.read()

    # generate the HTML from the Markdown
    html = '''
<html>
<head>
    <style>
    ins { text-decoration: line-through; }
    </style>
    '''
    if args.add_css:
        html += '''
<link rel="stylesheet" href="https://izbicki.me/css/code.css" />
<link rel="stylesheet" href="https://izbicki.me/css/default.css" />
        '''
    html+='''
</head>
<body>
    '''+compile_lines(text)+'''
</body>
</html>
    '''

    # write the output file
    with open(args.input_file[:-2]+'html', 'w') as f:
        f.write(html)
