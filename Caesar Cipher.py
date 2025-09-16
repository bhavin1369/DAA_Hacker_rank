#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result = []
    k = k % 26  # Handle rotations larger than 26
    for char in s:
        if char.isalpha():
            # Determine if it's uppercase or lowercase
            if char.isupper():
                base = ord('A')
                shifted = (ord(char) - base + k) % 26 + base
                result.append(chr(shifted))
            else:
                base = ord('a')
                shifted = (ord(char) - base + k) % 26 + base
                result.append(chr(shifted))
        else:
            # Keep non-alphabet characters as they are
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)
    fptr.write(result + '\n')
    fptr.close()
