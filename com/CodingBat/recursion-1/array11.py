"""
https://codingbat.com/prob/p135988
"""


def array11(nums, index):
    if len(nums) == index:
        return 0
    count = (0, 1)[nums[index] == 11]
    return count + array11(nums, index+1)
