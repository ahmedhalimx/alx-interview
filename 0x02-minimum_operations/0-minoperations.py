#!/usr/bin/python3
"""
    0-minoperations
"""


def minOperations(n):
    """
    Gets fewest number of operations needed
    to get exactly n H characters
    """
    if (n < 2):
        return 0
    res, root = 0, 2
    while root <= n:
        if n % root == 0:
            res += root
            n = n / root
            root -= 1
        root += 1
    return res
