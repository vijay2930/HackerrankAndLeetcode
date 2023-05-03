"""
https://www.codechef.com/problems/LTIME
"""
import sys


def lunchTime(x):
    return ("NO", "YES")[1 <= x <= 4]


T = int(sys.stdin.readline())
testCase = [int(sys.stdin.readline()) for _ in range(T)]

for x in testCase:
    sys.stdout.write(str(lunchTime(x))+"\n")
