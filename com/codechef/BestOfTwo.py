"""
https://www.codechef.com/problems/BESTOFTWO
"""


def bestOfTwo(a, b):
    return (a, b)[b > a]


t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    print(bestOfTwo(X, Y))
