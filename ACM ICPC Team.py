#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topics):
    n = len(topics)
    max_topics = 0
    team_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            # Combine knowledge of team members
            combined = bin(int(topics[i], 2) | int(topics[j], 2))
            # Count '1's (topics known)
            topic_count = combined.count('1')

            if topic_count > max_topics:
                max_topics = topic_count
                team_count = 1
            elif topic_count == max_topics:
                team_count += 1

    return [max_topics, team_count]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)
    result = acmTeam(topic)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
