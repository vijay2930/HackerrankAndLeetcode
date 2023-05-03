"""
https://www.codechef.com/problems/PROINC
"""


def profitIncrement(x, y):
    val = int(10 / 100 * x)
    return int((x + val) - (x - y))


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(profitIncrement(x, y))
