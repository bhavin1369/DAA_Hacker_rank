#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    left_to_right = 0
    right_to_left = 0
    for i in range(n):
        # Sum elements from top-left to bottom-right
        left_to_right += arr[i][i]
        # Sum elements from top-right to bottom-left
        right_to_left += arr[i][n-1-i]
    return abs(left_to_right - right_to_left)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
