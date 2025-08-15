#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Find the length of the common prefix
    common_length = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_length += 1
        else:
            break

    # Total moves needed to delete the rest of s and add rest of t
    min_ops = (len(s) - common_length) + (len(t) - common_length)

    # Check if it's possible in exactly k moves
    if k >= len(s) + len(t):  # We can delete all and re-add
        return "Yes"
    elif k >= min_ops and (k - min_ops) % 2 == 0:
        return "Yes"
    else:
        return "No"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    t = input()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    fptr.write(result + '\n')
    fptr.close()
