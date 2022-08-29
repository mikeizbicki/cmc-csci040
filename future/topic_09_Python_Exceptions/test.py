
def foo():
    grades = {
        'alice': {'hw1': 99, 'hw2': 88},
        'bob': {'hw1': 82, 'hw2': 91},
    }

    output = 'grade=' + grades[hw3][alice]

    try:
        output = 'grade=' + grades[alice]['hw1']
    except TypeError:
        output = 'oops'
foo()
print('output=', output)

# There are no functions on the quiz, so you will never have to put a UnboundLocalError,
# The reasons we talk about it in class is because you will see it while you're programming

# UnboundLocalError and NameError are synonyms