#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    def count_swaps(a):
        n = len(a)
        arr_pos = list(enumerate(a))
        arr_pos.sort(key=lambda x: x[1])   # Sort by value
        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or arr_pos[i][0] == i:
                continue
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr_pos[j][0]
                cycle_size += 1
            if cycle_size > 1:
                swaps += cycle_size - 1
        return swaps
    # Calculate swaps for ascending order
    asc = count_swaps(arr[:])
    # Calculate swaps for descending order
    desc = count_swaps(arr[::-1])
    return min(asc, desc)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = lilysHomework(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
