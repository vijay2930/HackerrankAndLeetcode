"""
https://www.codechef.com/problems/MINHEIGHT
"""

T = int(input())
heights = [map(int, input().split(" ")) for _ in range(T)]


def rollerCoster(x, h):
    return ("NO", "YES")[x >= h]


for x, h in heights:
    print(rollerCoster(x, h))
