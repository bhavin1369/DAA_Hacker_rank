#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    # Sort space station positions
    c.sort()
    # Distance before the first space station
    max_dist = c[0]
    # Distance after the last space station
    max_dist = max(max_dist, n - 1 - c[-1])
    # Maximum gap between consecutive space stations
    for i in range(1, len(c)):
        max_dist = max(max_dist, (c[i] - c[i - 1]) // 2)
    return max_dist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)
    fptr.write(str(result) + '\n')
    fptr.close()
