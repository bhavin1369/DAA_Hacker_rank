#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    n = len(s)
    # Try each possible starting length
    for i in range(1, n // 2 + 1):
        first_num = int(s[:i])
        num = first_num
        built = str(num)
        # Keep building the sequence until it matches or exceeds the input
        while len(built) < n:
            num += 1
            built += str(num)
        # Check if the built string equals the input
        if built == s:
            print("YES", first_num)
            return    
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        separateNumbers(s)
