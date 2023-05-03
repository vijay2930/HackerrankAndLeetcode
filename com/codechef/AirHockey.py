"""
https://www.codechef.com/problems/AIRHOCKEY
"""


def airHockey(a, b):
    return (7 - a, 7 - b)[a < b]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for a, b in testCase:
    print(airHockey(a, b))
