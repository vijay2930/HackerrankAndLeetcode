"""
https://www.codechef.com/problems/COMPLEXITY
"""


def timeComplexity(a, b):
    return ("NO", "YES")[a > b]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for a, b in testCase:
    print(timeComplexity(a, b))
