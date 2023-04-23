"""
https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
"""


def staircase(n):
    space = n - 1
    for i in range(1, n + 1):
        print(" " * space, "#" * i, sep="")
        space -= 1


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
