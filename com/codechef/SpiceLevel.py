"""
https://www.codechef.com/problems/KITCHENSPICE
"""


def spiceLevel(x):
    if x < 4:
        return "MILD"
    if 4 <= x < 7:
        return "MEDIUM"
    return "HOT"


T = int(input())
testCase = [int(input()) for _ in range(T)]

for x in testCase:
    print(spiceLevel(x))
