#!/usr/bin/python3

"""generates change
"""


def makeChange(coins, total):
    """A function that determines the
    fewest number of coins needed to
    meet a given amount total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0
    remaining_total = total

    for coin in coins:
        while remaining_total >= coin:
            remaining_total -= coin
            coin_count += 1

    if remaining_total == 0:
        return coin_count
    else:
        return -1
