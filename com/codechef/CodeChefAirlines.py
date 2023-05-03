"""
https://www.codechef.com/problems/AIRLINES
"""

T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]


def codeChefAirLines(x, y, z):
    total = min(x * 10, y)
    return total * z


for x, y, z in testCase:
    print(codeChefAirLines(x, y, z))
