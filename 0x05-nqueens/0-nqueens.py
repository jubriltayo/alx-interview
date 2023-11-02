#!/usr/bin/python3
"""A solution to N-Queens problem"""

from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    N = int(argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4,")
    exit(1)

cols = set()
pos_diagonal = set()
neg_diagonal = set()
board = []

# set up board position
for i in range(N):
    row = [0] * 2
    board.append(row)


def is_safe(row, col):
    """helper function to check if queen is safe to be in position"""
    if col in cols or (row + col) in pos_diagonal or \
       (row - col) in neg_diagonal:
        return False
    return True


def solve_n_queens(row):
    """strategically place queens on board recursively"""
    if row == N:
        print(board)
        return

    for col in range(N):
        if is_safe(row, col):
            cols.add(col)
            pos_diagonal.add(row + col)
            neg_diagonal.add(row - col)
            board[row] = [row, col]
            solve_n_queens(row + 1)

            # backtrack
            cols.remove(col)
            pos_diagonal.remove(row + col)
            neg_diagonal.remove(row - col)
            board[row] = [0, 0]


solve_n_queens(0)
