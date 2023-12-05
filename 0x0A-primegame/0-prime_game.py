#!/usr/bin/python3
""" This module defines the function `isWinner` """


def isWinner(x, nums):
    """ Returns the winner """
    p1 = 0
    p2 = 0
    for round in range(x):
        n = nums[round]
        prime_counter = 0
        for j in range(1, n + 1):
            if isPrime(j):
                prime_counter += 1

        if prime_counter % 2 == 0:
            p1 += 1
        else:
            p2 += 1

        if p1 == p2:
            return None
        elif p1 > p2:
            return 'Maria'
        else:
            return 'Ben'


def isPrime(n):
    """Checks if a number is Prime or not"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i) == 0:
            return False
    return True
