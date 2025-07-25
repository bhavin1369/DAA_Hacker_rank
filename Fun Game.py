#!/bin/python3

import math
import os
import random
import re
import sys

def funGame(a, b):
    n = len(a)
    moves = []

    # Create list of tuples: (total value, index)
    for i in range(n):
        moves.append((a[i] + b[i], i))

    # Sort moves by total value descending
    moves.sort(reverse=True)

    score_first = 0
    score_second = 0

    # Simulate turns
    for turn, (_, idx) in enumerate(moves):
        if turn % 2 == 0:  # First's turn
            score_first += a[idx]
        else:              # Second's turn
            score_second += b[idx]

    if score_first > score_second:
        return "First"
    elif score_second > score_first:
        return "Second"
    else:
        return "Tie"

# Main driver (HackerRank-style)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().rstrip().split()))
        b = list(map(int, input().rstrip().split()))
        result = funGame(a, b)
        fptr.write(result + '\n')
    fptr.close()
