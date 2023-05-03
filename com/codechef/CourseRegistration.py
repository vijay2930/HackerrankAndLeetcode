"""
https://www.codechef.com/problems/COURSEREG
"""


def course(n, m, k):
    return ("NO", "YES")[(n + k) <= m]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for n, m, k in testCase:
    print(course(n, m, k))
