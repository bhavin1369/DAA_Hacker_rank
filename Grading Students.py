#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            remainder = grade % 5
            if remainder >= 3:
                grade += (5 - remainder)
            result.append(grade)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
