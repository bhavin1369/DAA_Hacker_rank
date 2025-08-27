#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Dictionary to store the last seen index of each number
    last_seen = {}
    min_dist = float('inf')
    for i, num in enumerate(a):
        if num in last_seen:
            # Calculate distance
            dist = i - last_seen[num]
            min_dist = min(min_dist, dist)
        # Update last seen index
        last_seen[num] = i
    # If no pair found return -1
    return min_dist if min_dist != float('inf') else -1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)
    fptr.write(str(result) + '\n')
    fptr.close()
