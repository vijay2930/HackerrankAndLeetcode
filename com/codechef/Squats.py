"""
https://www.codechef.com/problems/SQUATS
"""

T = int(input())
squats = [int(input()) for _ in range(T)]
for s in squats:
    print(s * 15)
