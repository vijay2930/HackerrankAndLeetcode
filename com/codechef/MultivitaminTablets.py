"""
https://www.codechef.com/problems/TABLETS
"""


def multivitaminTablets(x, y):
    return ("NO", "YES")[x * 3 <= y]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(multivitaminTablets(x, y))
