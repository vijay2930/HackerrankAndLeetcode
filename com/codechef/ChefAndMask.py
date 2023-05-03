"""
https://www.codechef.com/problems/CMASKS
"""


def chefAndMask(x, y):
    return ("Cloth", "Disposable")[100 * x < y * 10]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(chefAndMask(x, y))
