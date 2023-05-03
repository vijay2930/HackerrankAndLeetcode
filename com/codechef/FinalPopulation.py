"""
https://www.codechef.com/problems/POPULATION
"""


def finalPopulation(x, y, z):
    return x - y + z


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y, z in testCase:
    print(finalPopulation(x, y, z))
