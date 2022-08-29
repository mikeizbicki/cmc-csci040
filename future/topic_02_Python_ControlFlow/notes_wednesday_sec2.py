'''
i = 0
total = 0
while i < 5:
    total = total + i

print('total=', total)
'''

'''
# CTRL+C is how you get out or "break" from an infinite loop

x = 4%5
print(x)
'''
























def is_even(n):
    '''
    Return True if n is even and False if n is odd.

    HINT: Use the modulus operator %

    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2000)
    True
    >>> is_even(-8)
    True
    >>> is_even(-9)
    False
    '''
    if n%2 == 0:
        return True
    else:
        return True

print( is_even(-9))
