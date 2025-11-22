#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    s = s.replace(" ", "")
    L = len(s)

    import math
    rows = int(math.floor(math.sqrt(L)))
    cols = int(math.ceil(math.sqrt(L)))

    # Ensure rows * cols >= L
    if rows * cols < L:
        rows += 1

    # Build encoded words column-by-column
    result = []
    for c in range(cols):
        word = []
        for r in range(rows):
            idx = r * cols + c
            if idx < L:
                word.append(s[idx])
        result.append("".join(word))

    return " ".join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
