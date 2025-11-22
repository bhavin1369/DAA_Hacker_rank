#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    n = len(arr)
    sorted_arr = sorted(arr)

    # If already sorted
    if arr == sorted_arr:
        print("yes")
        return

    # Find indices where arr differs from sorted_arr
    diff = [i for i in range(n) if arr[i] != sorted_arr[i]]

    # If exactly two elements are out of place -> simple swap case
    if len(diff) == 2:
        print("yes")
        # +1 for 1-based index
        print("swap", diff[0] + 1, diff[1] + 1)
        return

    # Otherwise try reverse operation
    L = diff[0]
    R = diff[-1]

    # Reverse the segment and check if sorted
    segment_reversed = arr[:L] + arr[L:R+1][::-1] + arr[R+1:]
    
    if segment_reversed == sorted_arr:
        print("yes")
        print("reverse", L + 1, R + 1)
        return

    # If neither swap nor reverse works
    print("no")
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)

