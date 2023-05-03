"""
https://www.codechef.com/problems/CCHOCOLATES
"""


def chefAndChocolate(x, y, z):
    return (x * 5 + y * 10) // z


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y, z in testCase:
    print(chefAndChocolate(x, y, z))
