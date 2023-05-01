"""
https://www.codechef.com/problems/DNATION
"""


def chefAndDonation(x, y):
    return y - x


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(chefAndDonation(x, y))

