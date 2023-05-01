"""
https://www.codechef.com/problems/BIRYANI
"""

T = int(input())
cooking_classes = [list(map(int, input().split())) for _ in range(T)]
for cooking_class, cost in cooking_classes:
    print(cooking_class * cost)
