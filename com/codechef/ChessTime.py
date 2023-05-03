"""
https://www.codechef.com/problems/CHESSTIME
"""


def chessTime(hour):
    return (hour * 60) // 20


T = int(input())
testCase = [int(input()) for _ in range(T)]

for hour in testCase:
    print(chessTime(hour))
