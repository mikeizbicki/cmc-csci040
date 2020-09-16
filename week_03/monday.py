for i in [1, 5,6,7, 23,985]:
    print('i=',i)

names = [
    'mike',
    'michael',
    'mikey',
    ]
for name in names:
    print('name=',name)

# indexing and slicing

names[0] # index

names[0:2] # slice

def filter_odd(lst):
    '''
    returns a list with all the odd elements removed
    >>> filter_odd([1,2,3,4])
    [2, 4]
    '''
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens
