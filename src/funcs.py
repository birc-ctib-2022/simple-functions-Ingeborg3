"""Exercises with simple functions"""

from math import sqrt

def prod(a, b, c):
    """
    Compute the product of three numbers.

    >>> prod(1, 2, 3)
    6
    """
    product = a*b*c
    return product

x = 3

def prod2(b):
    """
    Get a global a and write to a local c before computing prod(a, b, c)

    >>> prod2(42) # 3*42*2
    252
    """
    # Get value of global variable.
    a = x
    # Assign value to local variable.
    c = 2 
    product = a*b*c
    return product


def longest(x, y):
    """
    Returning the longest of two lists.

    >>> longest([1, 2, 3], [4, 5])
    [1, 2, 3]
    """
    max_length = max(len(x), len(y))
    if len(x) == max_length:
        return x
    else: 
        return y


def dist(p1, p2):
    """
    Compute the distance between p1 and p2.

    >>> dist((1,2), (3,4))
    3
    """
    x1, y1 = p1
    x2, y2 = p2
    
    dist = sqrt((x2-x1)**2+(y2-y1)**2)
    return round(dist)
