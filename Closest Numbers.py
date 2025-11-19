#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort()
    
    # Initialize variables
    min_diff = float('inf')
    result = []
    
    # Find the minimum difference between consecutive elements
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff < min_diff:
            min_diff = diff
    
    # Collect all pairs with the minimum difference
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == min_diff:
            result.append(arr[i-1])
            result.append(arr[i])
    
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
