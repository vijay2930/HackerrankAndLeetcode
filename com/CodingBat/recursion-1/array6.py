"""
https://codingbat.com/prob/p108997
"""


def array6(nums, index):
    if len(nums) == index:
        return False
    if nums[index] == 6:
        return True
    return array6(nums, index + 1)

