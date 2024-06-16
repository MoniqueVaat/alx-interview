#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Calculate the winner of the game
    """
    def calculate_winner(num, memo):
        if num < 2:
            return "Ben"

        if memo[num] is not None:
            return memo[num]

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                if calculate_winner(num // i, memo) == "Ben":
                    memo[num] = "Maria"
                    return "Maria"

        memo[num] = "Ben"
        return "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        memo = [None] * (n + 1)
        winner = calculate_winner(n, memo)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
