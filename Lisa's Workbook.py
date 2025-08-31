#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    special_count=0
    current_page=1
    for problems_in_chapter in arr:
        num_pages=(problems_in_chapter+k-1)//k
        for j in range(num_pages):
            start_problem=j*k+1
            end_problem=min((j+1)*k,problems_in_chapter)
            page_number=current_page+j
            if start_problem<=page_number<=end_problem:
                special_count+=1
        current_page+=num_pages
    return special_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
