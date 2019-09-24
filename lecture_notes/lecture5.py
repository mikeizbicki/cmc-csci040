lst=['a','b','c','z']
print('lst=',lst)

for elem in lst:
    print('elem=',elem)

new_list=list(range(5))
total=0
for i in range(5):
    total=total+i
    print('i=',i,'total=',total)

def print_odd_numbers(n):
    '''
    prints all the odd numbers from 1 to n
    '''

    '''
    range function starts at 1 and goes to n
    and increments by 2 each time;
    therefore, it will print the odd numbers
    '''
    #for i in range(1,n,2):
    #    print('i=',i)

    '''
    range function loops over all values between
    1 and n, and the if statement checks if i
    is even, and does nothing
    '''
    #for i in range(1,n):
    #    if i%2==0:
    #        pass
    #    else:
    #        print('i=',i)

    '''
    range function is the same as before,
    but now the if statement is checking for odd
    numbers directly
    '''
    for i in range(1,n):
        if i%2==1:
            print('i=',i)

def factorial(n):
    result=1
    for i in range(1,n+1):
        print('i=',i,'result=',result)
        result=result*i
    return result
