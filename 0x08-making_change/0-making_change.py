#!/usr/bin/python3
"""This module defines the `makeChange` function"""


def makeChange(coins, total):
    """returns the fewest number of coins"""
    coins = sorted(coins, reverse=True)
    coins_count = 0
    for coin in coins:
        if total == 0:
            break
        coins_count += total // coin
        total = total % coin
    if total == 0:
        return coins_count
    return -1
