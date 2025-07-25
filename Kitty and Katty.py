#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    T = int(input().strip())
    
    for _ in range(T):
        n = int(input().strip())
        if n == 1:
            print("Kitty")
        elif n % 2 == 0:
            print("Kitty")
        else:
            print("Katty")
