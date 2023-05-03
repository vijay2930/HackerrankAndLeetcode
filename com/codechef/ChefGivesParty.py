"""
https://www.codechef.com/problems/PARTY2
"""


def chefGivesParty(x, y, z):
    return ("NO", "YES")[x * y <= z]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y, z in testCase:
    print(chefGivesParty(x, y, z))
