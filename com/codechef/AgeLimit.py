"""
https://www.codechef.com/problems/AGELIMIT
"""

T = int(input())
ages = list(list(map(int, input().split())) for _ in range(T))
for X, Y, A in ages:
    if X <= A < Y:
        print("YES")
    else:
        print("NO")