#!/usr/bin/python3

"""
pascal_triangle function definition
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the pascal triangle n
    """
    q = []
    if n <= 0:
        return q
    q = [[1]]
    for i in range(1, n):
        tmp = [1]
        for j in range(len(q[i - 1]) - 1):
            tmp.append(q[i - 1][j] + q[i - 1][j + 1])
        tmp.append(1)
        q.append(tmp)
    return q
