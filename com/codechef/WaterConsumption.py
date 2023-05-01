"""
https://www.codechef.com/problems/WATERCONS
"""

T = int(input())
each_days_consumption = [int(input()) for _ in range(T)]
for water in each_days_consumption:
    if water >= 2000:
        print("YES")
    else:
        print("NO")
