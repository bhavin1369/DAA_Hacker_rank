#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def larrysArray(A):
    """
    Determines if an array can be sorted using a 3-element rotation.

    The core insight is that a 3-element rotation (e.g., ABC -> BCA) is an
    even permutation, meaning it's equivalent to two swaps. Applying an
    even permutation never changes the parity of the number of inversions
    in the array.

    A sorted array has 0 inversions (an even number). Therefore, the initial
    array can only be sorted if it also has an even number of inversions.

    Args:
        A: A list of integers, which is a permutation of numbers from 1 to n.

    Returns:
        A string, either "YES" or "NO".
    """
    inversions = 0
    n = len(A)

    # Count the total number of inversions in the array.
    # An inversion is any pair of indices (i, j) such that i < j and A[i] > A[j].
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                inversions += 1

    # If the number of inversions is even, it's possible to sort.
    # Otherwise, it's impossible.
    if inversions % 2 == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        A = list(map(int, input().rstrip().split()))
        result = larrysArray(A)
        fptr.write(result + '\n')
    fptr.close()
