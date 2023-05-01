"""
https://www.codechef.com/problems/WAITTIME
"""


def waitingTime(k, x):
    return k * 7 - x


T = int(input())
testCases = [map(int, input().split(" ")) for _ in range(T)]

for k, x in testCases:
    print(waitingTime(k, x))
