#!/bin/python3

import os
import sys


def apply_shift(A, shift, n):
    B = [0] * n
    for i in range(n):
        B[i] = A[i] ^ A[(i + shift) % n]
    return B


def xorMatrix(m, first_row):
    n = len(first_row)

    # If m = 1, no transformation needed
    if m == 1:
        return first_row

    # Precompute 1, 2, 4, 8... shifts (for binary exponentiation)
    shifts = []
    x = 1
    while x < m:
        shifts.append(x)
        x <<= 1

    ans = first_row[:]
    target = m - 1  # we want T^(m-1)

    i = 0
    while target > 0:
        if target & 1:
            ans = apply_shift(ans, shifts[i], n)

        # Next power: shift doubles
        shifts[i] = (shifts[i] * 2) % n

        target >>= 1
        i += 1

    return ans


# ---------------------------
#   HACKERRANK MAIN FUNCTION
# ---------------------------
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n, m = map(int, input().split())
    first_row = list(map(int, input().rstrip().split()))
    result = xorMatrix(m, first_row)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
