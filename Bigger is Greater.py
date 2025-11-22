#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    arr = list(w)
    n = len(arr)

    # Step 1: find pivot (rightmost char that can be increased)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i < 0:
        return "no answer"   # already largest permutation

    # Step 2: find the smallest char > arr[i] to the right
    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1

    # Step 3: swap pivot with successor
    arr[i], arr[j] = arr[j], arr[i]

    # Step 4: reverse suffix for smallest possible increase
    arr[i + 1:] = reversed(arr[i + 1:])

    return "".join(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
