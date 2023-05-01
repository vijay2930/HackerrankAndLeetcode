"""
https://www.codechef.com/problems/KNGTOR
"""


def tourOfKing(n, m):
    return n * 5 + m * 7


T = int(input())
cars = [list(map(int, input().split(" "))) for _ in range(T)]
for car in cars:
    print(tourOfKing(*car))
