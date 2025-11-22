#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 == 1:
        return -1
    
    half = len(s) // 2
    a = s[:half]
    b = s[half:]
    
    # Count frequency
    freq = [0] * 26
    for ch in a:
        freq[ord(ch) - 97] += 1
    for ch in b:
        freq[ord(ch) - 97] -= 1
    
    # Characters that appear more in B than A must be changed
    changes = 0
    for x in freq:
        if x < 0:
            changes += -x
    
    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
