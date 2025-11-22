#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    layers = min(m, n) // 2

    result = [[0]*n for _ in range(m)]

    for layer in range(layers):
        top = layer
        left = layer
        bottom = m - layer - 1
        right = n - layer - 1

        ring = []

        # Top row
        for j in range(left, right + 1):
            ring.append(matrix[top][j])

        # Right column
        for i in range(top + 1, bottom):
            ring.append(matrix[i][right])

        # Bottom row
        for j in range(right, left - 1, -1):
            ring.append(matrix[bottom][j])

        # Left column
        for i in range(bottom - 1, top, -1):
            ring.append(matrix[i][left])

        L = len(ring)
        rot = r % L
        rotated = ring[rot:] + ring[:rot]

        idx = 0

        # Put rotated values back

        # Top row
        for j in range(left, right + 1):
            result[top][j] = rotated[idx]
            idx += 1

        # Right column
        for i in range(top + 1, bottom):
            result[i][right] = rotated[idx]
            idx += 1

        # Bottom row
        for j in range(right, left - 1, -1):
            result[bottom][j] = rotated[idx]
            idx += 1

        # Left column
        for i in range(bottom - 1, top, -1):
            result[i][left] = rotated[idx]
            idx += 1

    # Print output
    for row in result:
        print(*row)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
