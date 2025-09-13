#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'introTutorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER V
#  2. INTEGER_ARRAY arr
#

def introTutorial(V, arr):
    # Since the array is sorted, we can use binary search
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == V:
            return mid
        elif arr[mid] < V:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Not found (though problem states it will be found)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    V = int(input().strip())
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = introTutorial(V, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
