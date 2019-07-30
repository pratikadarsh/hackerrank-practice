#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    names = s.split()
    for name in names:
        name = list(name)
        print("inside : ", names)
    print(names)

if __name__ == '__main__':
    s = input()
    result = solve(s)
    #print(result)
