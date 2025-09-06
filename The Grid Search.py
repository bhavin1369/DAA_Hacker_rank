#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    rows_G = len(G)
    cols_G = len(G[0])
    rows_P = len(P)
    cols_P = len(P[0])

    # Traverse through grid
    for i in range(rows_G - rows_P + 1):  # possible starting rows
        for j in range(cols_G - cols_P + 1):  # possible starting cols
            # Check if the subgrid matches the pattern
            found = True
            for x in range(rows_P):
                if G[i + x][j:j + cols_P] != P[x]:
                    found = False
                    break
            if found:
                return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        R = int(first_multiple_input[0])
        C = int(first_multiple_input[1])
        G = []
        for _ in range(R):
            G_item = input()
            G.append(G_item)
        second_multiple_input = input().rstrip().split()
        r = int(second_multiple_input[0])
        c = int(second_multiple_input[1])
        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)
        result = gridSearch(G, P)
        fptr.write(result + '\n')
    fptr.close()
