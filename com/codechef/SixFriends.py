"""
https://www.codechef.com/problems/SIXFRIENDS
"""


def sixFriends(x, y):
    cost1 = x * 3
    cost2 = y * 2
    return (cost1, cost2)[cost1 > cost2]


T = int(input())
testCase = [map(int, input().split(" ")) for _ in range(T)]

for x, y in testCase:
    print(sixFriends(x, y))
