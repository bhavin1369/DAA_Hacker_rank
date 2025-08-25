#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    def is_kaprekar(n: int) -> bool:
        d = len(str(n))
        sq = str(n ** 2)
        r = sq[-d:]               # right part
        l = sq[:-d] if sq[:-d] else "0"
        l, r = int(l), int(r)
        return l + r == n

    results = [n for n in range(p, q + 1) if is_kaprekar(n)]
    
    if results:
        print(" ".join(map(str, results)))
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)
