"""
https://www.codechef.com/problems/TIMELY
"""


def ReachOnTime(t):
    return ("NO", "YES")[t >= 30]


T = int(input())
time_of_reach = [int(input()) for _ in range(T)]
for time in time_of_reach:
    print(ReachOnTime(time))
