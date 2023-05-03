"""
https://www.codechef.com/problems/CANDYSTORE
"""


def candyStore(x, y):
    if x >= y:
        return y
    return x + (y - x) * 2


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(candyStore(x, y))
