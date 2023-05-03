"""
https://www.codechef.com/problems/CABS
"""


def cheaperCab(x, y):
    if x < y:
        return "FIRST"
    if y < x:
        return "SECOND"
    return "ANY"


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(cheaperCab(x, y))
