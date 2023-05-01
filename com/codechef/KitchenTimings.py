"""
https://www.codechef.com/problems/KITCHENTIME
"""

T = int(input())
timings = [list(map(int, input().split(" "))) for _ in range(T)]
for start, end in timings:
    print(end - start)
