#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    expected = "SOS"
    count = 0
    # Check each group of 3 characters
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        # Compare each character in this group with expected "SOS"
        for j in range(3):
            if group[j] != expected[j]:
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = marsExploration(s)
    fptr.write(str(result) + '\n')
    fptr.close()
