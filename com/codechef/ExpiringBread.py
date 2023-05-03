"""
https://www.codechef.com/problems/EXPIRY
"""


def expiringBread(n, m, k):
    return ("NO", "YES")[0 >= n - m * k]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for n, m, k in testCase:
    print(expiringBread(n, m, k))
