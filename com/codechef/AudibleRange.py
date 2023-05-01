"""
https://www.codechef.com/problems/AUDIBLE
"""


def audible_range(r):
    return ("NO", "YES")[67 <= r <= 45000]


T = int(input())
audio = [int(input()) for _ in range(T)]
for r in audio:
    print(audible_range(r))
