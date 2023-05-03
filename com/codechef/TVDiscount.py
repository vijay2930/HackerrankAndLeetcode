"""
https://www.codechef.com/problems/TVDISC
"""


def tvDiscount(a, b, c, d):
    val1 = a - c
    val2 = b - d
    if val1 == val2:
        return "ANY"
    return ("FIRST", "SECOND")[val1 > val2]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for a, b, c, d in testCase:
    print(tvDiscount(a, b, c, d))
