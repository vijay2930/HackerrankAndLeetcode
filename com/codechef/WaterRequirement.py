"""
https://www.codechef.com/problems/WATERREQ
"""
import sys


def waterRequirement(n):
    return n * 2


T = int(sys.stdin.readline())
testCase = [int(sys.stdin.readline()) for _ in range(T)]

for n in testCase:
    sys.stdout.write(str(waterRequirement(n)+"\n"))
