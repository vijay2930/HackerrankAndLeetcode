"""
https://www.codechef.com/problems/TALLER
"""


def whoIsTaller(a, b):
    return ("A", "B")[b > a]


T = int(input())
heights = [list(map(int, input().split())) for _ in range(T)]
for a, b in heights:
    print(whoIsTaller(a, b))
