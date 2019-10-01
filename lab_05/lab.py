def filter_even(lst):
    '''
    returns a list with all the even elements removed

        >>> filter_even([1,3,5])
        [1, 3, 5]
        >>> filter_even([2,4,6])
        []
        >>> filter_even([4,5,6,7])
        [5, 7]
        >>> filter_even([20,13,4,16,8,19,10])
        [13, 19]
    '''

def list_to_string(lst):
    '''
    This function takes a list as input and returns a string that contains all the elements of the list separated by commas with the word 'and' between the second to last and last items.

        >>> list_to_string(['apples', 'bananas', 'tofu', 'cats'])
        'apples, bananas, tofu, and cats'
        >>> list_to_string([1,2,3])
        '1, 2, and 3'
        >>> list_to_string([True,False])
        'True, and False'
        >>> list_to_string(['test'])
        'test'
    '''

def bigger_than_10(lst):
    '''
    returns the number of elements in the list bigger than 10

        >>> bigger_than_10([])
        0
        >>> bigger_than_10([10])
        0
        >>> bigger_than_10([11,1,12,2,13,3,14,4,15,5])
        5
        >>> bigger_than_10([4,5,6,11])
        1
    '''

def second_largest(lst):
    '''
    returns the second largest element in a list,
    if the list has less than 2 elements, returns None

        >>> second_largest([1,2,3])
        2
        >>> second_largest([99,-56,80,100,90])
        99
        >>> second_largest(list(range(0,100)))
        98
        >>> second_largest([10])
        None
        >>> second_largest([])
        None
    '''

def filter_flatten(lst_of_lst):
    '''
    This function takes as input a list of lists and returns a single list.
    The first element of the returned list is equal to the first element in the first nested list,
    the second element of the returned list is equal to the second element in the second nested list,
    and in general the n-th element of the returned list is equal to the n-th element in the n-th nested list.

        >>> filter_flatten([[True,False],[False,True]])
        [True, True]
        >>> filter_flatten([[1,2,3],[4,5,6],[7,8,9]])
        [1, 5, 9]
        >>> filter_flatten([['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']])
        ['a', 'f', 'k', 'p']
        >>> filter_flatten([[10]])
        [10]
    '''

def last_three(lst):
    '''
    returns a list containing the last three elements of the input list;
    if the list contains three or fewer elements, then return the entire list

    HINT: use list slices with negative indices

        >>> last_three([0,1,2,3,4,5,6,7,8,9])
        [7, 8, 9]
        >>> last_three(['a','b','c','d'])
        ['b', 'c', 'd']
        >>> last_three([0,1])
        [0, 1]
    '''


# DO NOT MODIFY BELOW THIS LINE
import doctest
doctest.testmod(verbose=True)
