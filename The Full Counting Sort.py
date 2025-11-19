#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    
    n = len(arr)
    
    # Find the maximum integer value to determine the size of our counting array
    max_val = 0
    for i in range(n):
        num = int(arr[i][0])
        if num > max_val:
            max_val = num
    
    # Create a counting array of empty lists (for stability)
    count = [[] for _ in range(max_val + 1)]
    
    # First pass: process first half and replace with '-'
    for i in range(n):
        num = int(arr[i][0])
        string_val = arr[i][1]
        
        # Replace strings in first half with '-'
        if i < n // 2:
            count[num].append('-')
        else:
            count[num].append(string_val)
    
    # Build the sorted result
    result = []
    for i in range(max_val + 1):
        result.extend(count[i])
    
    # Print the sorted strings separated by spaces
    print(' '.join(result))

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())
    countSort(arr)
