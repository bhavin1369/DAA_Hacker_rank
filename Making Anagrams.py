#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    freq = [0] * 26

    # count characters from s1
    for ch in s1:
        freq[ord(ch) - 97] += 1

    # subtract characters from s2
    for ch in s2:
        freq[ord(ch) - 97] -= 1

    # sum of absolute differences = deletions needed
    deletions = sum(abs(x) for x in freq)
    return deletions
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
