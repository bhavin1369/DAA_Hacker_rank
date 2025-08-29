#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Initial chocolates Bobby can buy
    chocolates = n // c
    wrappers = chocolates
    
    # Keep exchanging wrappers for chocolates
    while wrappers >= m:
        new_chocolates = wrappers // m
        chocolates += new_chocolates
        wrappers = wrappers % m + new_chocolates
    
    return chocolates


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        c = int(first_multiple_input[1])
        m = int(first_multiple_input[2])
        result = chocolateFeast(n, c, m)
        fptr.write(str(result) + '\n')
    fptr.close()
