"""
https://www.codechef.com/problems/SNDMAX
"""


def secondMaxOfThreeNumber(a, b, c):
    if a < b < c or c < b < a:
        return b
    elif b < c < a or a < c < b:
        return c
    else:
        return a


T = int(input())
testCase = [map(int, input().split()) for _ in range(T)]
for a, b, c in testCase:
    print(secondMaxOfThreeNumber(a, b, c))
