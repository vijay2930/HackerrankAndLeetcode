"""
https://www.codechef.com/problems/PAR2
"""


def parity(chocolate):
    return ("YES", "NO")[chocolate % 2]


T = int(input())
total_chocolates = [int(input()) for _ in range(T)]
for chocolate in total_chocolates:
    print(parity(chocolate))
