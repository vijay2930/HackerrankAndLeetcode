"""
https://www.codechef.com/problems/CWIREFRAME
"""


def chefAndWireFrames(n, m, x):
    return (n * 2 + m * 2) * x


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for n, m, x in testCase:
    print(chefAndWireFrames(n, m, x))
