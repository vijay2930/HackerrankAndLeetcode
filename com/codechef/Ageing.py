"""
https://www.codechef.com/problems/AGEING
"""


def ageing(age):
    return age - 10


T = int(input())
testCase = [int(input()) for _ in range(T)]
for age in testCase:
    print(ageing(age))
