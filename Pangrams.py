#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s: str) -> str:
    # Convert string to lowercase
    s = s.lower()
    # Create a set of all alphabets
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    # Create a set of characters in the string
    letters_in_s = set(s)
    # Check if all alphabets are in the string
    if alphabet.issubset(letters_in_s):
        return "pangram"
    else:
        return "not pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = pangrams(s)
    fptr.write(result + '\n')
    fptr.close()
