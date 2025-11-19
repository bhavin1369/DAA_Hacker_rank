#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'xoringNinja' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def xoringNinja(arr):
    MOD = 10**9 + 7
    OR = 0

    # OR of all elements
    for x in arr:
        OR |= x

    n = len(arr)

    # Multiply by 2^(n-1) % MOD
    result = (OR * pow(2, n-1, MOD)) % MOD

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        arr_count = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = xoringNinja(arr)
        fptr.write(str(result) + '\n')
    fptr.close()
