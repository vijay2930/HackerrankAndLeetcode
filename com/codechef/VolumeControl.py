"""
https://www.codechef.com/problems/VOLCONTROL
"""


def volumeControl(x, y):
    if x < y:
        x, y = y, x
    return x - y


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(volumeControl(x, y))
