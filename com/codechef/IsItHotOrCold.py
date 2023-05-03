"""
https://www.codechef.com/problems/HOTCOLD
"""


def isItHotOrCold(c):
    return ("COLD", "HOT")[c > 20]


T = int(input())
testCase = [int(input()) for _ in range(T)]

for c in testCase:
    print(isItHotOrCold(c))
