"""
https://www.codechef.com/problems/BURGERS
"""
T = int(input())
burgers = [list(map(int, input().split())) for _ in range(T)]
for patties, buns in burgers:
    print(patties if patties < buns else buns)
