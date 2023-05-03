"""
https://www.codechef.com/problems/FAIRPASS
"""


def passesForFair(n, k):
    return ("NO", "YES")[n < k]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for n, k in testCase:
    print(passesForFair(n, k))
