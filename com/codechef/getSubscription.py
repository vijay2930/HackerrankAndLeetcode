"""
https://www.codechef.com/problems/SUBSCRIBE
"""


def getSubscription(timing):
    return ("NO", "YES")[timing > 30]


T = int(input())
testCases = [int(input()) for _ in range(T)]

for timing in testCases:
    print(getSubscription(timing))
