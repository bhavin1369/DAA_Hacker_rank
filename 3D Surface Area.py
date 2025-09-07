#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    H = len(A)
    W = len(A[0])
    area = 0
    
    for i in range(H):
        for j in range(W):
            if A[i][j] > 0:
                # Top and bottom
                area += 2  
                # Four sides
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < H and 0 <= nj < W:
                        area += max(A[i][j] - A[ni][nj], 0)
                    else:
                        area += A[i][j]
    return area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    H = int(first_multiple_input[0])
    W = int(first_multiple_input[1])
    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))
    result = surfaceArea(A)
    fptr.write(str(result) + '\n')
    fptr.close()
