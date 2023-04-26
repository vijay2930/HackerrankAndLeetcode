"""
https://codingbat.com/prob/p107330
"""


def bunnyEars2(bunnies):
    ears = 2
    if bunnies == 0:
        return 0
    if bunnies % 2 == 0:
        ears = 3
    return bunnyEars2(bunnies - 1) + ears
