#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid

    grid: a list of list of integers

    return: perimeter of the island described in grid
    """

    perimeter = 0
    rows, cols = len(grid), len(grid[0]) if grid else 0

    # Loop through each row of the grid
    for i in range(rows):
        # Loop through each cell in the row
        for j in range(cols):
            if grid[i][j] == 1:  # If it's land
                perimeter += 4  # Count all four sides

                # Check if there's land in the adjacent cells
                # Subtract 1 for each adjacent land cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
