def get_user_name():
    print('type your name:')
    name = input()
    while not len(name) > 8: # len(name) <= 8:
        print('your name is too short! Try again.')
        name = input()
    if len(name) > 8:
        print('you have a good name')
    
# a while loop can do anything a for loop can do
# but a for loop cannot do anything a while loop do

#get_user_name()

def is_perfect_square(n):
    '''
    Returns true if n is is the product of two integers.o

    If the sqrt(n) is an integer, then it's a perfect square.

    HINT: use a for loop

    Try every number less than n,
    see if that number times itself is equal to n

        >>> is_perfect_square(1)
        True
        >>> is_perfect_square(2)
        False
        >>> is_perfect_square(4)
        True
        >>> is_perfect_square(97)
        False
        >>> is_perfect_square(0)
        True
        >>> is_perfect_square(-144)
        False
    '''
    if n==0:
        return True
    if n==1:
        return True
    for i in range(n):
        if i*i == n:
            return True
    return False

# python subtlty: i starts at 0, go to n-1 for range(n)
for i in range(10):
    print('i=',i)