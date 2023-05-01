"""
https://www.codechef.com/problems/MY1STCONTEST
"""


def myFirstContest(a, b, n):
    return (a - b, a - b - n)


a, b, n = map(int, input().split(" "))
print(*myFirstContest(a, b, n))
