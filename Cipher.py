#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. STRING s
#

def cipher(k, s):
    n = len(s)
    s = list(map(int, s))   # convert to integers

    b = [0] * n
    window_xor = 0

    for i in range(n):
        # XOR of current s[i] with accumulated window XOR gives b[i]
        b[i] = s[i] ^ window_xor

        # Add new bit to window
        window_xor ^= b[i]

        # Remove bit falling out of window
        if i >= k - 1:
            window_xor ^= b[i - (k - 1)]

    return ''.join(map(str, b[:n - (k - 1)]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = input()
    result = cipher(k, s)
    fptr.write(result + '\n')
    fptr.close()
