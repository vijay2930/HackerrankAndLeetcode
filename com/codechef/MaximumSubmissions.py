"""
https://www.codechef.com/problems/MAXIMUMSUBS
"""


def maximumSubmissions(x):
    return x * 2


T = int(input())
testCase = [int(input()) for _ in range(T)]

for x in testCase:
    print(maximumSubmissions(x))
