#!/usr/bin/python3
'''island perimeter'''


def island_perimeter(grid):
    '''island perimeter func
    returns the perimeter of the island'''
    perimeter = 0

    for row in grid:
        for cell in row:
            if cell == 1:
                perimeter += 4

                c_index = row.index(cell)
                r_index = grid.index(row)
                if c_index > 0 and row[c_index - 1] == 1:
                    perimeter -= 1
                if c_index < len(row) - 1 and row[c_index + 1] == 1:
                    perimeter -= 1
                if r_index > 0 and grid[r_index - 1][c_index] == 1:
                    perimeter -= 1
                if r_index < len(grid) - 1 and grid[r_index + 1][c_index] == 1:
                    perimeter -= 1

    return perimeter 
