#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    initial_sum = sum(int(c) for c in n)
    
    # Total sum after repeating k times
    total = initial_sum * k

    # Compute digital root (super digit)
    def digital_root(x):
        if x == 0:
            return 0
        return 1 + (x - 1) % 9

    return digital_root(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
