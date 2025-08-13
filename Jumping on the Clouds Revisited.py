#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100
    position = 0
    
    while True:
        # Jump to next cloud
        position = (position + k) % n
        # Reduce energy for the jump
        energy -= 1
        # If it's a thunderhead, reduce 2 more
        if c[position] == 1:
            energy -= 2
        # If back to start, break
        if position == 0:
            break
    
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, k)
    fptr.write(str(result) + '\n')
    fptr.close()
