'''
x = 2 // 3
y = x * 4
z = y + 5
#print("z=", z)

print(5%14)

# x = (x//a)*a + x%a


# range(5) same as saying range(0,5) same as range(0,5,1)
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
        return False

print(is_even(4))
