"""
https://www.codechef.com/problems/ADVANCE
"""


def ratingImprovement(x, y):
    return ("NO", "YES")[x <= y <= (x + 200)]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(ratingImprovement(x, y))
