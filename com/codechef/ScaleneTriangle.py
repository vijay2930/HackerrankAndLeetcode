"""
https://www.codechef.com/problems/SCALENE
"""


def scaleneTriangle(a, b, c):
    return ("NO", "YES")[a != b != c]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for a, b, c in testCase:
    print(scaleneTriangle(a, b, c))
