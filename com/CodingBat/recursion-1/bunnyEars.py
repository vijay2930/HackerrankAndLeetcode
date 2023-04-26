"""
https://codingbat.com/prob/p183649
"""


def bunny_ears(bunnies):
    if bunnies == 0:
        return 0
    return bunny_ears(bunnies-1)+2


print(bunny_ears(2))
print(bunny_ears(1))
print(bunny_ears(0))
