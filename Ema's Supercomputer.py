#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    n = len(grid)
    m = len(grid[0])
    def get_pluses():
        pluses = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'G':
                    size = 0
                    while (i-size >= 0 and i+size < n and j-size >= 0 and j+size < m and
                           all(grid[i+dx*size][j+dy*size] == 'G'
                               for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])):
                        cells = set([(i, j)])
                        for k in range(1, size+1):
                            cells.update([(i+k, j), (i-k, j), (i, j+k), (i, j-k)])
                        pluses.append(cells)
                        size += 1
        return pluses
    pluses = get_pluses()
    max_area = 0
    for i in range(len(pluses)):
        for j in range(i+1, len(pluses)):
            if pluses[i].isdisjoint(pluses[j]):
                max_area = max(max_area, len(pluses[i]) * len(pluses[j]))
    return max_area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = twoPluses(grid)
    fptr.write(str(result) + '\n')
    fptr.close()
