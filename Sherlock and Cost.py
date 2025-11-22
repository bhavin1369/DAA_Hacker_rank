#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(B):
    low = 0
    high = 0

    for i in range(1, len(B)):
        low_new = max(
            low,                       # |1 - 1| = 0
            high + abs(1 - B[i-1])     # previous was high
        )

        high_new = max(
            low + abs(B[i] - 1),       # previous was low
            high + abs(B[i] - B[i-1])  # previous was high
        )

        low, high = low_new, high_new

    return max(low, high)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
