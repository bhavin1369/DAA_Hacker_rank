#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    max_height = 0
    for char in word:
        index = ord(char.lower()) - ord('a')
        if index < 0 or index >= len(h):  # Handle potential index errors
            return 0
        letter_height = h[index]
        if letter_height > max_height:
            max_height = letter_height
    return max_height * len(word)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)
    fptr.write(str(result) + '\n')
    fptr.close()
