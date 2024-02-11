#!/usr/bin/python3
"""
0-rotate_2d_matrix.py
"""


def rotate_2d_matrix(matrix):
    """
    rotate two dimension matrix 90 degrees clockwise
    """
    s = len(matrix)
    for i in range(int(s / 2)):
        y = (s - i - 1)
        for j in range(i, y):
            x = (s - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tmp
