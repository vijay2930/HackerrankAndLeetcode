"""
https://www.codechef.com/problems/BUDGET_
"""


def monthlyBudget(x, y):
    return ("NO", "YES")[0 <= x - y * 30]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(monthlyBudget(x, y))
