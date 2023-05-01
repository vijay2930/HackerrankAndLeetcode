"""
https://www.codechef.com/problems/LUDO
"""

T = int(input())
dice_rolled = [int(input()) for _ in range(T)]
for dice in dice_rolled:
    print(("NO", "YES")[dice == 6])
