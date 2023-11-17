#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    """
    Check if it is safe to place a queen at a given position on the chessboard.

    Parameters:
        board (list[list[int]]): The current state of the chessboard.
        row (int): The row index where we want to place the queen.
        col (int): The column index where we want to place the queen.
        N (int): The size of the chessboard.

    Returns:
        bool: True if placing a queen is safe, False otherwise.
    """
    # Check if there is any queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False

    return True


def nqueens_util(board, row, N, solutions):
    """
    Recursive utility function to find all possible solutions for \
        the N Queens problem.

    Parameters:
        board (list[list[int]]): The current state of the chessboard.
        row (int): The current row being considered for queen placement.
        N (int): The size of the chessboard.
        solutions (list[list[int]]): List to store all found solutions.

    Returns:
        None
    """
    if row == N:
        # A solution is found when the queens are placed in all rows.
        solutions.append(
            [[i, j] for i in range(N) for j in range(N) if board[i][j] == 1])
    else:
        for col in range(N):
            if is_safe(board, row, col, N):
                # Place the queen and call the function recursively for the\
                # next row.
                board[row][col] = 1
                nqueens_util(board, row+1, N, solutions)
                # Backtrack and remove the queen from the current position.
                board[row][col] = 0


def nqueens(N):
    """
    Find and print all possible solutions for the N Queens problem.

    Parameters:
        N (int): The size of the chessboard.

    Returns:
        None
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
