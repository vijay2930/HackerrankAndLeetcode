"""
https://www.codechef.com/problems/READPAGES
"""


def readPages(n, x, y):
    return ("NO", "YES")[n <= x * y]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]
for n, x, y in testCase:
    print(readPages(n, x, y))
