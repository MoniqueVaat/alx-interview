def island_perimeter(grid):
    """returns the perimeter of the island described in grid

    grid: a list of list of integers

    return: perimeter of the island described in grid
    """

    perimeter = 0

    # Loop through each row and cell in the grid
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 1:  # If it's land
                perimeter += 4  # Count all four sides

                # Check if there's land in the adjacent cells
                # Subtract 1 for each adjacent land cell
                if j > 0 and row[j - 1] == 1:
                    perimeter -= 1
                if j < len(row) - 1 and row[j + 1] == 1:
                    perimeter -= 1
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1

    return perimeter
