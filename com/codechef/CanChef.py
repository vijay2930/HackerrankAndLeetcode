"""
https://www.codechef.com/problems/CANCHEF
"""


def canChef(x, y):
    return ("NO", "YES")[x * 15 >= 2 * y]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(canChef(x, y))
