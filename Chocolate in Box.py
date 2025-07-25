#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateInBox' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def chocolateInBox(arr):
    s = 0
    for a in arr:
        s ^= a
        
    if s == 0:
        return 0
        
    count = 0
    for a in arr:
        x = s ^ a
        if x < a:
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = chocolateInBox(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
