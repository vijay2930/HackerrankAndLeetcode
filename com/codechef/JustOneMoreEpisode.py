"""
https://www.codechef.com/problems/ONEMORE
"""


def justOneMoreEpisode(timeLeft):
    return ("NO", "YES")[timeLeft > 24]


T = int(input())
testCase = [int(input()) for _ in range(T)]
for timeLeft in testCase:
    print(justOneMoreEpisode(timeLeft))
