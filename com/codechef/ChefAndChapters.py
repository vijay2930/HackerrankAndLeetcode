"""
https://www.codechef.com/problems/SEMCOURSES
"""
import sys


def chefAndChapters(x, y, z):
    return x * y * z


T = int(sys.stdin.readline())
testCase = [map(int, sys.stdin.readline().split(" ")) for _ in range(T)]

for x, y, z in testCase:
    sys.stdout.write(str(chefAndChapters(x, y, z)))
