def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''
    if b is None:
        start, stop = 0, a
    else:
        start, stop = a, b
    step = 1 if c is None else c
    if step == 0:
        raise ValueError('range() arg 3 must not be zero')
    i = start
    while (step > 0 and i < stop) or (step < 0 and i > stop):
        yield i
        i += step
