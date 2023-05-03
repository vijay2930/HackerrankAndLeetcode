"""
https://www.codechef.com/problems/FEVER
"""


def fever(degree):
    return ("NO", "YES")[degree > 98]


T = int(input())
testCase = [int(input()) for _ in range(T)]

for x in testCase:
    print(fever(x))
