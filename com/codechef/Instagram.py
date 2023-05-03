"""
https://www.codechef.com/problems/INSTAGRAM
"""


def instagram(x, y):
    return ("NO", "YES")[x > y * 10]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]
for x, y in testCase:
    print(instagram(x, y))
