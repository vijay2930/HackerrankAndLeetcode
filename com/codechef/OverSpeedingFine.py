"""
https://www.codechef.com/problems/FINE
"""


def overSpeedingFine(speed):
    if speed <= 70:
        return 0
    elif 70 < speed <= 100:
        return 500
    else:
        return 2000


T = int(input())
testCase = [int(input()) for _ in range(T)]
for speed in testCase:
    print(overSpeedingFine(speed))
