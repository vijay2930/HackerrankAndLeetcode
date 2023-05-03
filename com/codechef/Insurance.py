"""
https://www.codechef.com/problems/INSURANCE
"""


def insurance(x, y):
    return (x, y)[x > y]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(insurance(x, y))
