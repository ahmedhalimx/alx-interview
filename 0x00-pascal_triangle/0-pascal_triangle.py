#!/usr/bin/python3
"""
pascal_triangle() function definition
"""


def pascal_triangle(n):
    """
    returns a list of integers
    representing the pascal triangle n
    """
    pascal_list = []
    if n <= 0:
        return pascal_list
    pascal_list = [[1]]
    for i in range(1, n):
        tmp = [1]
        for j in range(len(pascal_list[i - 1]) - 1):
            tmp.append(pascal_list[i - 1][j] + pascal_list[i - 1][j + 1])
        tmp.append(1)
        pascal_list.append(tmp)
    return pascal_list
