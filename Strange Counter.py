#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    # Initial cycle starts at 3 and length = 3
    cycle_length = 3
    start_time = 1
    
    # Find the cycle that contains time t
    while t > start_time + cycle_length - 1:
        start_time += cycle_length
        cycle_length *= 2
    
    # Compute value
    value = cycle_length - (t - start_time)
    return value
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    result = strangeCounter(t)
    fptr.write(str(result) + '\n')
    fptr.close()
