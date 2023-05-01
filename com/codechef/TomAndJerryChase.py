"""
https://www.codechef.com/problems/JERRYCHASE
"""

T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]


def tomAndJerryChase(x, y):
    return ("NO", "YES")[x < y]


for x, y in testCase:
    print(tomAndJerryChase(x, y))
