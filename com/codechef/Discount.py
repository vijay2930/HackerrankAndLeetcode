"""
https://www.codechef.com/problems/DISCNT
"""


def discount(price):
    return 100 - price


T = int(input())
testCase = [int(input()) for _ in range(T)]

for price in testCase:
    print(discount(price))
