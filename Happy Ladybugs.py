#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    from collections import Counter
    
    # Count frequencies of each character
    counts = Counter(b)
    
    # Case 1: If there's no empty cell ('_')
    if '_' not in counts:
        # Check if already happy
        for i in range(len(b)):
            if (i > 0 and b[i] == b[i-1]) or (i < len(b)-1 and b[i] == b[i+1]):
                continue
            else:
                return "NO"
        return "YES"
    
    # Case 2: There is at least one empty cell
    # Check if any color has only 1 ladybug (cannot be paired)
    for char, freq in counts.items():
        if char != '_' and freq == 1:
            return "NO"
    
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    g = int(input().strip())
    for g_itr in range(g):
        n = int(input().strip())
        b = input()
        result = happyLadybugs(b)
        fptr.write(result + '\n')
    fptr.close()
