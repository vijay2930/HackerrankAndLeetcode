"""
https://www.codechef.com/problems/MAXDIFFMIN
"""


def maxMinusMin(a, b, c):
    return c - a


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]
for a, b, c in testCase:
    print(maxMinusMin(a, b, c))
