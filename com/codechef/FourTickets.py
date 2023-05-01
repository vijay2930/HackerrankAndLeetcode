"""
https://www.codechef.com/problems/FOURTICKETS
"""


def fourTicketsCost(money):
    return ("NO", "YES")[money * 4 <= 1000]


T = int(input())
testCases = [int(input()) for _ in range(T)]
for money in testCases:
    print(fourTicketsCost(money))
