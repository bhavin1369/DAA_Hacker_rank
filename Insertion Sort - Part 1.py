#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Store the rightmost element
    e = arr[-1]
    i = n - 2  # Start from the second last element
    
    # Move left until we find the correct position for e
    while i >= 0 and arr[i] > e:
        # Shift element to the right
        arr[i + 1] = arr[i]
        # Print the array after shifting
        print(' '.join(map(str, arr)))
        i -= 1
    
    # Insert the stored element at the correct position
    arr[i + 1] = e
    # Print the final sorted array
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)