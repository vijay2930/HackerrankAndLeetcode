"""
https://www.codechef.com/problems/PODIUM
"""


def podiumFinish(a, b):
    return a + b


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for a, b in testCase:
    print(podiumFinish(a, b))
