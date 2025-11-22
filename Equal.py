#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    mn = min(arr)
    best = float('inf')
    
    for base in range(mn, mn - 5, -1):
        ops = 0
        for x in arr:
            diff = x - base
            ops += diff // 5
            diff %= 5
            ops += diff // 2
            diff %= 2
            ops += diff
        best = min(best, ops)

    return best
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
