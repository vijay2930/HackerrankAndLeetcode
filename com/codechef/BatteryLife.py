"""
https://www.codechef.com/problems/BATTERYLOW
"""


def batteryLife(x):
    return ("NO", "YES")[x <= 15]


T = int(input())
testCase = [int(input()) for _ in range(T)]

for x in testCase:
    print(batteryLife(x))
