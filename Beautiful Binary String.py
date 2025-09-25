#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    count = 0
    i = 0
    n = len(b)
    while i < n - 2:
        # Check if current position starts with "010"
        if b[i:i+3] == "010":
            count += 1
            # Skip ahead to avoid overlapping patterns
            i += 3
        else:
            i += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    b = input()
    result = beautifulBinaryString(b)
    fptr.write(str(result) + '\n')
    fptr.close()
