"""
https://www.geeksforgeeks.org/move-zeroes-end-array/
"""


def move_all_zero_to_end(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    print(nums)


move_all_zero_to_end([5, 6, 0, 4, 6, 0, 9, 0, 8])
