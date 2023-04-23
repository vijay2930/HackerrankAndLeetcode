"""
https://leetcode.com/problems/two-sum/
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in num_map:
                return num_map[diff], index
            num_map[diff] = index
