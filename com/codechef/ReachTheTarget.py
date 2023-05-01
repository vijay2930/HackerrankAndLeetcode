"""
https://www.codechef.com/problems/REACHTARGET
"""


def reachTheTarget(x, y):
    return x - y


T = int(input())
total = [list(map(int, input().split())) for _ in range(T)]
for x, y in total:
    print(reachTheTarget(x, y))
