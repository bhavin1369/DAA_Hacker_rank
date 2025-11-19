#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    freq = [0] * 100
    
    # Count occurrences of each number
    for num in arr:
        freq[num] += 1
    
    # Build sorted array from frequency counts
    sorted_arr = []
    for i in range(len(freq)):
        sorted_arr.extend([i] * freq[i])
    
    return sorted_arr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
