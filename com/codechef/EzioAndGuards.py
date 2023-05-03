"""
https://www.codechef.com/problems/MANIPULATE
"""


def ezioAndGuards(x, y):
    return ("NO", "YES")[x >= y]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(ezioAndGuards(x, y))
