"""
https://www.codechef.com/problems/INVESTMENT
"""
import sys


def goodInvestmentOrNot(x, y):
    return ("NO", "YES")[x >= y * 2]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(goodInvestmentOrNot(x, y))
