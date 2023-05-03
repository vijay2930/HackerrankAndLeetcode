"""
https://www.codechef.com/problems/MINCOINSREQ
"""


def minimumCoins(x):
    return x % 10


T = int(input())
testCase = [int(input()) for _ in range(T)]

for x in testCase:
    print(minimumCoins(x))
