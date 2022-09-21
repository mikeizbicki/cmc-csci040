def largest(xs):
    '''
    Return the largest element in a list.

    >>> largest([1,2,3])
    3
    >>> largest([99,-56,80,100,90])
    100
    >>> largest(list(range(0,100)))
    99
    >>> largest([10])
    10
    >>> largest([])
    '''
    if len(xs) == 0:
        return None
    xs.sort()
    return xs[-1]


def largest3(xs):
    '''
    Return the largest 3 elements in a list in sorted order.

    >>> largest3([1,2,3])
    [1, 2, 3]
    >>> largest3([99,-56,80,100,90])
    [90, 99, 100]
    >>> largest3(list(range(0,100)))
    [97, 98, 99]
    >>> largest3([10])
    [10]
    >>> largest3([])
    []
    '''
    xs.sort()
    return xs[-3:]


def filter_odd(xs):
    '''
    Return a list with all the odd elements removed.

    HINT:
    Use the accumulator pattern with a for loop.

    >>> filter_odd([2,4,6])
    [2, 4, 6]
    >>> filter_odd([1,3,5])
    []
    >>> filter_odd([4,5,6,7])
    [4, 6]
    >>> filter_odd([20,13,4,16,8,19,10])
    [20, 4, 16, 8, 10]
    '''
    accumulator = []
    for x in xs:
        if x%2 == 0:
            accumulator.append(x)
    return accumulator


def nested_filter_odd(xss):
    '''
    Convert a list of lists into a single list that contains only the even elements.

    >>> nested_filter_odd([[2, 4, 5], [1, 3, 6]])
    [2, 4, 6]
    >>> nested_filter_odd([[1, 3, 6]])
    [6]
    >>> nested_filter_odd([[4, 5], [6, 7]])
    [4, 6]
    >>> nested_filter_odd([[20],[13,4,16,8,19],[10], [15, 13, 1]])
    [20, 4, 16, 8, 10]
    '''
    accumulator = []
    for xs in xss:
        for x in xs:
            if x%2 == 0:
                accumulator.append(x)
    return accumulator
