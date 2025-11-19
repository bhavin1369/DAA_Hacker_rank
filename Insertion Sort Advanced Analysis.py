#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def insertionSort(arr):

    # Helper function to merge and count inversions
    def merge_count(left, right):
        i = j = inv = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inv += len(left) - i   # All remaining left elements are greater
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv

    # Recursive merge sort
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_merge = merge_count(left, right)
        return merged, inv_left + inv_right + inv_merge
    _, total_shifts = merge_sort(arr)
    return total_shifts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = insertionSort(arr)
        fptr.write(str(result) + '\n')
    fptr.close()
