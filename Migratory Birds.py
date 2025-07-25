#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    # Initialize a dictionary to count frequencies of each bird type
    frequency = defaultdict(int)
    for bird in arr:
        frequency[bird] += 1
    
    max_frequency = max(frequency.values())
    # Collect all bird types with the maximum frequency
    candidates = [bird for bird in frequency if frequency[bird] == max_frequency]
    # Return the smallest bird type among the candidates
    return min(candidates)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
