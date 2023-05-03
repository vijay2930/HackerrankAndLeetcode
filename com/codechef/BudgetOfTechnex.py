"""
https://www.codechef.com/problems/BUDTECH
"""


def budgetOfTechnex(x):
    return x * 100


T = int(input())
testCase = [int(input()) for _ in range(T)]

for x in testCase:
    print(budgetOfTechnex(x))
