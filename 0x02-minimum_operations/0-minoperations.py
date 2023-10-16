#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates minimal operations needed to \
        achieve exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    div = 2

    while n > 1:
        if n % div == 0:
            operations += div
            n //= div
        else:
            div += 1

    return operations
