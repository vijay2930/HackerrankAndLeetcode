"""
https://www.codechef.com/problems/TYRE
"""


def tyreProblem(n, m):
    return n * 2 + m * 4


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for n, m in testCase:
    print(tyreProblem(n, m))
