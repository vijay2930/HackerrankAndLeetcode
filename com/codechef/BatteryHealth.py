"""
https://www.codechef.com/problems/BTRYHLTH
"""


def batterHealth(percentage):
    return ("NO", "YES")[percentage >= 80]


T = int(input())
totalTestCase = [int(input()) for _ in range(T)]
for percentage in totalTestCase:
    print(batterHealth(percentage))
