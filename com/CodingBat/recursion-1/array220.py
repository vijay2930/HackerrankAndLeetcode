"""
https://codingbat.com/prob/p173469
"""


def array220(nums, index):
    if len(nums) == index:
        return False
    if nums[index] * 10 == nums[index + 1]:
        return True
    return array220(nums, index + 1)
