import os
import sys
from collections import deque

def stoneDivision(n, S_list):
    S = set(S_list)
    divisors = set([n])
    queue = deque([n])
    while queue:
        x = queue.popleft()
        for s_val in S:
            if s_val > x:
                continue
            if x % s_val == 0:
                next_d = x // s_val
                if next_d not in divisors:
                    divisors.add(next_d)
                    queue.append(next_d)
                    
    divisors_sorted = sorted(divisors)
    
    dp = {}
    for d in divisors_sorted:
        moves_set = set()
        for s_val in S:
            if s_val > d:
                continue
            if d % s_val == 0:
                child = d // s_val
                if s_val % 2 == 1:
                    moves_set.add(dp[child])
                else:
                    moves_set.add(0)
        mex_val = 0
        while mex_val in moves_set:
            mex_val += 1
        dp[d] = mex_val
        
    if dp[n] != 0:
        return "First"
    else:
        return "Second"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))
    result = stoneDivision(n, s)
    fptr.write(result + '\n')
    fptr.close()
