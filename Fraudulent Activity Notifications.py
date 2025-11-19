#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Frequency array for values 0 to 200
    freq = [0] * 201
    
    # Initialize frequency with first d days
    for i in range(d):
        freq[expenditure[i]] += 1

    def get_median(freq, d):
        count = 0
        if d % 2 == 1:
            # Odd: middle element
            mid = d // 2 + 1
            for i in range(201):
                count += freq[i]
                if count >= mid:
                    return i
        else:
            # Even: average of two middle elements
            first = None
            mid1 = d // 2
            mid2 = mid1 + 1
            for i in range(201):
                count += freq[i]
                if first is None and count >= mid1:
                    first = i
                if count >= mid2:
                    return (first + i) / 2

    notifications = 0
    n = len(expenditure)

    for i in range(d, n):
        median = get_median(freq, d)

        if expenditure[i] >= 2 * median:
            notifications += 1

        # Update sliding window:
        # Remove old value
        freq[expenditure[i - d]] -= 1
        # Add new value
        freq[expenditure[i]] += 1

    return notifications


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    fptr.write(str(result) + '\n')
    fptr.close()
