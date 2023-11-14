#!/usr/bin/python3
"""This module defines the function `rotate_2d_matrix`"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D Matrix 90 degrees clockwise"""
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for arr in matrix:
        arr.reverse()
