#!/usr/bin/python3
"""
Module to find the winner of a prime game
"""


def isWinner(x, nums):
    """
    Determines the winner of prime game
    """

    p1_wins = 0
    p2_wins = 0
    p1 = 'Maria'
    p2 = 'Ben'
    rounds = 0
    # for i in nums:
    while rounds < x:
        i = nums[rounds]
        no_prime = 0

        for j in range(1, i + 1):
            if is_prime(j):
                no_prime = no_prime + 1

        if no_prime % 2 == 0:
            p2_wins = p2_wins + 1
        else:
            p1_wins = p1_wins + 1

        rounds = rounds + 1

    if p1_wins == p2_wins:
        return None
    elif p1_wins > p2_wins:
        return p1
    else:
        return p2


def is_prime(num):
    """
    Checks if number is prime
    """

    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True