#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    Function that returns the perimeter
    of the island described in grid
    """
    def dfs(grid, i, j):
        if (
            i < 0 or i >= len(grid) or
            j < 0 or j >= len(grid[0]) or
            grid[i][j] == 0
        ):
            return 1  # perimeter
        if grid[i][j] == -1:  # already visited
            return 0

        grid[i][j] = -1  # mark as visited

        perimeter = 0
        perimeter += dfs(grid, i+1, j)  # down
        perimeter += dfs(grid, i-1, j)  # up
        perimeter += dfs(grid, i, j+1)  # right
        perimeter += dfs(grid, i, j-1)  # left

        return perimeter

    # find the first land cell to start the dfs
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(grid, i, j)

            # if no land cell is found, return 0
    return 0
