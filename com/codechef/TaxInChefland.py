"""
https://www.codechef.com/problems/TAXES
"""

T = int(input())
taxes = [int(input()) for _ in range(T)]
for tax in taxes:
    print((tax, tax - 10)[tax > 100])
