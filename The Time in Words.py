#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    words = {
        1: "one",       2: "two",        3: "three",     4: "four",
        5: "five",      6: "six",        7: "seven",     8: "eight",
        9: "nine",      10: "ten",       11: "eleven",   12: "twelve",
        13: "thirteen", 14: "fourteen",  15: "quarter",  16: "sixteen",
        17: "seventeen",18: "eighteen", 19: "nineteen", 20: "twenty",
        21: "twenty one", 22: "twenty two", 23: "twenty three",
        24: "twenty four", 25: "twenty five", 26: "twenty six",
        27: "twenty seven", 28: "twenty eight", 29: "twenty nine",
        30: "half"
    }

    # Exact hour
    if m == 0:
        return f"{words[h]} o' clock"

    # Minutes past
    if m <= 30:
        if m == 15:
            return f"quarter past {words[h]}"
        if m == 30:
            return f"half past {words[h]}"
        if m == 1:
            return f"one minute past {words[h]}"
        return f"{words[m]} minutes past {words[h]}"

    # Minutes to next hour
    remain = 60 - m
    next_hour = h + 1 if h < 12 else 1

    if remain == 15:
        return f"quarter to {words[next_hour]}"
    if remain == 1:
        return f"one minute to {words[next_hour]}"
    return f"{words[remain]} minutes to {words[next_hour]}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
