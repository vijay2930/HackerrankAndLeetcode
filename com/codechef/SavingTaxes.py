"""
https://www.codechef.com/problems/TAXSAVING
"""

T = int(input())

rupees_per_year = [list(map(int, input().split())) for _ in range(T)]

for amount, tax in rupees_per_year:
    print(amount - tax)
