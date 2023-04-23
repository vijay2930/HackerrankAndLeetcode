"""
https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true
"""

import math
import os
import random
import re
import sys


def simpleArraySum(arr):
    sum = 0
    for val in arr:
        sum += val
    return sum


if __name__ == '__main__':
    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)
