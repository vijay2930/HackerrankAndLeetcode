"""
https://www.codechef.com/problems/MANAPTS
"""


def manaPoints(x, y):
    return y // x


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]
for x, y in testCase:
    print(manaPoints(x, y))
