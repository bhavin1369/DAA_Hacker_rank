#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    from collections import Counter
    
    freq = Counter(s)
    
    # Count how many characters have an odd occurrence
    odd_count = sum(1 for c in freq.values() if c % 2 != 0)
    
    # A palindrome can have at most one odd-frequency character
    return "YES" if odd_count <= 1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
