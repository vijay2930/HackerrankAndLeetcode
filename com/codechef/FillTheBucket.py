"""
https://www.codechef.com/problems/FBC
"""


def fillTheBucket(k, x):
    return k - x


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for k, x in testCase:
    print(fillTheBucket(k, x))
