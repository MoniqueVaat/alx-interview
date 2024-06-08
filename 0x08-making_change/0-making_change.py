#!/usr/bin/python3
"""
A function that makes changes from within the function
"""


def makeChange(coins, total):
    """
    Function that determines the
    fewest number of coins needed
    meet a given amount total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        # Use divmod to get the qoutient and remainder
        num_coins, remaining_total = divmod(total, coin)

        coin_count += num_coins
        total = remaining_total

    return coin_count if total == 0 else -1
