#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the 'cavityMap' function below.
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
def cavityMap(grid):
    n = len(grid)
    if n < 3:
        return grid  # no interior cells
    original = [list(row) for row in grid]   # read-only reference
    result   = [list(row) for row in grid]   # we write X's here
    for i in range(1, n-1):
        for j in range(1, n-1):
            c = int(original[i][j])
            if (c > int(original[i-1][j]) and
                c > int(original[i+1][j]) and
                c > int(original[i][j-1]) and
                c > int(original[i][j+1])):
                result[i][j] = 'X'
    return [''.join(row) for row in result]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)
    result = cavityMap(grid)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
