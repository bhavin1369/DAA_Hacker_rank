#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    if n == 1:
        return grid
    rows, cols = len(grid), len(grid[0])
    def detonate(current):
        new_grid = [['O'] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if current[r][c] == 'O':
                    new_grid[r][c] = '.'
                    if r > 0: new_grid[r-1][c] = '.'
                    if r < rows - 1: new_grid[r+1][c] = '.'
                    if c > 0: new_grid[r][c-1] = '.'
                    if c < cols - 1: new_grid[r][c+1] = '.'
        return new_grid
    grid = [list(row) for row in grid]
    if n % 2 == 0:
        return ["O" * cols for _ in range(rows)]
    first = detonate(grid)
    second = detonate(first)
    if n % 4 == 3:
        return ["".join(row) for row in first]
    else:
        return ["".join(row) for row in second]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    n = int(first_multiple_input[2])
    grid = []
    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)
    result = bomberMan(n, grid)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
