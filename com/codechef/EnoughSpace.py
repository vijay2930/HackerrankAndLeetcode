"""
https://www.codechef.com/problems/ENSPACE
"""


def enoughSpace(n, x, y):
    return ("NO", "YES")[x + y * 2 <= n]

T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]
for n, x, y in testCase:
        print(enoughSpace(n, x, y))
