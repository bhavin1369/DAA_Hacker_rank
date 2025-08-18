#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    result = []
    arr.sort()
    while arr:
        result.append(len(arr))  # count of sticks before cutting
        cut_length = arr[0]      # shortest stick
        arr = [x - cut_length for x in arr if x - cut_length > 0]  # cut & remove zeros
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
