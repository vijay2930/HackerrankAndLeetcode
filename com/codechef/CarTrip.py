"""
https://www.codechef.com/problems/CARTRIP
"""


def carTrip(x):
    if x <= 300:
        return 3000
    return x * 10


T = int(input())
testCase = [int(input()) for _ in range(T)]

for x in testCase:
    print(carTrip(x))
