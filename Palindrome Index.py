#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    i, j = 0, len(s) - 1
    
    # Move inward until a mismatch
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    
    # If fully matched, it's already a palindrome
    if i >= j:
        return -1
    
    # Try removing s[i]
    if s[i+1:j+1] == s[i+1:j+1][::-1]:
        return i
    
    # Try removing s[j]
    if s[i:j] == s[i:j][::-1]:
        return j
    
    # Otherwise no solution
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
