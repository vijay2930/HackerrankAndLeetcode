"""
https://www.codechef.com/problems/EQUALDIST
"""


def equalDistribution(a, b):
    return ("YES", "NO")[(a + b) % 2]


T = int(input())

testCase = [map(int, input().split(" ")) for _ in range(T)]

for a, b in testCase:
    print(equalDistribution(a, b))
