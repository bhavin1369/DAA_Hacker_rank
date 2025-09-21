#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Convert characters to ASCII values
    ascii_values = [ord(c) for c in s]
    reverse_ascii = ascii_values[::-1]
    
    # Compute differences
    diff_original = [abs(ascii_values[i] - ascii_values[i-1]) for i in range(1, len(ascii_values))]
    diff_reverse = [abs(reverse_ascii[i] - reverse_ascii[i-1]) for i in range(1, len(reverse_ascii))]
    
    # Compare both lists
    if diff_original == diff_reverse:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        fptr.write(result + '\n')
    fptr.close()
