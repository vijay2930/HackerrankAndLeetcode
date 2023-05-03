"""
https://www.codechef.com/problems/SLEEP
"""


def sleepDeprivation(slept):
    return ("NO", "YES")[slept < 7]


T = int(input())
testCase = [int(input()) for _ in range(T)]

for slept in testCase:
    print(sleepDeprivation(slept))
