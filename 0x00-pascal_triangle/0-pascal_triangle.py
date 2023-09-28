#!/usr/bin/python3
"""A module to display Pascal's triangle"""
def pascal_triangle(n):
    """
    Displays Pascal's triangle of n size

    Parameters:
        n (int): size of triangle
    
    Returns:
        triangle: list of list of triangle of size n 
    """
    triangle = []
    for i in range(n):
        row = []
        for elem in range(i + 1):
            if (elem == 0) or (elem == i):
                row.append(1)
            else:
                row.append(triangle[i - 1][elem - 1] + triangle[i - 1][elem])
        triangle.append(row)
    return triangle
